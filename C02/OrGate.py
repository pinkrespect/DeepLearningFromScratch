import numpy as np

def Or(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x)+b
    if tmp <= 0:
        return 0
    else:
        return 1

print(Or(0, 0)) #0
print(Or(0, 1)) #1
print(Or(1, 0)) #1
print(Or(1, 1)) #1