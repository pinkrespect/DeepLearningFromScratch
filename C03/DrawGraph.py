import matplotlib.pylab as plt
import numpy as np

def stepFunction(x):
    return np.array(x > 0, dtype=np.int)

x = np.arange(-5.0, 5.0, 0.1)
#-5.0 ~ 5.0 사이의 0.1 간격의 numpy Array 생성

y = stepFunction(x)
#배열의 원소 각각을 인수로 하여 stepFunction 실행

plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
