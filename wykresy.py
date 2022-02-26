import matplotlib.pyplot as plt
import numpy as np
#x = np.arange(0.0,6.0,0.01)
x = range (1,5)
plt.plot([xi*1.5 for xi in x])
plt.plot([xi*5 for xi in x])
plt.plot([xi/3 for xi in x])
plt.show()
