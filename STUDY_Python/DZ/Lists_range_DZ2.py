for value in range(1,21):
    print(value)

million = []
for value in range (1,1000001):
    million.append(value)
print(million)

print(min(million))
print(max(million))
print(sum(million))

for value in range(1,21,2):
    print(value)

multiples_of_three = []

for value in range(3,31):
    if value%3 == 0:
        multiples_of_three.append(value)
print(multiples_of_three)

cubes = []
for value in range(1,101):
    cube = value**3
    cubes.append(cube)
print(cubes)

cubes2 = [value**3 for value in range(1,11)]
print(cubes2)