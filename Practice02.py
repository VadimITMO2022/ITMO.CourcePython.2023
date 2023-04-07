import math

def func_d1(dd1): # расстояние d1 в футах
    return dd1*3.

def func_h(hh): # расстояние h в футах
    return hh * 3.

def func_v_sand(vvv_sand): # скорость v_sand в футах/сек
    vv_sand = vvv_sand * 5280.
    return vv_sand / 3600.

def func_theta1(ttheta1): # угол theta1 в радианах
    return ttheta1 / 180. * math.pi

def func_x(d1,theta1): # расстояние x в футах
    return d1 * math.tan(theta1)

def func_l1(x, d1):  # расстояние l1 в футах
    return math.sqrt(x ** 2 + d1 ** 2)

def func_l2(h, x, d2):  # расстояние l2 в футах
    return math.sqrt((h - x) ** 2 + d2 ** 2)

def func_t(v_sand, l1, l2, n):  # время t в секундах
    tt = 1. / v_sand * (l1 + n * l2)
    return "{:4.1f}".format(tt)

#-----------------------------------------------------------------------------------------------

#dd1 = float(input("Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды)"))
#d2 = float(input("Введите кратчайшее расстояние от утопающего до берега, d2 (футы)"))
#hh = float(input("Введите боковое смещение между спасателем и утопающим, h (ярды)"))
#vvv_sand = float(input("Введите скорость движения спасателя по песку, v_sand (мили в час)"))
#n = float(input("Введите коэффициент замедления спасателя при движении в воде, n"))
#ttheta1 = float(input("Введите направление движения спасателя по песку, theta1 (градусы)"))

#-----------------------------------------------------------------------------------------------

# значения параметров
dd1 = 8
d2 = 10
hh = 50
vvv_sand = 5
n = 2
ttheta1 = 39.413

# вычисление функций

d1=func_d1(dd1)  # расстояние d1 в футах

h=func_h(hh) # расстояние h в футах

v_sand=func_v_sand(vvv_sand) # скорость v_sand в футах/сек

theta1= func_theta1(ttheta1) # угол theta1 в радианах

x=func_x(d1,theta1) # расстояние x в футах

l1=func_l1(x, d1) # расстояние l1 в футах

l2=func_l2(h, x, d2) # расстояние l2 в футах

t=func_t(v_sand, l1, l2, n) # время t в секундах в нужном формате

# тесты

print("d1=",d1)
print("h=",h)
print("v_sand=",v_sand)
print("theta1=",theta1)
print("x=",x)
print("l1=",l1)
print("l2=",l2)
print("t=",t)

print("Если спасатель начнёт движение под углом theta1, равным " + \
      str(ttheta1) + " градусам, он достигнет утопающего через " + str(t) + " секунды")





