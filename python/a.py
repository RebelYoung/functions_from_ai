import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,np.pi,101)
y=x*np.sin(x)
plt.plot(x,y)
plt.show()
