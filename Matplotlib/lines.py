import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
plt.plot(ypoints, ls = ':' , color = 'r', linewidth=10)
plt.plot(y2)
plt.show()