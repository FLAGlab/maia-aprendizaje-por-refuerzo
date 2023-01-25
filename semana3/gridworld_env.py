class Environment:
    def __init__(self, n):
        self.current_state = (0,0)
        self.board = [[True for x in range(0, n)] for y in range(0,n)]
        self.board[2][1] = False
        self.board[2][2] = False
        self.board[2][3] = False
        self.board[2][4] = False
        self.board[2][6] = False
        self.board[2][7] = False
        self.board[2][8] = False
        self.board[3][4] = False
        self.board[3][5] = False
        self.board[3][6] = False
        self.board[3][7] = False
        self.rewards = [[0]*n]*n
        self.rewards[5][5] = 1
        self.rewards[4][5] = -1
        self.rewards[5][7] = -1
        self.rewards[5][8] = -1
    
    def get_current_state(self):
        """
        Returns the current state of environment
        """
        return self.current_state

    def get_possible_actions(self, state):
        """
          Returns possible actions the agent
          can take in the given state. Can
          return the empty list if we are in
          a terminal state.
        """
        actions = ()
        if state[0] > 0:
          actions += ('up', )
        if state[0] < self.dimensions -1:
          actions += ('down', )
        if state[1] > 0:
          actions += ('left', )
        if state[1] < self.dimensions -1:
          actions += ('right', )
        return actions

    def do_action(self, action):
        """
          Performs the given action in the current
          environment state and updates the environment.

          Returns a (reward, nextState) pair
        """
        if action == 'north':
          self.current_state[0] -= 1
        elif action == 'south':
          self.current_state[0] += 1
        elif action == 'left':
          self.current_state[1] -= 1
        elif action == 'right':
          self.current_state[1] += 1
        reward = self.rewards[self.current_state[0]][self.current_state[1]]
        return (reward, self.current_state)
        
    def reset(self):
        """
          Resets the current state to the start state
        """
        self.current_state = (0,0)

    def is_terminal(self):
        """
          Has the environment entered a terminal
          state? This means there are no successors
        """
        state = self.get_current_state()
        reward = self.rewards[state[0]][state[1]]
        return reward == 1