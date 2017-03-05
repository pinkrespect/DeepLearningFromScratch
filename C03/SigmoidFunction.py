import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-1))

x = np.array([-1.0, 1.0, 2.0])
print(sigmoid(x))
'''브로드 캐스트 기능: 넘파이 배열과 스칼라값의 연산을
                       넘파이 배열의 원소 각각과 스칼라값의 연산으로 수행'''

t = np.array([1.0, 2.0, 3.0])
print(1.0 + t)
print(1.0 / t)
'''sigmoid function도 넘파이 배열의 각 원소에 연산을 수행한 결과를 반환'''


# ValueError: x and y must have same first dimension, but have shapes (100,) and (1,)
z = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(z)
plt.plot(z, y)
plt.ylim(-0.1, 1.1)
plt.show()
