favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
peoples = ['adam', 'sergey', 'jen', 'sarah', 'edward', 'lesly', 'amanda', 'phil', 'ivan']

for name in peoples:
    if name in peoples and name not in favorite_languages:
        print(f"{name.title()} please take our pool!")
    else:
        print(f"{name.title()} thanks for taking part in the pool!")

print("\n")

rivers = {
    'Nile': 'Egipt',
    'Amazonka': 'Brazil',
    'Yantzy': 'China',
    'Missisipy': 'USA',
    'Enisey': 'Russia',
    'Huanhe': 'China',
    'Chambeshi': 'Kongo',
    'Amur': 'Russia',
    'Lena': 'Russia',
    'Niger': 'Nigeria'
}
for key, value in rivers.items():
    print(f"{key} runs through {value}")