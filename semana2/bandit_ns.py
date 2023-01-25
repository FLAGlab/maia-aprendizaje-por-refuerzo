import random
import math
import numpy as np

class Bandit:
    def __init__(self, start=1, arms=10, epsilon=0.01, alpha=0.1):
        self.arms = [start*random.randint(1,arms) for x in range(0,arms)]
        self.epsilon = epsilon
        self.alpha = 0.1
        self.cumulative_rewards = [0]*arms
        for i in range(0, arms):
            r = random.uniform(-3,3)
            self.arms[i] = r
        self.reward = 0
        
    def choose_arm(self):
        if random.uniform(0,1) < self.epsilon:
            return random.randint(0, len(self.arms)-1)
        else:
            return np.argmax(self.cumulative_rewards)

    def expected_reward(self, step):
        arm = self.choose_arm()
        #define how the reward is calculated
        # observation, reward, done, info = env.step(action)
        sum_part = 0
        for i in range(1, step):
            reward = self.arms[arm] * math.sin(math.radians(arm*i % 360))
            sum_part = sum_part + ((1-self.alpha)**(step - i))*reward*self.alpha
        
        self.cumulative_rewards[arm] = ((1-self.alpha)**step) * self.arms[arm] + sum_part
        return self.cumulative_rewards[arm]
            
def run(cum):
    episodes = 5
    step = 50
    bandit = Bandit(1)
    expected_reward = [0]*episodes
    for i in range(0, episodes):
        expected_reward[i] = bandit.expected_reward(step)
    print(expected_reward)
    return expected_reward


run(1)