# print('We are the {} who say {}!'.format('knights', 'Ni'))

# print('{0} and {1}'.format('spam', 'eggs'))
# print('{1} and {0}'.format('spam', 'eggs'))

# print('This {food} is {adjective}'.format(food='spam', adjective='absolutely horrible'))

# print('The story of {0}, {1}, and {other}'.format('Bill', 'Manfred', other='Georg'))

# table = {'John': 4127, 'Jack': 4098, 'Deborah': 8637678}
# print('Jack: {0[Jack]:d}; John: {0[John]:d}; Deborah: {0[Deborah]:d}'.format(table))

table = {'John': 4127, 'Jack': 4098, 'Deborah': 8637678}
# print('Jack: {Jack:d}; John: {John:d}; Deborah: {Deborah:d}'.format(**table))

# table = {k: str(v) for k, v in vars().items()}
# message = " ".join([f'{k}:' + '{' + k  + '};' for k in table.keys()])
# print(message.format(**table))

# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

nums = list(range(1, 13))
for x in nums:
    print('2 x {0} = {1}'.format(x, x*2))