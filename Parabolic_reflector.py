#
# Algorithm for cutting out a parabolic reflector
#
# Dmitriy Makhnovskiy, August 2024
#

import csv
import numpy as np

pi = np.pi  # pi-constant 3.1415....
c = 2.99792458e8  # speed of light in m/s

# Design parameters
units = 'mm'  # your length units: mm, cm, m (use small letters)
# For R and f use the same units: mm, cm, or m
R = 500.0  # dish radius
f = 500.0  # focus length
N = 10  # number of petals used for cutting out the parabolic reflector
M = 50  # number of points on the petal template for drawing its profile
eps = 1.0e-10  # calculation precision of the roots of the non-linear equation
# The minimum and maximum frequencies used for the communication, for example, those used for 4G LTE
f_min = 0.9  # minimum frequency in GHz
f_max = 2.6  # maximum frequency in GHz
k = 0.6  # reflector efficiency (0-1)

# Calculated parameters
f_min = f_min * 1.0e9  # frequency in Hz
f_max = f_max * 1.0e9  # frequency in Hz

lambda_max = c / f_min  # maximal wavelength
lambda_min = c / f_max  # minimal wavelength
if units == 'mm':
    radius = R / 1000.0
elif units == 'cm':
    radius = R / 100.0
else:
    radius = R

# Antenna gain range [Gain_min, Gain_max] dB for the given reflector efficiency k
Gain_min = 10.0 * np.log10(k * (2.0 * pi * radius / lambda_max)**2)
Gain_max = 10.0 * np.log10(k * (2.0 * pi * radius / lambda_min)**2)

a = 1.0 / (4.0 * f)  # parabola coefficient, z(x) = a*x^2
theta = 2.0 * pi / N  # angular width of the petal
value = np.sqrt(1.0 + 4.0 * a**2 * R**2)
L = R * value / 2.0 + np.log(2.0 * a * R + value) * f  # petal length

# Calculating the radius r from the length l along the parabola using the method of "dividing by half"
def rl(length):
    left = 0.0
    right = R
    r = (left + right) / 2.0  # initial middle point
    value = np.sqrt(1.0 + 4.0 * a ** 2 * r ** 2)
    value = r * value / 2.0 + np.log(2.0 * a * r + value) * f - length
    i = 1  # interation counter
    # Shifting the boundaries
    while np.abs(value) > eps and i < 100:
        if value < 0.0:
            left = r
        elif value > 0.0:
            right = r
        r = (left + right) / 2.0  # new middle point
        value = np.sqrt(1.0 + 4.0 * a ** 2 * r ** 2)
        value = r * value / 2.0 + np.log(2.0 * a * r + value) * f - length
        i = i + 1  # number of iterations
    return r

l = [0.0] * M  # points along the petal
l[M - 1] = L

r = [0.0] * M  # array of r corresponding to the array of l
r[M - 1] = R

D = [0.0] * M  # array of the tangent segments
D[M - 1] = R * np.sqrt(1.0 + 4.0 * a**2 * R**2)

eff = [0.0] * M  # array of the opening angles
eff[0] = theta / 2.0
eff[M - 1] = theta / (2.0 * np.sqrt(1.0 + 4.0 * a**2 * R**2))

q = [0.0] * M  # meridian displacements with respect to the l-points
q[M - 1] = D[M - 1] * (1.0 - np.cos(eff[M - 1]))

s = [0.0] * M # array of the meridian coordinates
s[M - 1] = l[M - 1] - q[M - 1]

w = [0.0 for i in range (M)]  # array of the widths corresponding to the array of s
w[M - 1] = D[M - 1] * np.sin(eff[M - 1])

for i in range(1, M-1):
    length = i * L / (M - 1)
    l[i] = length
    r[i] = rl(length)
    D[i] = r[i] * np.sqrt(1.0 + 4.0 * a ** 2 * r[i] ** 2)
    eff[i] = theta / (2.0 * np.sqrt(1.0 + 4.0 * a ** 2 * r[i] ** 2))
    q[i] = D[i] * (1.0 - np.cos(eff[i]))
    s[i] = l[i] - q[i]
    w[i] = D[i] * np.sin(eff[i])

# Saving the profile data to a CSV file
data = np.column_stack((l, r, D, eff, q, s, w))
header = ['l', 'r', 'D', 'eff', 'q', 's', 'w']

with open('Profile_data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(header)
    writer.writerows(data)

# Saving the design parameters to a txt file
Dish_radius = 'Dish radius = ' + str(R) + ' ' + units + '\n'
Dish_height = 'Dish height = ' + str(a * R**2) + ' ' + units + '\n'
Focus_length = 'Focus length of the reflector= ' + str(f) + ' ' + units + '\n'
Maximum_length = 'Petal length = ' + str(L) + ' ' + units + '\n'
N_number = 'Number of petals = ' + str(N) + '\n'
Petal_radius = 'Petal radius of curvature = ' + str(D[M - 1]) + ' ' + units +  '\n'
Frequency_min = 'Minimum frequency = ' + str(f_min / 1.0e9) + ' GHz' + '\n'
Frequency_max = 'Maximum frequency = ' + str(f_max / 1.0e9) + ' GHz' + '\n'
Wavelength_min = 'Minimum wavelength = ' + str(lambda_min) + ' m' + '\n'
Wavelength_max = 'Maximum wavelength = ' + str(lambda_max) + ' m' + '\n'
Reflector_eff = 'Reflector efficiency = ' + str(k) + '\n'
Antenna_Gain_min = 'Minimum antenna gain = ' + str(Gain_min) + ' dB' + '\n'
Antenna_Gain_max = 'Maximum antenna gain = ' + str(Gain_max) + ' dB' + '\n'

design_parameters = open('Design_parameters.txt', 'w')
design_parameters.write(Dish_radius)
design_parameters.write(Dish_height)
design_parameters.write(Focus_length)
design_parameters.write(Maximum_length)
design_parameters.write(N_number)
design_parameters.write(Petal_radius)
design_parameters.write(Frequency_min)
design_parameters.write(Frequency_max)
design_parameters.write(Wavelength_min)
design_parameters.write(Wavelength_max)
design_parameters.write(Reflector_eff)
design_parameters.write(Antenna_Gain_min)
design_parameters.write(Antenna_Gain_max)
design_parameters.close()