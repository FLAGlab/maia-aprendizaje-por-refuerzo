import random

class Bandit:
    def __init__(self, arms = 10):
        self.arms = [0]*arms
        self.cumulative_rewards = [0]*arms
        self.occurrences = [0]*arms
        for i in range(0, arms):
            r = random.uniform(-3,3)
            self.arms[i] = r
        self.reward = 0
        

    def expected_reward(self, cum):
        arm = random.randint(0,len(self.arms)-1)
        #print(f'\t Arm chosen: {arm + 1}')
        #print(f'\t Reward: {self.arms[arm]}')
        self.occurrences[arm] += 1
        if random.uniform(0,1) < 0.5:
            self.cumulative_rewards[arm] += self.arms[arm]
        else:
            self.cumulative_rewards[arm] += (self.arms[arm] / (arm + 1))
        self.reward += self.cumulative_rewards[arm]/self.occurrences[arm]
        #print(f'\t Average reward: {self.reward / iteration}')
        #print(f'\t Total reward: {self.reward}')
        if cum == 't':
            return self.reward      
        else: 
            return self.cumulative_rewards[arm]/self.occurrences[arm]
            
    def run(self, cum):
        episodes = 1000
        bandit = Bandit()
        expected_reward = [0]*episodes
        for i in range(0, episodes):
            #print(f'Iteration {i}')
            expected_reward[i] = bandit.expected_reward(cum)
        #print(cummulative_reward)
        return expected_reward
        