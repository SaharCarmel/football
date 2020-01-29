
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
from rlpyt.algos.pg.ppo import PPO
from rlpyt.agents.pg.gaussian import GaussianPgAgent
from rlpyt.runners.minibatch_rl import MinibatchRlEval
from rlpyt.utils.logging.context import logger_context
import argparse
import os
from rlpyt.agents.pg.atari import AtariFfAgent, AtariLstmAgent
from rlpyt.agents.pg.coach import Coach

import gfootball.env as football_env


import yaml


class Args():
    def __init__(self, yamlfile):
        self.state = self.load_param(yamlfile, "state")
        self.reward_experiment = self.load_param(yamlfile, "reward_experiment")
        self.dump_scores = self.load_param(yamlfile, "dump_scores")
        self.dump_full_episodes = self.load_param(
            yamlfile, "dump_full_episodes")
        self.render = self.load_param(yamlfile, "render")
        self.initialQ = self.load_param(yamlfile, "initialQ") 
        self.beta = self.load_param(yamlfile, "Beta") 
        self.envVectorSize = self.load_param(yamlfile, "env_vector_size")
        self.envOptions = self.load_param(yamlfile, "env_options")

    def load_param(self, yamlfile, parm_name):
        with open(yamlfile) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data[parm_name]
        pass

    def __repr__(self):
        for key in self.__dict__.keys():
            print("{} : {}".format(key, self.__dict__[key]))
        return ''


def build_and_train(game="academy_empty_goal_close", run_ID=1, cuda_idx=None):
    env_vector_size = args.envVectorSize
    coach = Coach(envOptions=args.envOptions,
                  vectorSize=env_vector_size,
                  algo='Bandit',
                  initialQ=args.initialQ, 
                  beta=args.beta)
    sampler = SerialSampler(
        EnvCls=create_single_football_env,
        env_kwargs=dict(game=game),
        eval_env_kwargs=dict(game=game),
        batch_T=5,  # Four time-steps per sampler iteration.
        batch_B=env_vector_size,
        max_decorrelation_steps=0,
        eval_n_envs=1,
        eval_max_steps=int(10e3),
        eval_max_trajectories=5,
        coach = coach,
        eval_env = 'academy_empty_goal_close',
    )
    algo = PPO(minibatches=1)  # Run with defaults.
    agent = AtariLstmAgent() # TODO: move to ff
    runner = MinibatchRlEval(
        algo=algo,
        agent=agent,
        sampler=sampler,
        n_steps=10e6,
        log_interval_steps=1e3,
        affinity=dict(cuda_idx=cuda_idx),
    )
    config = dict(game=game)
    name = "soccer_" + game
    log_dir = "example_1"
    with logger_context(log_dir, run_ID, name, log_params=vars(args), snapshot_mode="last"):
        runner.train()


def create_single_football_env(seed, level='academy_empty_goal_close'):
    """Creates gfootball environment."""
    env = football_env.create_environment(
        env_name=level, stacked=('stacked' in args.state),
        rewards=args.reward_experiment,
        logdir='/dump',
        enable_goal_videos=args.dump_scores and (seed == 0),
        enable_full_episode_videos=args.dump_full_episodes and (seed == 0),
        render=args.render and (seed == 0),
        dump_frequency=1 if args.render and seed == 0 else 0)
    print("Creating env:{}".format(level))
#   env = monitor.Monitor(env, logger.get_dir() and os.path.join(logger.get_dir(),
#                                                                str(seed)))
    return env


if __name__ == "__main__":
    args = Args('football/Experiments/configs/first.yaml') ## TODO: move a copy of the file to the data file
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '--run_ID', help='run identifier (logging)', type=int, default=0)
    parser.add_argument('--cuda_idx', help='gpu to use ', type=int, default=0)
    args1 = parser.parse_args()
    build_and_train(
        run_ID=args1.run_ID,
        cuda_idx=args1.cuda_idx,
    )
