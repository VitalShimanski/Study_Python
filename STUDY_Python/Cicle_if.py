cars = ['audi', 'bmw', 'subaru', 'toyoya', 'opel', 'chevrolet', 'nissan', 'citrioen']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print('\n')

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print('Hold the anchovies!')
print('\n')
requested_topping = ['mushrooms', 'onions', 'pineapple']
user_message = input("Что бы Вы хотели добавть к Вашей пицце?: ")
if user_message in requested_topping:
    print('OK, start cooking pizza')
else:
    print(f"Add {user_message} please!")
print('\n')

answer = 17
if answer != 42:
    print('That is not the correct answer. Please try again!')
print('\n')

age_0 = 22
age_1 = 23
if (age_0 >= 21) and (age_1 >= 21):
    print('Your team admitted')
else:
    print('Your team disqualified')
print('\n')

banned_users = ['andrew', 'carolina', 'svetlana', 'ivan', 'sergey', 'pavel']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a responce if you whish")
