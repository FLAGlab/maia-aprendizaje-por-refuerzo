import matplotlib.pyplot as plt
import numpy as np
from bandit2 import *

# x axis data
x = np.linspace(0, 1000, 1000)

# plot definition
fig, ax = plt.subplots()
plt.title("Bandit average reward")
plt.xlabel("Iterations")
plt.ylabel("Average reward")

# y axis data definition and graph definition 
def plot_bandits(bandits=1, cum = 'c', epsilon = 0.01):
    for i in range(1, bandits+1):
        b = Bandit(10, epsilon)
        y = np.array(b.run(cum))
        ax.plot(x, y, linewidth=1.0, label=f'bandit {i}')
#    ax.legend()
#    plt.show()

#example: plot with 3 bandits
#remove the coment for the case you want to observe
#plot_bandits(3)
#plot_bandits(3, 't')
#plot_bandits(1, 't')
plot_bandits(1, 't', 0.1)
plot_bandits(1, 't', 0.01)
ax.legend()
plt.show()