# 2) Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры
# как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def user_info(name, surname, birth_year, city, email, phone):
    print(f'Информация о пользователе: имя - {name}, фамилия - {surname}, год рождения - {birth_year},'
          f'город проживания - {city}, email - {email}, телефон - {phone}')
user_info(name='Алиса', surname='Селезнева', birth_year='1994', city='Москва',
          email='alicesel@gmail.com', phone='89886767677')