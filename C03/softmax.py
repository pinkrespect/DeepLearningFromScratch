"""Softmax function in page 92."""

import numpy as np


def softmax(number):
    max_number = np.max(number)
    exp_a = np.exp(number - max_number)  # Overflow
    sum_exp_a = np.sum(exp_a)
    result = exp_a / sum_exp_a

    return result
