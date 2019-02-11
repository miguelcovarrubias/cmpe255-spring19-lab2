
from math import pi
from math import sqrt
from math import exp

def normal_pdf(x, mu=0, sigma=1):
    return (1 / sqrt(2 * pi * sigma * sigma)) * exp(-1 * ((x - mu) * (x - mu)) / (2 * sigma * sigma))

from matplotlib import pyplot as plt
xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '-', label='mu=0,sigma=2')
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], '-', label='mu=0,sigma=0.5')
plt.plot(xs, [normal_pdf(x, sigma=-1) for x in xs], '-', label='mu=0,sigma=-1')
plt.legend()
plt.show()

