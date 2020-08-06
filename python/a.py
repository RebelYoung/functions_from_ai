import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,6*np.pi,1001)
y=x*np.sin(x)
z=x*np.sin(1/(x+0.000001))
plt.plot(x,y,x,z)
plt.show()
print('---------------------------\n')
print('hello kitty!\n')
