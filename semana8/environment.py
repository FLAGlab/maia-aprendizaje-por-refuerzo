import matplotlib.pyplot as plt
import matplotlib.patches as patches

#Environment class defining gridworld
class Environment: 
    def __init__(self, board):
        self.nrows, self.ncols = len(board),len(board[0])
        self.states = [[0 for _ in range(self.ncols)] for _ in range(self.nrows)]
        self.initial_state = None
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'S':
                    self.initial_state = (i,j)
                elif board[i][j] == "#":
                    self.states[i][j] = None
                elif board[i][j] != ' ':
                    self.states[i][j] = int(board[i][j])
        self.current_state = self.initial_state
        self.actions = ['left', 'right', 'up', 'down']
        
    def get_states(self):
        return [(i, j) for i in range(self.nrows) for j in range(self.ncols)]

    def get_current_state(self):
        return self.current_state

    def get_possible_actions(self, state):
        if self.is_terminal(state):
            return ['end']
        return self.actions            
    
    def get_next_state(self, state, action):
        i, j = state
        reward = 0
        done = False
        if self.is_terminal(state):
            reward = self.states[i][j]
            done = True
        elif action == 'left' and j > 0 and self.states[i][j-1] != None:
            j -= 1  #(i,j) = noise(state, action)
        elif action == 'right' and j < self.ncols - 1 and self.states[i][j+1] != None:
            j += 1
        elif action == 'down' and i < self.nrows -1 and self.states[i+1][j] != None:
            i += 1
        elif action == 'up' and i > 0 and self.states[i-1][j] != None:
            i -= 1
        self.current_state = (i, j)
        return reward, self.current_state, done

    def do_action(self, action):
        return self.get_next_state(self.current_state, action)

    def reset(self):
        self.current_state = self.initial_state

    def is_terminal(self, state):
        return self.states[state[0]][state[1]] != 0 and self.states[state[0]][state[1]] != None
    
    def plot(self):
        fig1 = plt.figure(figsize=(10, 10))
        ax1 = fig1.add_subplot(111, aspect='equal')
        
        # Lineas
        for i in range(0, len(self.states)+1):
            ax1.axhline(i , linewidth=2, color="#2D2D33")
        for i in range(len(self.states[0])+1):
            ax1.axvline(i , linewidth=2, color="#2D2D33")
        
        # Amarillo - inicio
        (i,j)  = self.initial_state
        ax1.add_patch(patches.Rectangle((j, self.nrows - i -1), 1, 1, facecolor = "#F6D924"))
        for j in range(len(self.states[0])):
            for i in range(len(self.states)):
                if self.states[i][j] == 1: # verde
                    ax1.add_patch(patches.Rectangle((j,self.nrows - i -1), 1, 1, facecolor = "#68FF33"))
                if self.states[i][j] == None: # gris
                    ax1.add_patch(patches.Rectangle((j,self.nrows - i -1), 1, 1, facecolor = "#6c7780"))
                if self.states[i][j] == -1: # rojo
                    ax1.add_patch(patches.Rectangle((j,self.nrows - i -1), 1, 1, facecolor = "#cc0000"))
        #plt.scatter(self.ncols - self.state[1] - 1 + 0.5, self.nrows - self.state[0] - 1 +0.5, s = 100, color = "black", marker = "o", facecolor = "blue", edgecolors = "blue", zorder = 10)
        for i in range(len(self.states)):
            for j in range(len(self.states[0])):
                if self.states[i][j] == None:
                    ax1.text(self.ncols-j-1, self.nrows-i-1, "", ha='center', va='center')
                else:
                    ax1.text(j+0.5, self.nrows-i-1+0.5, str(round(self.states[i][j],2)), ha='center', va='center')
        plt.axis("off")
        plt.show()

    def get_action_test(self, action):
        if action=='left':
            return '<'
        if action=='right':
            return '>'
        if action=='up':
            return '^'
        if action=='down':
            return 'v'
        if action=='exit':
            return 'x'
        
    def plot_action(self, actions, values):
        fig1 = plt.figure(figsize=(5, 5))
        ax1 = fig1.add_subplot(111, aspect='equal')
        
        # Lineas
        for i in range(0, len(self.states)+1):
            ax1.axhline(i , linewidth=2, color="#2D2D33")
        for i in range(len(self.states[0])+1):
            ax1.axvline(i , linewidth=2, color="#2D2D33")
        
        # Amarillo - inicio
        (i,j)  = self.initial_state
        ax1.add_patch(patches.Rectangle((j, self.nrows - i -1), 1, 1, facecolor = "#F6D924"))
        for j in range(len(self.states[0])):
            for i in range(len(self.states)):
                if self.states[i][j] == 1: # verde
                    ax1.add_patch(patches.Rectangle((j,self.nrows - i -1), 1, 1, facecolor = "#68FF33"))
                if self.states[i][j] == None: # gris
                    ax1.add_patch(patches.Rectangle((j,self.nrows - i -1), 1, 1, facecolor = "#6c7780"))
                if self.states[i][j] == -1: # rojo
                    ax1.add_patch(patches.Rectangle((j,self.nrows - i -1), 1, 1, facecolor = "#cc0000"))
        self.reset()
       # plt.scatter(self.state[0] + 0.5, self.state[1] +0.5, s = 100, color = "black", marker = "o", facecolor = "blue", edgecolors = "blue", zorder = 10) 
        for i in range(len(self.states)):
            for j in range(len(self.states[0])):
                if self.states[i][j] == None:
                    ax1.text(i+0.5, j+0.5, "", ha='center', va='center')
                else:
                    ax1.text(j+0.5, self.nrows-i-1+0.5, str(round(values[i][j],2)), ha='center', va='center')
                    #ax1.text(i+0.5, j+0.75, round(values[i, j],2), ha='center', va='center')
                    text2=self.get_action_test(actions[(i,j)])
                    ax1.text(j+0.5, self.nrows-i-1+0.25, text2, ha='center', va='center')
        plt.axis("off")
        plt.show() 