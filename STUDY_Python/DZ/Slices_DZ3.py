players = ['charles', 'martina', 'michael', 'florence', 'elena', 'nikolay', 'traktoryna', 'alesia', 'ivan']

First_three_players = players[:3]
print(f"The first three players in my team is {First_three_players}")

Three_players_in_middle = players[3:6]
print(f"The first three players in my team is {Three_players_in_middle}")

Last_three_players = players[-3:]
print(f"The first three players in my team is {Last_three_players}")

my_pizzas = ['Pepperoni', 'Spaisies', 'Bavarskaya', 'Firmennaya', 'Provance', '5 cheses', 'Alaska' ]
my_friend_pizzas = my_pizzas[:]
my_pizzas.append('Fermerskaya')
my_friend_pizzas.append('Barbeque')
print(f"My favorite pizzas are: {my_pizzas}. \n")
print(f"My friends favorite pizzas are: {my_friend_pizzas}.\n")

for pizza in my_pizzas:
    print(pizza)
print('\n')
for pizza in my_friend_pizzas:
    print(pizza)

