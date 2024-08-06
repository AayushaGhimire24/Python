# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([5,6,8,17])
# y=np.array([99,86,87,88])
# plt.scatter(x,y)
# plt.show()

# you cannot use the color argument for this, only the cargument
# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([5,6,8,17])
# y=np.array([99,86,87,88])
# colors=np.array([0,10,20,30])
# colors=np.array(["red","green","blue","yellow"])
# plt.scatter(x,y,c=colors,cmap="virdis")
# plt.colorbar()
# plt.show()

# Changing size of dots:
# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([5,6,8,17])
# y=np.array([99,86,87,88])
# sizes=np.array([20,50,100,200])
# plt.scatter(x,y,s=sizes)
# plt.show()

# Adjusting the transparency of dot(Alpha)
import matplotlib.pyplot as plt
import numpy as np
x=np.array([5,6,8,17])
y=np.array([99,86,87,88])
sizes=np.array([20,50,100,200])
plt.scatter(x,y,s=sizes,alpha=0.5)
plt.show()