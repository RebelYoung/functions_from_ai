import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,np.pi,101)
y=x*np.sin(x)
z=x*np.sin(1/x)
plt.plot(x,y,x,z)
plt.show()
