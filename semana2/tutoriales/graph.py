import matplotlib.pyplot as plt
import numpy as np
from bandit import *

# x axis data
x = np.linspace(0, 1000, 1000)

# plot definition
fig, ax = plt.subplots()
plt.title("Bandit average reward")
plt.xlabel("Iterations")
plt.ylabel("Average reward")

# y axis data definition and graph definition 
def plot_bandits(bandits=1, cum = 'c'):
    for i in range(1, bandits+1):
        b = Bandit()
        y = np.array(b.run(cum))
        ax.plot(x, y, linewidth=1.0, label=f'bandit {i}')
    ax.legend()
    plt.show()

#example: plot with 3 bandits
#remove the coment for the case you want to observe
plot_bandits(3)
#plot_bandits(3, 't')