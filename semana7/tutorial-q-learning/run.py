import environment as Env
import qlearning_agent as Q


board = [['S', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', '#', '#', '#', '#', ' ', '#', '#', '#', ' '],
        [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', '#', '-1' , ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', '#', '+1' , ' ', '-1', ' ', ' '],
        [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', '#', '-1' , ' ' , ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

env = Env.Environment(board)
agent = Q.Agent(env, gamma=0.9, alpha=0.1, epsilon=0.9, episodes=500)
agent.run()
actions, values = agent.actions_values()
agent.save_qtable()
print(values)
print(agent.qtable)
