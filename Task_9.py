# 9. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

number = int (input('Введите номер четверти: '))
if number >= 1 and number <= 4:
    if number == 1:
        print('x > 0; y > 0')
    elif number == 2:
        print('x < 0; y > 0')
    elif number == 3:
        print('x < 0; y < 0')
    elif number == 4:
        print('x > 0; y < 0')
else:
    print ('Ошибка! Введите цифру от 1 до 4.')
    