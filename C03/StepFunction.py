'''
    오예
'''

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


def stepFunction(number):
    '''
        Step Function은 0이면 0, 1이면 1을 출력함
    '''
    boolean = number > 0
    return boolean.astype(np.int)


X = np.array([-1.0, 1.0, 2.0])
print(X)
# Numpy Array init

'''넘파이 배열에 부등호 연산을 수행하면
배열의 원소 각각에 부등호 연산을 수행한 bool 배열 생성'''

Y = X > 0
print(Y)
# Boolean type return

Y = Y.astype(np.int)
# 넘파이 배열의 자료형 반환, 인수: 원하는 자료형
print(Y)
# Array Type changes: Boolean > Integer
