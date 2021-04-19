users = ['admin', 'Leha05022010', 'VitShim', 'vitalesasha', 'dimon', 'vovan', 'diktator']
if users:
    for user in users:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f"Hello {user}, thank you for loggin in again")
else:
    print("We need to ind some users")

print("\n")

current_users = ['Andrew', 'Zadrot', 'Picasso', 'tikhon', 'Abrakadabra', 'McDonnel', 'Slava1972']
current_users2 = current_users[:]


new_users = ['Zlata1988', 'Zadrot', 'KimChenUn', 'TIKHON', 'Fedor1975', 'McDonnel', 'Surinam']
for user in new_users:
    if user not in current_users2:
        print(f"{user} free for registration")
    else:
        print(f"{user} is not available, please select another name to registration")

print("\n")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number != 1 and number != 2 and number != 3:
        print(f"{number}th\n")
    elif number == 1:
        print(f"{number}st\n")
    elif number == 2:
        print(f"{number}nd\n")
    elif number == 3:
        print(f"{number}rd\n")