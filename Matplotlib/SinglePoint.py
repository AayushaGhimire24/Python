# using plot() to draw a line
import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([0,45])
ypoints=np.array([5,55])
# plt.plot(xpoints,ypoints)
# plt.show()


# to plot only the markers, you can use shortcur string notation parameter 'o', which means 'rings'. Or'*'
# plt.plot(xpoints,ypoints,'o')
# plt.show()

# to plot line with markers
plt.plot(xpoints,ypoints,marker='o')
plt.show()