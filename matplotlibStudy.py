
import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
import matplotlib as mpl
# plt.plot([1,2,3],[5,7,2])
# plt.show()
# A=np.array([[1,3,5],[2,5,1],[2,3,8]])
# print(linalg.inv(A))
#plt.style.use('ggplot')
x=np.linspace(0,2,10)

plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='square')
plt.plot(x, x**3, label='cubic')

plt.title('Simple plot')

plt.legend()

plt.show()

