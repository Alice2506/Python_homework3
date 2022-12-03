# 1) Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.

def divide_numbers():
    print('Введите два числа: ')
    first_number = int(input())
    second_number = int(input())
    if second_number == 0:
        print('Деление на ноль невозможно')
        pass
    else:
        return first_number / second_number


print(divide_numbers())
