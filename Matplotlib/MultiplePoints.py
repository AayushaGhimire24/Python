# Drawing a line from position(10,12) to (40,28) to (82,92) to (102,98)
import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([10,40,82,102])
ypoints=np.array([12,28,92,98])
plt.plot(xpoints,ypoints,ls=":",color='red')
plt.show()