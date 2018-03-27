import numpy as np
from collections import defaultdict

class Agent:

    def __init__(self, alpha, gamma, nA=6):
        """ Initialize agent"""
        self.nA = nA
        self.alpha = alpha
        self.gamma = gamma
        self.Q = defaultdict(lambda: np.zeros(self.nA))
        self.choices = np.arange(self.nA)

    def select_action(self, S1, i_episode):
        """selects the next state"""
        # set epsilon
        self.epsilon = 1 / ((i_episode + 1) * 10)
        A1 = np.random.choice(self.choices, p=self.epsilon_greedy_probs(S1))
        return A1

    def step(self, S1, A1, reward, S2, done):
        """selects next step"""
        if not done:
            A2_greedy = np.random.choice(self.choices, p=self.greedy_probs(S2))
            self.Q[S1][A1] = self.Q_update(self.Q[S1][A1], self.Q[S2][A2_greedy], reward)
        else:
            self.Q[S1][A1] = self.Q_update(self.Q[S1][A1], 0, reward)

    def Q_update(self, Q_S1_A1, Q_S2_A2, reward):
        """ updates the action-value function estimate using the most recent time step """
        return Q_S1_A1 * (1 - self.alpha) + (reward + self.gamma * Q_S2_A2) * self.alpha

    def greedy_probs(self, S):
        """ obtains the action probabilities corresponding to epsilon-greedy policy """
        probs = np.zeros(self.nA)
        mask = self.Q[S] == np.max(self.Q[S])
        greedy_choices = np.argwhere(mask)
        greedy_count = len(greedy_choices)
        probs[greedy_choices] = 1 / greedy_count
        return probs

    def epsilon_greedy_probs(self, S):
        """ obtains the action probabilities corresponding to epsilon-greedy policy """
        probs = np.ones(self.nA) * self.epsilon / self.nA
        mask = self.Q[S] == np.max(self.Q[S])
        greedy_choices = np.argwhere(mask)
        greedy_count = len(greedy_choices)
        probs[greedy_choices] = \
            (1 - ((self.nA - greedy_count) * self.epsilon / self.nA)) / greedy_count
        return probs
