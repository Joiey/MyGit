# array=[1,2,3,4,5]
# small=[n*2 for n in array if n<3]
# print(small)
# d = {'a': 61, 'b': 62, 'c': 63, 'd': 64, 'e': 65}
# for i in d.values():
# print(d.items())
import numpy as np
import matplotlib.pyplot as plt

a=np.loadtxt('IOTA-STD.txt')
print(a.shape)
angle=a[:,0]
intensity=a[:,1]

plt.plot(angle,intensity,'k')

plt.xlabel(r'$2\theta$')
plt.ylabel('Intensity')

plt.show()
