import numpy as np

def Nand(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x)+b
    if tmp <= 0:
        return 0
    else:
        return 1

print(Nand(0, 0)) #1
print(Nand(0, 1)) #1
print(Nand(1, 0)) #1
print(Nand(1, 1)) #0