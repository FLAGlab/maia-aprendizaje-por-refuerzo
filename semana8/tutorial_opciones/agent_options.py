import numpy as np
import random
import copy
import ast

class Agent:
    def __init__(self, env, gamma=0.9, alpha=0.1, epsilon=0.9, o_epsilon=0.1, episodes=1):
        #hyper parameters
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.environment = env
        self.qtable = self.__initdic__() #rewards table
        self.episodes = episodes
        # Option information
        self.option_probability = o_epsilon
        self.options = []  #[(o,n,a1a2a3…an), …(o,m,a1a2….am)]
        
    def __initdic__(self):
        table = dict()
            
        # Initialize Q table with 0 for each state-action pair
        for state in self.environment.get_states():
            table[state] = {a:0 for a in self.environment.get_possible_actions(state)}
        return table


    def add_option(self, state, length, action_list):
        self.options.append((state,length, action_list))
        self.qtable[state][str(action_list)] = 0

    def get_option(self, state):
        for s,n,al in self.options:
            if s == state:
                return s,n,al
            
    def run(self):
        for counter in range(self.episodes):
            done = False
            while not done:
                current_state = copy.deepcopy(self.environment.get_current_state())
                option_state =  set([state for state, _, _ in self.options])
                if current_state in option_state and random.uniform(0,1) < self.option_probability:
                    state, n, al = self.get_option(current_state)
                    cum_reward = 0
                    for i in range(n):
                        next_state, reward, done, info = self.step(al[i])
                        cum_reward = self.gamma*cum_reward + reward
                    old_value = self.qtable[current_state][str(al)]
                    next_max = max(self.qtable[next_state].values())
                    new_value = (1 - self.alpha)*old_value + self.alpha*(cum_reward + self.gamma*next_max)
                    self.qtable[current_state][str(al)] = new_value
                else:    
                    if random.uniform(0,1) < self.epsilon:
                        action = self.random_action(current_state)
                    else:
                        action = self.max_action(current_state)
                    action_index = self.actions_index(current_state, action)
                    if action_index > len(self.environment.actions):
                        actions = ast.literal_eval(action)
                        reward = 0
                        for a in actions:
                            next_state, s_reward, done, info = self.step(a)
                            reward = self.gamma*reward + s_reward
                    else:
                        next_state, reward, done, info = self.step(action)
                    
                    if not done:
                        old_value = self.qtable[current_state][action]
                        next_max = max(self.qtable[next_state].values())
                        new_value = (1 - self.alpha)*old_value + self.alpha*(reward + self.gamma*next_max)
                        self.qtable[current_state][action] = new_value
                    else:
                        self.qtable[current_state][action] = reward
            if counter % 30 == 0:
                self.epsilon -= self.epsilon/10
            self.environment.reset()
        return self.qtable

    def max_action(self, current_state):
        action_index = np.argmax(self.qtable[current_state]) 
        actions = self.environment.actions
        return actions[action_index]

    def action_name(self, action_index):
        return self.environment.actions[action_index]
    
    def actions_index(self, state, action):
        state_actions = self.qtable[state].keys()
        for i, k  in enumerate(state_actions):
            if action == k:
                return i
        return -1

    def random_action(self, current_state):
        actions = self.qtable[current_state].keys()
        return random.sample(sorted(actions),len(actions))[0]

    def step(self, action):
        old_state = copy.deepcopy(self.environment.get_current_state())
        reward, new_state, done = self.environment.do_action(action)
        next_state = copy.deepcopy(new_state)
        info = f'Executed action: {action} at state {old_state} getting reward {reward}'
        return next_state, reward, done, info
    
    def actions_values(self):
        actions = {}
        self.environment.reset()
        values = np.zeros_like(self.environment.states)
        for state in self.environment.get_states():
            action = np.argmax(self.qtable[state]) 
            actions[state] = self.environment.get_possible_actions(state)[action]
            values[state] = np.max(self.qtable[state])
        return actions, values
    

