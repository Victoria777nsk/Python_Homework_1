# 6. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

day_number = int (input ('Введите цифру, обозначающую день недели: '))
if day_number >= 1 and day_number <= 7 :
    if day_number == 6 or day_number == 7:
        print ('День является выходным.')
    else:
        print ('День НЕ является выходным.')
else:
    print ('Ошибка! Введите цифру от 1 до 7.')
