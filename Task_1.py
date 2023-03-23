"""
Задача 22: Даны два неупорядоченных набора
целых чисел (может быть, с повторениями). Выдать
без повторений в порядке возрастания все те числа,
которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов
первого множества. m - кол-во элементов второго
множества. Затем пользователь вводит сами элементы множеств.
Например:
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18

6 12
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

# Находим одинаковые элементы двух списков, создаем из них новый
# список, переводим его в множество и возвращаем элементы
# отсортированным списком
def matching_numbers(list1, list2):
    res_list = []
    for i in range(len(list1)):
        if list1[i] in list2:
            res_list.append(list1[i])
    res_set = set(res_list)
    return sorted(res_set)




quantity_elements_list1 = user_input(message = "Введите кол-во элементов первого множества (от 1 до 100): ", min_elem = 1, max_elem = 100)
quantity_elements_list2 = user_input(message = "Введите кол-во элементов второго множества (от 1 до 100): ", min_elem = 1, max_elem = 100)
list_1 = [randint(1, 20) for i in range(quantity_elements_list1)]
list_2 = [randint(1, 20) for i in range(quantity_elements_list2)]

print(list_1)
print(list_2)
print(*matching_numbers(list_1, list_2))



