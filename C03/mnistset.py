import sys
import os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image
import SigmoidFunction as sf
import softmax as sm


def image_show(IMG):
    pil_img = Image.fromarray(np.uint8(IMG))
    pil_img.show()


def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True,
                                                      flatten=True,
                                                      one_hot_label=False)
    return x_test, t_test


def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    
    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sf.sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sf.sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y


(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

IMG = x_train[0]
label = t_train[0]
print(label)

print(IMG.shape)
IMG = IMG.reshape(28, 28)
print(IMG.shape)

image_show(IMG)