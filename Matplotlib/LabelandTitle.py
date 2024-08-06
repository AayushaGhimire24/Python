import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([10,40,82,102])
ypoints=np.array([12,28,92,98])
plt.plot(xpoints,ypoints)
# Specifying font
font1={'family':'serif','color':'blue','size':20}
font2={'family':'serif','color':'darkred','size':15}
plt.title('Title Text',fontdict=font1)
plt.xlabel('Label for X-Axis',fontdict=font2)
plt.ylabel('Label for y-axis',fontdict=font2)
plt.show()