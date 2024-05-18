import environment as Env
import agent_options as Q


board = [
        [' ', ' ', ' ', '+1'],
        [' ', '#', ' ', '-1'],
        ['S', ' ', ' ', ' '],
]

env = Env.Environment(board)
agent = Q.Agent(env, gamma=0.9, alpha=0.1, epsilon=0.9, o_epsilon=0.8, episodes=500)
agent.add_option((0,2), 10, ['down', 'down', 'left', 'left', 'up', 'up', 'right', 'right', 'right', 'end'])
agent.add_option((2,3), 5, ['left', 'up', 'up', 'right', 'end'])
agent.run()
actions, values = agent.actions_values()

print(values)
print(agent.qtable)
