footballers = ['Haaland', 'Gabriel Jesus', 'Foden', 'Ederson', 'Gabriel Martinelli']

print('original:', footballers)

# footballers.append('Odergaard')

# print('append:', footballers)

# extension = ['Saka', 'Maguire', 'Cole Palmer']

# footballers.extend(extension)

# print('extend:', footballers)

# footballers.insert(0, 'Jay Z')

# print('insert:', footballers)

# footballers.remove('Jay Z')

# print('remove:', footballers)

# pop_value = footballers.pop()

# print('pop:', footballers)
# print('pop_value:', pop_value)

footballers.clear()
print('clear:', footballers)

footballers = ['Haaland', 'Gabriel', 'Foden', 'Ederson', 'Gabriel']
index_value = footballers.index('Foden')
index_value2 = footballers.index('Gabriel')
index_value3 = footballers.index('Gabriel', 2)
index_value4 = footballers.index('Gabriel', 2, 5)
print('index_value:', index_value)
print('index_value2:', index_value2)
print('index_value3:', index_value3)
print('index_value4:', index_value4)

count_value = footballers.count('Gabriel')
print('count_value:', count_value)

footballers.sort()
print('sort:', footballers)

footballers.sort(reverse=True)
print('reverse sort', footballers)

footballers.reverse()
print('reverse:', footballers)

footballers_copy = footballers.copy()
print('footballers:', footballers)
print('footballers_copy', footballers_copy)