"""
Three Layers neural network implementation.

page 83-96 in the book
"""
import numpy as np
# We use numpy for deep learning because we wants use easy methmatical methods.


def sigmoid(number):
    """
    Sigmoid method returns you real number.

    This method needs number or array arguments,
    and returns real number in 0 to 1.
    """
    return 1 / (1 + np.exp(-number))


def identity_function(number):
    """
    Identity function method returns you argument as it is.

    It needs number or array arguments -in this documents, numpy array-,
    and returns arguments as it is.
    It costs resources to Run sigmoid, but inputs for last layer,
    We needs only show us result. We can't always use sigmoid function,
    but we should not forget to use activate function for depends on situation.
    """
    return number


X = np.array([1.0, 0.5])  # 2X3 Array
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
# W1 is one-dimensional array, It has 2 elements.
B1 = np.array([0.1, 0.2, 0.3])  # B1 means visualized bias.

print(W1.shape)  # (2, 3)
print(X.shape)  # (2,)
print(B1.shape)  # (3,)

A1 = np.dot(X, W1)+B1

Z1 = sigmoid(A1)

print(A1)  # [0.3, 0.7, 1.1]
print(Z1)  # [0.57444252, 0.66818777, 0.75026011]

W2 = np.array([[0.1, 0.4],
               [0.2, 0.5],
               [0.3, 0.6]])
B2 = np.array([0.1, 0.2])

print(Z1.shape)  # (3, )
print(W2.shape)  # (3, 2)
print(B2.shape)  # (2, )

A2 = np.dot(Z1, W2)+B2
Z2 = sigmoid(A2)

W3 = np.array([[0.1, 0.3],
               [0.2, 0.4]])
B3 = np.array([0.1, 0.2])

A3 = np.dot(Z2, W3)+B3
Y = identity_function(A3)  # Or Y = A3
