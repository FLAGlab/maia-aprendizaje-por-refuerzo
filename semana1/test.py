import random
import numpy as np

class Learner:
    def __init__(self, agent, env, alpha=0.1, gamma=0.6, epsilon=0.5):
        #hyper parameters
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.environment = env
        self.agent = agent          #actual agent
        self.qtable = self.__initdic__()
    
    def __initdic__(self):
        table = dict()
        for i in range(0, self.environment.end()):
            table[i] = np.zeros(len(self.agent.actions))
        return table

    def run(self):
        done = False
        while not done:
            current_state = self.agent.state
            if random.uniform(0,1) < self.epsilon:
                action = self.randomAction()
            else:
                action = np.argmax(self.qtable[current_state]) 
            next_state, reward, done, info = self.step(action)
            old_value = self.qtable[current_state][action]
            next_max = np.max(self.qtable[next_state])
            new_value = (1 - self.alpha)*old_value + self.alpha*(reward + self.gamma*next_max)
            self.qtable[current_state][action] = new_value

            #print(info)
            #print(f'{current_state}, {action}, {next_state}')

    def randomAction(self):
        return random.randint(0,len(self.agent.actions)-1)

    def step(self, action):
        old_state = self.agent.state
        reward, done = self.getReward(old_state, self.agent.getAction(action))
        self.agent.action(action)
        next_state = self.agent.state
        info = f'Executed action: {self.agent.getAction(action)} at state {old_state}'
        return next_state, reward, done, info

    def getReward(self, state, action):
        if state == self.environment.end() - 2 and action == 'right':
            return 10, True
        else:
            return 0, False

class Environment:
    def __init__(self):
        self.board = [False for x in range(0, 5)]
        self.board[4] = True
    
    def reset(self):
        self.steps = 10
    
    def start(self):
        return 0
    
    def end(self): 
        return len(self.board)    

class Agent:
    def __init__(self, rb):
        self.state = 0
        self.actions = [0,1]
        self.rightBound = rb - 1

    def reset(self):
        self.state = 0
        
    def forward(self):
        self.state = min(self.state + 1, self.rightBound)
        
    def back(self):
        self.state = max(self.state - 1, 0)
        
    def action(self, action : int):
        if action:
            self.forward()
        else:
            self.back()
    
    def getAction(self, action : int):
        if action:
            return 'right'
        else:
            return 'left'

def main():
    episodes = 10
    e = Environment()
    a = Agent(e.end())
    l = Learner(a, e)
    for i in range(0, episodes):
        print(f"Episode: {i+1}")
        l.run()
        a.reset()
        print(l.qtable)
        
main()