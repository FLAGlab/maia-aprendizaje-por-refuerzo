import random
import numpy as np

class Bandit:
    def __init__(self,arms=10, epsilon=0.01):
        self.arms = [0]*arms
        self.epsilon = epsilon
        self.cumulative_rewards = [0]*arms
        self.occurrences = [0]*arms
        for i in range(0, arms):
            r = random.uniform(-3,3)
            self.arms[i] = r
        self.reward = 0
        
    def choose_arm(self):
        if random.uniform(0,1) < self.epsilon:
            return random.randint(1, len(self.arms))
        else:
            return np.argmax(self.cumulative_rewards)

    def expected_reward(self, cum):
        arm = self.choose_arm()
        self.occurrences[arm] += 1
        if random.uniform(0,1) < 0.5:
            self.cumulative_rewards[arm] += self.arms[arm]
        else:
            self.cumulative_rewards[arm] += (self.arms[arm] / (arm + 1))
        self.reward += self.cumulative_rewards[arm]/self.occurrences[arm]
        if cum == 't':
            return self.reward      
        else: 
            return self.cumulative_rewards[arm]/self.occurrences[arm]
            
    def run(self, cum):
        episodes = 1000
        bandit = Bandit()
        expected_reward = [0]*episodes
        for i in range(0, episodes):
            expected_reward[i] = bandit.expected_reward(cum)
        return expected_reward