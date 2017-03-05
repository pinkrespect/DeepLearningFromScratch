"""
Summary of implements for Chapter 3.

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


def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5],
                              [0.2, 0.4, 0.6]])
    network['B1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4],
                              [0.2, 0.5],
                              [0.3, 0.6]])
    network['B2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3],
                              [0.2, 0.4]])
    network['B3'] = np.array([0.1, 0.2])

    return network


def forward(network, bias):
    w_1, w_2, w_3 = network['W1'], network['W2'], network['W3']
    b_1, b_2, b_3 = network['B1'], network['B2'], network['B3']

    a_1 = np.dot(bias, w_1)+b_1
    z_1 = sigmoid(a_1)
    a_2 = np.dot(z_1, w_2)+b_2
    z_2 = sigmoid(a_2)
    a_3 = np.dot(z_2, w_3)+b_3
    result = identity_function(a_3)

    return result


NETWORK = init_network()
X = np.array([1.0, 0.5])
Y = forward(NETWORK, X)
print(Y)  # [ 0.31682708  0.69627909]
