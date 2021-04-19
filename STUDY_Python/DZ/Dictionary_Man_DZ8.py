man = {
    'first_name': 'Gena',
    'last_name': 'Bukin',
    'age': '39',
    'city': 'Ekaterinburg'

}
print(man['first_name'])
print(man['last_name'])
print(man['age'])
print(man.get('sex'))
print(man.get('Weight', 'There is no such key '))
print(man['city'])

print("\n")

favorite_numbers = {
    'Elena': '6',
    'Egor': '5',
    'Ilya': '37',
    'Vitaly': '7',
    'Inna': '69'
}
print(f"Inna's favorite number is {favorite_numbers['Inna']}")
print(f"Elena's favorite number is {favorite_numbers['Elena']}")
print(f"Egor's favorite number is {favorite_numbers['Egor']}")
print(f"Ilya's favorite number is {favorite_numbers['Ilya']}")
print(f"Vitaly's favorite number is {favorite_numbers['Vitaly']}")

print("\n")

Programmer_dictionary = {
    'id': 'идентификатор',
    'Bug': 'ошибка в программе/коде',
    'Bot': 'программа, имитирующая действия человека, иногда с зачатками искусственного интеллекта',
    'directory': 'папка',
    'increment': 'увеличение значения на заданное значение',
    'customer': 'покупатель, клиент или заказчик',
    'code review': 'рецензирование/проверка кода с целью обнаружения и исправления ошибок',
    'constant': 'переменная, которую нельзя изменить',
    'boolean': 'это тип данных, переменные которого содержат одно из двух возможный значений: true (1) или false (0)',
    'overflow': 'происходит, когда запрашиваемой памяти нет в наличии (вся память уже занята)',

}
for key, value in Programmer_dictionary.items():
    print(f"{key} - это \n{value}")


print("\n")

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',

}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"\nValue: {value}")

