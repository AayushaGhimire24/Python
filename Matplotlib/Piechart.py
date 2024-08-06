# import matplotlib.pyplot as plt
# import numpy as np
# y=np.array([35,25,25,15])
# plt.pie(y)
# plt.show()

# Adding labels
# import matplotlib.pyplot as plt
# import numpy as np
# y=np.array([35,25,25,15])
# mylabels=["Apple","Banana","Cherry","Dates"]
# plt.pie(y,labels=mylabels)
# plt.show()

# Start Angle
# plt.pie(y,labels=mylabels,startangle=90)

# Explode
import matplotlib.pyplot as plt
import numpy as np
y=np.array([35,25,25,15])
mylabels=["Apple","Banana","Cherry","Dates"]
myexplode=[0.2,0,0,2]
plt.pie(y,labels=mylabels,explode=myexplode)
plt.show()
# Shadow
plt.pie(y,labels=mylabels,explode=myexplode,shadow=True)
plt.show()
