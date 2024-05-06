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
env = Env.Gridworld(board)
agent = Q.Agent(env, gamma=0.9, alpha=0.1, epsilon=0.9, episodes=1000)
agent.run()
actions, values = agent.actions_values()
env.plot_action(actions, values)
print(values)