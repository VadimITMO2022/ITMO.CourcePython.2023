import time
import pygame as p
import random
from pygame.locals import *
from PIL import Image

#-------------------------------------------------------------------------------------------

# Константы цветов RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
# Создаем окно
root = p.display.set_mode((1000, 500))


# начальная конфигурация
# 2х мерный список с помощью генераторных выражений
cells3 = [[random.choice([0, 1]) for j in range(root.get_width() // 20)] for i in range(root.get_height() // 20)]


# запись начальной конфигурации в файл
f_input = open('Practice05-input.txt', 'w')
for j in range(root.get_width() // 20):
    for i in range(root.get_height() // 20):
        f_input.write(str(cells3[i][j]) + "\n")
f_input.close()

# извлечение начальной конфигурации из файла
f_output = open('Practice05-input.txt', 'r')
cells = [[0 for j in range(root.get_width() // 20)] for i in range(root.get_height() // 20)]
for j in range(root.get_width() // 20):
    for i in range(root.get_height() // 20):
        cells[i][j] = int(f_output.readline())
f_output.close()


# красный цвет для клеток
color_cells = [[255 for j in range(root.get_width() // 20)] for i in range(root.get_height() // 20)]

# Функция определения кол-ва соседей
def near(pos: list, system=[[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]):
    count = 0
    for i in system:
        if cells[(pos[0] + i[0]) % len(cells)][(pos[1] + i[1]) % len(cells[0])]:
            count += 1
    return count

# ввод числа шагов моделирования игры с консоли
count_max = int(input("введите число шагов моделирования игры Жизнь \n"))

count = 0
# Основной цикл
while count < count_max:
# while 1:
# Заполняем экран белым цветом
    root.fill(WHITE)
# создаем сетку во все окно
    # Рисуем сетку
    for i in range(0, root.get_height() // 20):
        p.draw.line(root, BLACK, (0, i * 20), (root.get_width(), i * 20))
    for j in range(0, root.get_width() // 20):
        p.draw.line(root, BLACK, (j * 20, 0), (j * 20, root.get_height()))
# Нужно чтобы виндовс не думал что программа "не отвечает"
    for i in p.event.get():
        if i.type == QUIT:
            quit()

 #------------------------------------------------------------------------------

# Записываем в прямоугольник конфигурацию клеток

    for i in range(0, len(cells)):
        for j in range(0, len(cells[i])):
            print(cells[i][j], i, j)
            p.draw.rect(root, (color_cells[i][j] * cells[i][j] % 256, 0, 0), [i * 20, j * 20, 20, 20])
 #           p.draw.rect(root, (255 * cells[i][j] % 256, 0, 0), [i * 20, j * 20, 20, 20])

    # Обновляем экран
    p.display.update()
 #   new_img = root
#    new_img.save.update()
    if(count % 5 == 0):
      image_name = 'Practice05-Images/'+str(count)+'.png'
      p.image.save(root, image_name)
    cells2 = [[0 for j in range(len(cells[0]))] for i in range(len(cells))]
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            if cells[i][j]:
                # Если у клетки не 2 или 3 соседа
                if near([i, j]) not in (2, 3):
                    cells2[i][j] = 0
                    continue
                    # В ином случае
                cells2[i][j] = 1
                color_cells[i][j] -= 40
                continue
                # Если клетка мертва и у неё 3 соседа
            if near([i, j]) == 3:
                cells2[i][j] = 1
                color_cells[i][j]=255
                continue
                # В противном случае
            cells2[i][j] = 0
    cells = cells2

    count += 1
