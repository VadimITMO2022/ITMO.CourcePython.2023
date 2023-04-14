import numpy
import matplotlib.pyplot
import matplotlib.pyplot as plt
import math

f = open('time.txt', 'r')

# reading from file 'time.txt'

l_max = int(f.readline())
ttime = numpy.empty(l_max, dtype="int")
l1 = numpy.empty(l_max, dtype="int")

print(str(l_max))
ll = 0
while ll < l_max:
    l1[ll] = int(f.readline())
    ttime[ll] = int(f.readline())
    print(str(l1[ll]) + "   " +str(ttime[ll]))
    ll = ll + 1

# calculation average value
av = 0.
ll = 0
while ll < l_max:
    av = av + float(ttime[ll])
    print("l=" + str(ll) + "    " + "t=" + str(ttime[ll]))
    ll = ll + 1

av = av / float(l_max)

# calculation mean deviation

s = 0
l1 = 0
while l1 < l_max:
    s = s + math.pow(av - ttime[l1], 2)
    l1 = l1 + 1

Dev = math.sqrt(s / l_max)

# calculation median value

if int(l_max) % 2 != 0:
    l1 = int((l_max - 1) / 2)
    print("l1=" + str(l1))
    med = ttime[l1]

else:
    l2 = int(l_max / 2-1)
    l3 = int(l_max / 2)
    print("l2=" + str(l2) + "    l3=" + str(l3))
    med = (ttime[l2] + ttime[l3]) / 2.

dx=1

print("shortest time= " + str(ttime[0]/dx) + "\n" + "longest time= " + str(ttime[l_max - 1]/dx))
print("average value= " + str(av/dx))
print("median value= " + str(med/dx))
print("mean deviation= " + str(Dev/dx))




