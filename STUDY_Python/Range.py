for value in range(1,10):
    print(value)

numbers = list(range (1,10))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,100,2):
    square = value**2
    squares.append(square)
print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

