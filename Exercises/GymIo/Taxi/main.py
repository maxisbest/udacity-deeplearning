from Agent import Agent
from Monitor import interact
import gym
import numpy as np

env = gym.make('Taxi-v2')
agent = Agent(alpha=0.1, gamma=1)
avg_rewards, best_avg_reward = interact(env, agent)
