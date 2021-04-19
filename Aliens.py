allien_0 = {'color': 'green', 'points': 5}
allien_1 = {'color': 'yellow', 'points': 10}
allien_2 = {'color': 'red', 'points': 15}

alliens = [allien_0, allien_1, allien_2]

for alien in alliens:
    print(alien)

# Создание пустого списка для хранения пришельцев

aliens = []
# Создание 30 зеленых пришельцев
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10


# Вывод первых 5 пришельцев
for alien in aliens[:5]:
    print(alien)

# Вывод количества созданных пришельцев
print(f"Total number of aliens: {len(aliens)}")