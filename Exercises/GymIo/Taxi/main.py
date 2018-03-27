"""this program prepares the taxi-v2 environment from gym.io
it the initiates the agent and tries him on the environment"""
from Agent import Agent
from Monitor import interact
import gym
import numpy as np

env = gym.make('Taxi-v2')
agent = Agent(alpha=0.1, gamma=1)
avg_rewards, best_avg_reward = interact(env, agent)
