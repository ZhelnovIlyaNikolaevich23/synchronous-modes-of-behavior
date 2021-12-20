import matplotlib.pyplot as plt
import pylab

delta, mu, b, c, d = 0.1, 0.1, 0.1, 0.1, 0.1

def f1(x1, y1, z1, x2, y2, z2):
    return x1 - x1 ** 3 / 3 - y1 + z1 + 0.5 * (x2 - x1)

def g1(x1, y1, z1, x2, y2, z2):
    return delta * (x1 - b * y1)

def h1(x1, y1, z1, x2, y2, z2):
    return mu * (c - x1 - d * z1)

def f2(x1, y1, z1, x2, y2, z2):
    return x2 - x2 ** 3 / 3 - y2 + z2 + 0.5 * (x1 - x2)

def g2(x1, y1, z1, x2, y2, z2):
    return delta * (x2 - b * y2)

def h2(x1, y1, z1, x2, y2, z2):
    return mu * (c - x2 - d * z2)

H = 0.1
N = 1000
X1, Y1, Z1, X2, Y2, Z2 = [0.0], [0.0], [0.0], [0.0], [0.0], [0.0]
for i in range(N):
    X1.append(X1[i] + H * float(f1(X1[i], Y1[i], Z1[i], X2[i], Y2[i], Z2[i])))
    Y1.append(Y1[i] + H * float(g1(X1[i], Y1[i], Z1[i], X2[i], Y2[i], Z2[i])))
    Z1.append(Z1[i] + H * float(h1(X1[i], Y1[i], Z1[i], X2[i], Y2[i], Z2[i])))
    X2.append(X2[i] + H * float(f2(X1[i], Y1[i], Z1[i], X2[i], Y2[i], Z2[i])))
    Y2.append(Y2[i] + H * float(g2(X1[i], Y1[i], Z1[i], X2[i], Y2[i], Z2[i])))
    Z2.append(Z2[i] + H * float(h2(X1[i], Y1[i], Z1[i], X2[i], Y2[i], Z2[i])))
T = []
for i in range(N + 1):
    T.append(i)
pylab.subplot(3, 1, 1)
pylab.plot(T, X1)
pylab.ylabel('v1')
pylab.subplot(3, 1, 2)
pylab.plot(T, X2)
pylab.ylabel('v2')
pylab.subplot(3, 1, 3)
pylab.plot(T, X1)
pylab.plot(T, X2)
pylab.xlabel('t')
pylab.ylabel('v1, v2')
pylab.show()
def h2(x1, y1, z1, x2, y2, z2):
    return mu * (c - x2 - d * z2)

H = 0.1
N = 1000
X1, Y1, Z1, X2, Y2, Z2 = [0.0], [0.0], [0.0], [0.0], [0.0], [0.0]
for i in range(N):
    X1.append(X1[i] + H * float(f1(X1[i], Y1[i], Z1[i], X2[i], Y2[i], Z2[i])))
    Y1.append(Y1[i] + H * float(g1(X1[i], Y1[i], Z1[i], X2[i], Y2[i], Z2[i])))
    Z1.append(Z1[i] + H * float(h1(X1[i], Y1[i], Z1[i], X2[i], Y2[i], Z2[i])))
    X2.append(X2[i] + H * float(f2(X1[i], Y1[i], Z1[i], X2[i], Y2[i], Z2[i])))
    Y2.append(Y2[i] + H * float(g2(X1[i], Y1[i], Z1[i], X2[i], Y2[i], Z2[i])))
    Z2.append(Z2[i] + H * float(h2(X1[i], Y1[i], Z1[i], X2[i], Y2[i], Z2[i])))
T = []
for i in range(N + 1):
    T.append(i)
pylab.subplot(3, 1, 1)
pylab.plot(T, X1)
pylab.ylabel('v1')
pylab.subplot(3, 1, 2)
pylab.plot(T, X2)
pylab.ylabel('v2')
pylab.subplot(3, 1, 3)
pylab.plot(T, X1)
pylab.plot(T, X2)
pylab.xlabel('t')
pylab.ylabel('v1, v2')
pylab.show()