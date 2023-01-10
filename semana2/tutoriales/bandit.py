import random

class Bandit:
    def __init__(self, arms = 10):
        self.arms = [0]*arms
        for i in range(0, arms):
            r = random.uniform(-3,3)
            self.arms[i] = r
        self.reward = 0

    def choose_arm(self, iteration):
        arm = random.randint(0,len(self.arms)-1)
        #print(f'\t Arm chosen: {arm + 1}')
        #print(f'\t Reward: {self.arms[arm]}')
        self.reward += self.arms[arm]
        #print(f'\t Average reward: {self.reward / iteration}')
        #print(f'\t Total reward: {self.reward}')
        return self.reward / (iteration + 1)
            
    def run(self):
        episodes = 1000
        bandit = Bandit()
        average_reward = [0]*episodes
        for i in range(0, episodes):
            #print(f'Iteration {i}')
            average_reward[i] = bandit.choose_arm(i)
        #print(cummulative_reward)
        return average_reward
        