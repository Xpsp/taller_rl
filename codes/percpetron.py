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

y = np.array([1, 0, 1, 1])

w = np.random.rand(2)
b = np.random.rand()

line = np.linspace(-1, 2, 100)
plt.plot(line, -(w[0]*line+b)/w[1])
plt.scatter(x[:, 0], x[:, 1], c=y)
plt.ylim(-1, 2)
plt.xlim(-1, 2)
plt.title("Perceptron sin entrenar")
plt.show()


# Training
lr = 1.0
for epoch in range(1000):
    z = np.dot(x, w) + b
    a = sigmoid(z)
    dL_dz = (a-y)*a*(1-a)
    w = w - lr * x.T@dL_dz
    b = b - lr * dL_dz.mean()

# Testing
z = np.dot(x, w)+b
a = sigmoid(z)
a = np.round(a)
print("\nSalida del perceptron Entrenado")
print(a)

plt.plot(line, -(w[0]*line+b)/w[1])
plt.scatter(x[:, 0], x[:, 1], c=y)
plt.ylim(-1, 2)
plt.xlim(-1, 2)
plt.show()