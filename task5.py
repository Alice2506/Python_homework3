# 5) Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
# ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится
# специальный символ, выполнение программы завершается. Если специальный символ введен
# после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
# ранее сумме и после этого завершить программу.

result_sum = 0
stop_prog = False
while stop_prog == False:
    print('Введите числа через пробел или клавишу "j" для выхода: ')
    user_numbers = input().split(' ')
    transitional_sum = 0
    for el in range(len(user_numbers)):
        if user_numbers[el] == 'j' or user_numbers[el] == 'J':
            stop_prog = True
            break
        else:
            user_numbers = list(map(int, user_numbers))
            transitional_sum = sum(user_numbers)
            print(transitional_sum)
    result_sum += transitional_sum
    print(f'Ваш текущий итог: {result_sum}')
print(f'Ваша итоговая сумма: {result_sum}')








