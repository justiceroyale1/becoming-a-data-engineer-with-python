vec = [-4, -2, 0, 2, 4]

# doubled = [x*2 for x in vec]
# print(doubled)

# remove_negatives = [x for x in vec if x >= 0]
# print(remove_negatives)

# apply_function = [abs(x) for x in vec]
# print(apply_function)

# freshfruits = ['   banana', '   loganberry', 'passion fruit   ']
# freshfruits_stripped = [fruit.strip() for fruit in freshfruits]
# print('freshfruit: ', freshfruits)
# print('freshfruit_stripped', freshfruits_stripped) 

# tuples = [(x, x**2) for x in range(6)]
# print(tuples)
# tuples = [x, x**2 for x in range(6)]
# print(tuples)

vec = [[1,2,3], [4,5,6], [7,8,9]]
flatten_vec = [num for elem in vec for num in elem]
print(flatten_vec)