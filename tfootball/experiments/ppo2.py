
"""
Runs one instance of the Atari environment and optimizes using DQN algorithm.
Can use a GPU for the agent (applies to both sample and train). No parallelism
employed, so everything happens in one python process; can be easier to debug.

The kwarg snapshot_mode="last" to logger context will save the latest model at
every log point (see inside the logger for other options).

In viskit, whatever (nested) key-value pairs appear in config will become plottable
keys for showing several experiments.  If you need to add more after an experiment, 
use rlpyt.utils.logging.context.add_exp_param().

"""

from rlpyt.samplers.serial.sampler import SerialSampler
from rlpyt.envs.atari.atari_env import AtariEnv
from rlpyt.algos.dqn.dqn import DQN
from rlpyt.agents.dqn.atari.atari_dqn_agent import AtariDqnAgent
from rlpyt.runners.minibatch_rl import MinibatchRlEval
from rlpyt.utils.logging.context import logger_context
import argparse
import os


import gfootball.env as football_env

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

def build_and_train(game="academy_empty_goal_close", run_ID=0, cuda_idx=None):
    sampler = SerialSampler(
        EnvCls=create_single_football_env,
        env_kwargs=dict(game=game),
        eval_env_kwargs=dict(game=game),
        batch_T=4,  # Four time-steps per sampler iteration.
        batch_B=1,
        max_decorrelation_steps=0,
        eval_n_envs=10,
        eval_max_steps=int(10e3),
        eval_max_trajectories=5,
    )
    algo = DQN(min_steps_learn=1e3)  # Run with defaults.
    agent = AtariDqnAgent()
    runner = MinibatchRlEval(
        algo=algo,
        agent=agent,
        sampler=sampler,
        n_steps=50e6,
        log_interval_steps=1e3,
        affinity=dict(cuda_idx=cuda_idx),
    )
    config = dict(game=game)
    name = "dqn_" + game
    log_dir = "example_1"
    with logger_context(log_dir, run_ID, name, config, snapshot_mode="last"):
        runner.train()


def create_single_football_env(seed):
  """Creates gfootball environment."""
  env = football_env.create_environment(
      env_name=args.level, stacked=('stacked' in args.state),
      rewards=args.reward_experiment,
    #   logdir=logger.get_dir(),
    #   enable_goal_videos=args.dump_scores and (seed == 0),
    #   enable_full_episode_videos=args.dump_full_episodes and (seed == 0),
      render=args.render and (seed == 0),
      dump_frequency=50 if args.render and seed == 0 else 0)
#   env = monitor.Monitor(env, logger.get_dir() and os.path.join(logger.get_dir(),
#                                                                str(seed)))
  return env

if __name__ == "__main__":
    args = Args('football/tfootball/configs/first.yaml')
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--game', help='Atari game', default='pong')
    parser.add_argument('--run_ID', help='run identifier (logging)', type=int, default=0)
    parser.add_argument('--cuda_idx', help='gpu to use ', type=int, default=0)
    args1 = parser.parse_args()
    build_and_train(
        run_ID=args1.run_ID,
        cuda_idx=args1.cuda_idx,
    )
