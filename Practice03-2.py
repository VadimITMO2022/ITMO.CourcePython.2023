import math
import matplotlib.pyplot as plt
import numpy as np

ttheta1 = np.linspace(79, 81, 200)

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
    return d1 * np.tan(theta1)

def func_l1(x, d1):  # расстояние l1 в футах
    return np.sqrt(x ** 2 + d1 ** 2)

def func_l2(h, x, d2):  # расстояние l2 в футах
    return np.sqrt((h - x) ** 2 + d2 ** 2)

def func_t(v_sand, l1, l2, n):  # время t в секундах
    tt = 1. / v_sand * (l1 + n * l2)
    return tt

def func_dt(d1,x,v_sand, l1, l2, n,h,theta1):  # derivative dt / d theta1 в секундах/градус
    dt = 1./v_sand*(x/l1+n*(x-h)/l2)*d1/(np.cos(theta1))**2
    return dt

def func_theta1_plot(ttheta1): # the dependence of the derivative dt/d theta1 on angle \theta1
    # some input parameters
    dd1 = 8
    d2 = 10
    hh = 50
    vvv_sand = 5
    n = 2

    d1 = dd1 * 3.  # расстояние d1 в футах
    h = hh * 3.  # расстояние h в футах
    vv_sand = vvv_sand * 5280.  # скорость  vv_sand в футах/час
    v_sand = vv_sand / 3600.  # скорость v_sand в футах/сек
    theta1 = ttheta1 / 180. * math.pi  # угол theta1 в радианах
    xx = d1 * np.tan(theta1)  # расстояния x, l1, l2
    l1 = np.sqrt(xx ** 2 + d1 ** 2)
    l2 = np.sqrt((h - xx) ** 2 + d2 ** 2)

    d1 = func_d1(dd1)  # расстояние d1 в футах
    h = func_h(hh)  # расстояние h в футах
    v_sand = func_v_sand(vvv_sand)  # скорость v_sand в футах/сек
    theta1 = func_theta1(ttheta1)  # угол theta1 в радианах
    x = func_x(d1, theta1)  # расстояние x в футах
    l1 = func_l1(x, d1)  # расстояние l1 в футах
    l2 = func_l2(h, x, d2)  # расстояние l2 в футах
    derivative=func_dt(d1,x,v_sand, l1, l2, n,h,theta1) #the derivative dt / d theta1

    return derivative

#--------------------------------------------------------------------------------

# plot the dependence of the derivative dt/d theta1 on angle theta1 as a graph
dpi = 80
fig = plt.figure(dpi=dpi, figsize=(512/dpi , 384/dpi ))
plt.plot(ttheta1, func_theta1_plot(ttheta1), 'go-')
plt.legend(["derivative 'dt/d theta1' vs angle 'theta1'"], loc='upper left')
fig.savefig('dt-theta1.png')
plt.show()

# plot the dependence of the derivative dt/d theta1 on angle theta1 as a table
i = 0
while i < 200:
          ttheta1 = 75.+10. *(i/200.)
          dt=func_theta1_plot(ttheta1)
          print(ttheta1,dt)
          i += 1