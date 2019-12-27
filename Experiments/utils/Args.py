import yaml

class Args():
    def __init__(self, yamlfile):
        self.level = self.load_param(yamlfile,"level")
        self.state = self.load_param(yamlfile,"state")
        self.reward_experiment = self.load_param(yamlfile,"reward_experiment")
        self.dump_scores = self.load_param(yamlfile,"dump_scores")
        self.dump_full_episodes = self.load_param(yamlfile,"dump_full_episodes")
        self.render = self.load_param(yamlfile,"render")
        



    
    def load_param(self,yamlfile,parm_name):
        with open(yamlfile) as f:
                data = yaml.load(f, Loader=yaml.FullLoader)
                return data[parm_name]
        pass
    
    def __repr__(self):
        print('repr is missing')
        return ''