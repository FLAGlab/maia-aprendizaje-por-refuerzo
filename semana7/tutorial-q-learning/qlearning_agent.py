import numpy as np
import random
import copy


class Agent:
    def __init__(self, env, gamma=0.9, alpha=0.1, epsilon=0.9, episodes=1):
        #hyper parameters
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.environment = env
        self.qtable = self.__initdic__() #rewards table
        self.episodes = episodes
    
    def __initdic__(self):
        table = dict()
            
        # Initialize Q table with 0 for each state-action pair
        for state in self.environment.get_states():
            table[state] = np.zeros(len(self.environment.get_possible_actions(state)))
        return table

    def run(self):
        for counter in range(self.episodes):
            done = False
            while not done:
                current_state = copy.deepcopy(self.environment.state)
                if random.uniform(0,1) < self.epsilon:
                    action = self.random_action(current_state)
                else:
                    action = self.max_action(current_state)
                action_index = self.action_index(action)
                next_state, reward, done, info = self.step(action)
                
                if not done:
                    old_value = self.qtable[current_state][action_index]
                    next_max = np.max(self.qtable[next_state])
                    new_value = (1 - self.alpha)*old_value + self.alpha*(reward + self.gamma*next_max)
                    self.qtable[current_state][action_index] = new_value
                else:
                    self.qtable[current_state][action_index] = reward
            if counter % 30 == 0:
                self.epsilon -= self.epsilon/10
                # print(info)
                # print(f'{current_state}, {action}, {next_state}')
                # print("value", new_value)
            self.environment.reset()
            # print("----------------")
            print(counter)
        return self.qtable

    def max_action(self, current_state):
        action_index = np.argmax(self.qtable[current_state]) 
        actions = self.environment.actions
        return actions[action_index]


    def action_index(self, action):
        actions = self.environment.actions
        for i in range(len(actions)):
            if actions[i] == action:
                return i
        return -1

    def random_action(self, current_state):
        actions = self.environment.get_possible_actions(current_state)
        return random.sample(actions,len(actions))[0]

    def step(self, action):
        old_state = copy.deepcopy(self.environment.state)
        reward, new_state, done = self.environment.do_action(action)
        #print(old_state,"->",new_state, ":", action)
        # self.env.action(action)
        next_state = copy.deepcopy(new_state)
        info = f'Executed action: {action} at state {old_state} getting reward {reward}'
        return next_state, reward, done, info
    
    def actions_values(self):
        actions = {}
        self.environment.reset()
        values = np.zeros_like(self.environment.grid)
        for state in self.environment.get_states():
            action = np.argmax(self.qtable[state]) 
            actions[state] = self.environment.get_possible_actions(state)[action]
            values[state] = np.max(self.qtable[state])
        return actions, values
    
