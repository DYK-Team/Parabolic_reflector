#
# Algorithm for cutting out petals for a sphere
#
# Dmitriy Makhnovskiy, September 2024
#

import csv
import numpy as np

pi = np.pi  # pi-constant 3.1415....

# Design parameters
R = 1000.0  # dish radius; your units (mm, cm, or m)
N = 10  # number of petals used for cutting out the sphere
M = 50  # number of points on the petal template for drawing its profile

# Calculated parameters
theta = 2.0 * pi / N  # angular width of the petal
L = pi * R / 2.0  # petal length

l = [0.0] * M  # points along the petal
l[M - 1] = L
r = [0.0] * M  # array of r corresponding to the array of l
r[M - 1] = R
eff = [0.0] * M  # array of the opening angles
eff[M - 1] = 0.0
q = [0.0] * M  # meridian displacements with respect to the l-points
q[M - 1] = 0.0
s = [0.0] * M  # array of the meridian coordinates
s[M - 1] = L
w = [0.0] * M  # array of the widths corresponding to the array of s
w[M - 1] = theta * R / 2.0

for i in range(0, M-1):
    length = i * L / (M - 1)
    l[i] = length
    r[i] = R * np.sin(length / R)
    sqroot = np.sqrt(R ** 2 - r[i] ** 2)
    eff[i] = theta * sqroot / (2.0 * R)
    q[i] = r[i] * (1.0 - np.cos(eff[i]) - eff[i] ** 2 / 2.0) / sqroot + r[i] * theta ** 2 * sqroot / (8.0 * R)
    s[i] = l[i] - q[i]
    w[i] = r[i] * (np.sin(eff[i]) - eff[i]) / sqroot + r[i] * theta / 2.0

# Saving the profile data to a CSV file
data = np.column_stack((l, r, eff, q, s, w))
header = ['l', 'r', 'eff', 'q', 's', 'w']

with open('Spherical_profile_data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(header)
    writer.writerows(data)