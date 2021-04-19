pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
print(f"You ordered a {pizza['crust']} - crust pizza "
      "whith the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

prompt = "\nTell me which topping do you added your pizza? "
prompt += "\nEnter 'quit' to end the programm. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
