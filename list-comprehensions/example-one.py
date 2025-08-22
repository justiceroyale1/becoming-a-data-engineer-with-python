# squares = []
# for x in range(10):
#     squares.append(x**2)

# print(squares)

# squares = list(map(lambda x: x**2, range(10)))
# print(squares)

# squares = [x**2 for x in range(10)]
# print(squares)

tuples = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(tuples)