alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 10
alien_1['x_position'] = 15
alien_1['y_position'] = 45
print(alien_1)

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0 ['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
alien_0['speed'] = 'max'
print(f"Original position: {alien_0['x_position']}")
# Пришелец перемещается вправо
# Вычисляем величину смещения на основании текущей скорости

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'max':
    x_increment = 3
else:
    alien_0['speed'] == 0
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

print("\n")

# Удаление пары ключ-значение
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

print("\n")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
language = favorite_languages['phil'].title()
print(f"Phil's favorite language is {language}.")
print("\n")
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")
print("\n")
for name in favorite_languages.keys():
    print(f"{name.title()}")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi, {name.title()}")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\tHi, {name.title()}, I see you love {language}!")
if 'olga' not in favorite_languages.keys():
    print("Olga, please take our poll!!!")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the pool.")
print("The following languages have been mentioned: ")
for language in favorite_languages.values():
    print(language.title())
print("\n")
for language in set(favorite_languages.values()):
    print(language.title())

print("\n")
# Метод get()
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned')
print(point_value)
point_value = alien_0.get('points')
print(point_value)