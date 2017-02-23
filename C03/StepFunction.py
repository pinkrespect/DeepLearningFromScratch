import numpy as np

# Step Function 원형
# def stepFunction(x):
#     if x > 0:
#         return 1
#     else:
#         return 0
'''여기서 인수 x는 실수(부동 소수점)만 받음
   넘파이 배열은 인수로 들어갈 수 없다.    '''

# Step Function & Numpy
def StepFunction(x):
    y = x > 0
    return y.astype(np.int)

x = np.array([-1.0, 1.0, 2.0])
print(x)
# Numpy Array init

'''넘파이 배열에 부등호 연산을 수행하면
   배열의 원소 각각에 부등호 연산을 수행한 bool 배열 생성'''
y = x > 0
print(y)
# Boolean type return

y = y.astype(np.int) #넘파이 배열의 자료형 반환, 인수: 원하는 자료형
print(y)
# Array Type changes: Boolean > Integer

