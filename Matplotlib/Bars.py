import matplotlib.pyplot as plt
import numpy as np
x=np.array(["A","B","C","D"])
y=np.array([3,8,1,10])
plt.bar(x,y)
plt.show()

# to display the bars horizontally,
plt.barh(x,y)
plt.show()

# adjusting colour and the width value
plt.bar(x,y,color="red",width=0.1)
plt.show()