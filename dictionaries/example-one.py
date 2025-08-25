tel = {'jack': 4098, 'sape': 4139}
print(tel)

tel['guido'] = 4127
print(tel)

del tel['sape']
print(tel)

print("Jack's number is;", tel['jack'])

tel['irv'] = 4127

print("Key's unsorted:", list(tel))
print("Key's sorted:", sorted(tel))

print('guido' in tel)

print('jack' not in tel)