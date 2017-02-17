import numpy as np

# Step Function 원형
# def stepFunction(x):
#     if x > 0:
#         return 1
#     else:
#         return 0

# Step Function & Numpy
def StepFunction(x):
    y = x > 0
    return y.astype(np.int)

x = np.array([-1.0, 1.0, 2.0])
print(x)
# Numpy Array init

y = x > 0
print(y)
# Boolean type return

y = y.astype(np.int)
print(y)
# Array Type changes: Boolean > Integer

