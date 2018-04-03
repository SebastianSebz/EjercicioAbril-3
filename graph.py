import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('datos.txt')

plt.figure()
x = np.linspace(0,160, 160)

plt.plot(x, data[:,0])
plt.plot(x, data[:,1])

plt.savefig('DataAlbum.pdf')
plt.show()
