"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
Она растет на круглой грядке, причем кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних. Всего на
грядке растет N кустов. Эти кусты обладают разной урожайностью,
поэтому ко времени сбора на них выросло различное число ягод –
на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена
система автоматического сбора черники. Эта система состоит из управляющего
модуля и нескольких собирающих модулей. Собирающий модуль за один заход,
находясь непосредственно перед некоторым кустом, собирает ягоды с этого
куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.

4 -> 1 2 3 4
9
"""

from random import randint

def user_input(message, min_elem, max_elem):
    input_error: bool = True
    while input_error:
        try:
            number = int(input(message))
        except:
            print("Вы ввели не число!")
        else:
            if min_elem <= number <= max_elem:
                input_error = False
            else:
                print("Вы ввели число, не соответствующее условию!")
    return number

def find_max_berry(input_list):
    input_list.insert(0, input_list[len(input_list) - 1])
    input_list.append(input_list[1])
    max_summ = 0
    for i in range(1, len(input_list) - 1):
        summ = input_list[i - 1] + input_list[i] + input_list[i + 1]
        if summ > max_summ:
            max_summ = summ
    return max_summ


quantity_elements = user_input(message = "Введите кол-во кустов черники (от 1 до 100): ", min_elem = 1, max_elem = 100)
list_1 = [randint(1, 20) for i in range(quantity_elements)]

print(list_1)
print(f'Максимальное количество ягод: {find_max_berry(list_1)}')


