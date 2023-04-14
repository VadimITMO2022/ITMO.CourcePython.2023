import numpy as np
import time
import math

l_max = 50
# creation of empty array ttime
ttime = np.empty(l_max, dtype="int")

# reading alpha,beta,op(A),op(B),C from 'input.txt'
f = open('input.txt')


alpha = int(f.readline())
beta = int(f.readline())
m = int(f.readline())
k = int(f.readline())
n = int(f.readline())

Array_op_A = np.empty((m, k), dtype="int")
Array_op_B = np.empty((k, n), dtype="int")
Array_C = np.empty((m, n), dtype="int")
Array_D = np.empty((m, n), dtype="int")

i = 0
while i < m:
     j = 0
     while j < k:
         Array_op_A[i][j] = int(f.readline())
#         print(str(Array_op_A[i][j]))
         j = j + 1
     i = i + 1


i = 0
while i < k:
     j = 0
     while j < n:
         Array_op_B[i][j] = int(f.readline())
#        print("B"+str(i)+str(j)+"   "+str(Array_op_B[i][j]))
         j = j + 1
     i = i + 1

i = 0
while i < m:
    j = 0
    while j < n:
        Array_C[i][j] = int(f.readline())
#       print("C" + str(i) + str(j) + "   " + str(Array_C[i][j]))
        j = j + 1
    i = i + 1

f.close()


l = 0
while l < l_max:

#    t0 = time.perf_counter_ns()
#    t0 = time.time()
    t0 = time.time_ns()

# calculation matrix D

    i = 0
    while i < m:
        j = 0
        while j < n:
             Array_D[i][j] = 0
             i1 = 0
             while i1 < k:
                Array_D[i][j] = Array_D[i][j] + Array_op_A[i][i1] * Array_op_B[i1][j]
                i1 = i1 + 1
#            print("D" + str(i) + str(j) + "   " + str(Array_D[i][j]))
             Array_D[i][j] = alpha * Array_D[i][j] + beta * Array_C[i][j]
             j = j + 1
        i = i + 1

        #   t1 = time.time()
    t1 = time.time_ns()
        #  t1 = time.perf_counter_ns()
    ttime[l] = (t1 - t0)/1000

    print("l=" + str(l) + "  time=" + str(ttime[l]))

#    i = 0
#    while i < m:
#        j = 0
#        while j < n:
#            print(" " + "(" + str(i) + str(j) + ") " + str(Array_D[i][j]) + " ")
#           j = j + 1
#        i = i + 1
#        print()

    l = l + 1

# sorting array ttime
ttime.sort()
print()

# writing sorted array ttime in the file 'time.txt'
file_time = open('time.txt', 'w')
file_time.write(str(l_max) + "\n")
ll = 0
while ll < l_max:
    file_time.write(str(ll) + "\n")
    file_time.write(str(ttime[ll]) + "\n")
    ll = ll + 1

# calculation average value
av = 0.
ll = 0
while ll < l_max:
    av = av + float(ttime[ll])
    print("l=" + str(ll) + "    " + "t=" + str(ttime[ll]) +  "    " + str(av))
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


print("shortest time= " + str(ttime[0]) + "\n" + "longest time= " + str(ttime[l_max - 1]))
print("average value= " + str(av))
print("median value= " + str(med))
print("mean deviation= " + str(Dev))