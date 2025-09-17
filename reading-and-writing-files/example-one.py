# f = open('workfile.txt', 'w', encoding='utf-8')

# mode = rb = readonly, wb = write only (overwrites existing files)
# mode = rb+ = read and write, ab = append

with open('workfile.txt', encoding='utf-8') as f:
    read_data = f.read()
    print(read_data)

print(f.closed)

f.read()