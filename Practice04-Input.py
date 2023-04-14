import random
import numpy as np



# transa=0 матрица А не транспонирована; transa=1 матрица А транспонирована
# transb=0 матрица B не транспонирована; transb=1 матрица B транспонирована

transa = 1
transb = 1

# Размерность матрицы op(A)= m x k
# Размерность матрицы op(B)= k x n
# Размерность матрицы C= m x n

m = 120
k = 100
n = 80

# матрицы op(A), op(B) и C

Array_op_A = np.empty((m,k), dtype="int")
Array_op_B = np.empty((k,n), dtype="int")
Array_C = np.empty((m,n), dtype="int")

# Размерность матрицы A= s1 x s2
# Размерность матрицы B= t1 x t2
# размерность матрицы A:  s1 x s2

if transa == 0:   # op(A)=A
   s1 = m
   s2 = k
else:     # op(A)=A^Т
    s1 = k
    s2 = m

# размерность матрицы B:  t1 x t2

if transb == 0:   # op(B)=B
    t1 = k
    t2 = n
else:    # op(B)=B^Т
    t1 = n
    t2 = k

print("размерность матрицы op(A): " + str(m) + "x" + str(k))
print("размерность матрицы op(B): " + str(k) + "x" + str(n))
print("размерность матрицы C: " + str(m) + "x" + str(n)+"\n")

print("размерность матрицы A: " + str(s1) + "x" + str(s2))
print("размерность матрицы B: " + str(t1) + "x" + str(t2)+"\n")


# матрицы A и B


#Array_A=range(s1)           # Array_A является списком из s1 строк
#for i in range(s1):
#   Array_A[i]=range(s2)    # Каждая строка является списком из s2 элементов


Array_A = np.empty((s1,s2), dtype="int")
Array_B = np.empty((t1,t2), dtype="int")
#Array_A = [s1, s2]
#Array_B = [t1, t2]

alpha = random.randint(0, 100)
beta = random.randint(0, 100)
print("параметер alpha: " + str(alpha))
print("параметер beta: " + str(beta))
print()

# -----------------------------------------------------------

# задание и печать элементов матрицы A

print("Array A" + "\n")
# i = 0

i = 0
while i < s1:
    str_A = " "
    j = 0
    while j< s2:
       Array_A[i][j] = random.randint(0, 100)
#       Array_A[i][j] = 0
       str_A = str_A + "(" + str(i) + str(j) + ") " + str(Array_A[i][j]) + "    "
       j = j+1
    print(str_A)
    i = i+1


print(" ")

# ----------------------------------------------------------------------

# задание и печать элементов матрицы B
print("Array B" + "\n")
i = 0
while i < t1:
    str_B = " "
    j = 0
    while j < t2:
        Array_B[i][j] = random.randint(0, 100)
        str_B = str_B + "(" + str(i) + str(j) + ") " + str(Array_B[i][j]) + "    "
        j = j+1
    i = i+1
    print(str_B)

print("\n")

# ----------------------------------------------------------------------

# задание и печать элементов матрицы С
print("Array С" + "\n")
i = 0
while i < m:
    str_C = " "
    j = 0
    while j < n:
        Array_C[i][j] = random.randint(0, 100)
        str_C = str_C + "(" + str(i) + str(j) + ") " + str(Array_C[i][j]) + "    "
        j = j+1
    i = i+1
    print(str_C)


print("\n")
# -----------------------------------------------------------
# матрица op(A)
print("Array op(A)" + "\n")
i = 0
while i < m:
    str_op_A = " "
    j = 0
    while j < k:
        if transa == 0:
           Array_op_A[i][j] = Array_A[i][j]
        else:
           Array_op_A[i][j] = Array_A[j][i]
        str_op_A = str_op_A + "(" + str(i) + str(j) + ") " + str(Array_op_A[i][j]) + "    "
        j = j+1
    print(str_op_A)
    i = i+1

print("\n")


# -----------------------------------------------------------
# матрица op(B)
print("Array op(B)" + "\n")
i = 0
while i < k:
    str_op_B = " "
    j = 0
    while j < n:
        if transb == 0:
            Array_op_B[i][j] = Array_B[i][j]
        else:
            Array_op_B[i][j] = Array_B[j][i]
        str_op_B = str_op_B + "(" + str(i) + str(j) + ") " + str(Array_op_B[i][j]) + "    "
        j = j+1
    print(str_op_B)
    i = i+1

print("\n")

# ----------------------------------------------------------------------------------------------

# записываем параметры alpha,beta
# размерности массивов m,n,k
# и сами массивы op(A),op(B) и C
# в файл "input.txt"


f = open('input.txt', 'w')

f.write(str(alpha) + "\n")
f.write(str(beta) + "\n")

f.write(str(m) + "\n")
f.write(str(k) + "\n")
f.write(str(n) + "\n")

i = 0
while i < m:
    j = 0
    while j < k:
        f.write(str(Array_op_A[i][j]) + "\n")
        j = j+1
    i = i+1

i = 0
while i < k:
    j = 0
    while j < n:
        f.write(str(Array_op_B[i][j]) + "\n")
        j = j+1
    i = i+1

i = 0
while i < m:
    j = 0
    while j < n:
        f.write(str(Array_C[i][j]) + "\n")
        j = j+1
    i = i+1


f.close()
