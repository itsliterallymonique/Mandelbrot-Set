# -*- coding: utf-8 -*-
"""
MANDELBROT SET

By: it's literally monique
"""
# import libraries needed for program
import numpy as np
import matplotlib.pyplot as plt
  
#initialize list & set first values to 1
rows = 1000
cols = 1000
iterations = 150

def mandelbrot(c, z):
    global iterations
    count = 0
    for a in range(iterations):
        z = z**2 + c
        count += 1
        if(abs(z) > 4):
            break
    return count

def mandelbrot_set(x, y):
    m = np.zeros((len(x), len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            c = complex(x[i], y[j])
            z = complex(0, 0)
            count = mandelbrot(c, z)
            m[i, j] = count
    return m

x = np.linspace(-2, 1, rows)
y = np.linspace(-1, 1, cols)

m = mandelbrot_set(x, y)

# show the set (best colors: binary, hot, bone, magma)
plt.imshow(m.T, cmap = "magma")
plt.axis("off")
plt.show()