# 10. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

print('Введите координаты точки А: ')
x1 = float(input('X = '))
y1 = float(input('Y = '))
print('Введите координаты точки B: ')
x2 = float(input('X = '))
y2 = float(input('Y = '))

from math import sqrt
print (f'Расстояние между точками A и B =', round (sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)) 
