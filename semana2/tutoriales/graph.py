import matplotlib.pyplot as plt
import numpy as np
from bandit import *

# get data
x = np.linspace(0, 1000, 1000)

# plot
fig, ax = plt.subplots()
plt.title("Bandit average reward")
plt.xlabel("Iterations")
plt.ylabel("Average reward")
#ax.set(xlim=(0, 1000), xticks=np.arange(1, 1000), 
#       ylim=(0, 3), yticks=np.arange(0, 3))

def plot_bandits(bandits=1):
    for i in range(1, bandits+1):
        b = Bandit()
        y = np.array(b.run())
        ax.plot(x, y, linewidth=2.0, label=f'bandit {i}')
    ax.legend()
    plt.show()

plot_bandits(3)