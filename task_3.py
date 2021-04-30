"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //, НЕ ИСПОЛЬЗУЕМ ОПЕРАЦИИ ВЗЯТИЯ ЭЛЕМЕНТА ПО ИНДЕКСУ
Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить и на числах, заканчивающихся нулем.
Пример:
Введите число, которое требуется перевернуть: 1230
Перевернутое число: 0321
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

"""
#  Рабочий вариант №1
def rev_num(num, index=-1):
    try:
        print(num[index], end='')
    except IndexError:
        return
    else:
        index -= 1
        rev_num(num, index)
rev_num('1230')
"""


def revers_number(numb):
    #  Рекурсия
    rest_numb, numeral = divmod(numb, 10)
    if rest_numb == 0:
        return str(numeral)
    else:
        return str(numeral) + str(revers_number(rest_numb))


number = int(input("Введите число, которое требуется перевернуть:"))
print(f'Перевёрнутое число: {revers_number(number)}')
