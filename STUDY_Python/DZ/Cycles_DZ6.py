#!/usr/bin/env python3
alien_color = 'yellow'
if alien_color == 'green':
    print("You earned five points")
elif alien_color == 'red':
    print("You earned ten points")
else:
    print("You earned fifteen points")
print('\n')

age = 100
if age < 2:
    print("Baby")
elif age < 2:
    print("Kid")
elif 4 <= age < 13:
    print("child")
elif 13 <= age < 20:
    print("teenager")
elif 20 <= age < 65:
    print("adult")
elif 65 <= age < 110:
    print("old man")
else:
    print("Do not live so much!")

print('\n')
favorite_fruits = ['avocado', 'grapes', 'bananas', 'apples', 'orange', 'mandarin', 'pineapple', 'grapefruit']
favorite_fruit = input("What's your favorite fruit?: ")
if favorite_fruit in favorite_fruits:
    print(f"I really like {favorite_fruit}")
else:
    print(f"I do not like {favorite_fruit}")