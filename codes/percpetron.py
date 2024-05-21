import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1+np.exp(-x))

x = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([0, 1, 1, 1]).reshape(-1, 1)

w = np.random.rand(2).reshape(-1, 1)
b = np.random.rand()

# Testing no trained perceptron
z = np.dot(x, w) + b
a = sigmoid(z)
a = np.round(a)
print("salida del perceptron sin entrenar")
print(a)

# Training
lr = 1.0
for epoch in range(1000):
    z = np.dot(x, w) + b
    a = sigmoid(z)
    dL_dz = -(y - a)*a*(1-a)
    w = w - lr * x.T@dL_dz
    b = b - lr * dL_dz.mean()

# Testing
z = np.dot(x, w)+b
a = sigmoid(z)
a = np.round(a)
print("\nSalida del perceptron Entrenado")
print(a)