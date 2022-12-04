# 3) Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(first_arg, second_arg, third_arg):
    my_sum = 0
    if first_arg < second_arg and first_arg < third_arg:
        my_sum = second_arg + third_arg
    elif second_arg < first_arg and second_arg < third_arg:
        my_sum = first_arg + third_arg
    else:
        my_sum = first_arg + second_arg
    return my_sum
print(my_func(9, 6, 6))