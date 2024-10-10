#
# Algorithm for cutting the petals for a sphere
# Optimised code: it does not use arrays saved in the memory and writes values directly to the csv output file
#
# Dmitriy Makhnovskiy, October 2024
#

import csv
import numpy as np

pi = np.pi  # pi-constant 3.1415....

# Design parameters
R = 1000.0  # dish radius; your units (mm, cm, or m)
N = 10  # number of petals used for the sphere
M = 50  # number of points on the petal template for drawing its profile

# Calculated parameters
theta = 2.0 * pi / N  # angular width of the petal
L = pi * R / 2.0  # petal length

with open('Spherical_profile_data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    header = ['l', 'r', 'eff', 'q', 's', 'w']
    writer.writerow(header)

    for i in range(0, M-1):
        l = i * L / (M - 1)
        r = R * np.sin(l / R)
        sqroot = np.sqrt(R ** 2 - r ** 2)
        eff = theta * sqroot / (2.0 * R)
        q = r * (1.0 - np.cos(eff) - eff ** 2 / 2.0) / sqroot + r * theta ** 2 * sqroot / (8.0 * R)
        s = l - q
        w = r * (np.sin(eff) - eff) / sqroot + r * theta / 2.0
        writer.writerow([l, r, eff, q, s, w])

    writer.writerow([L, R, 0.0, 0.0, L, theta * R / 2.0])  # last row