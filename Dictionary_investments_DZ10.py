
gena_bukin_1981 = {
    'first_name': 'gena',
    'last_name': 'bukin',
    'age': '39',
    'city': 'ekaterinburg'
}
slava_kozlov_1979 = {
    'first_name': 'slava',
    'last_name': 'kozlov',
    'age': '41',
    'city': 'zhlobin'
}
vlad_lagun_1988 = {
    'first_name': 'vlad',
    'last_name': 'lagun',
    'age': '32',
    'city': 'slutck'
}
vital_shim_1981 = {
    'first_name': 'vital',
    'last_name': 'shimanski',
    'age': '39',
    'city': 'minsk'
}
peoples = [gena_bukin_1981, slava_kozlov_1979, vlad_lagun_1988, vital_shim_1981]

for people_info in peoples:
    full_name = f"{people_info['first_name']} {people_info['last_name']}"
    city = f"{people_info['city']}"
    print(f"{full_name.title()} {people_info['age']} от роду, проживает"
          f" в городе {city.title()}")
print("\n")
