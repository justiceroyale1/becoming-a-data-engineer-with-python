with open('newfile.txt', 'a', encoding='utf-8') as f:
    # print(f.write('This is a test\n'))
    value = ('the answer', 42)
    s = str(value)
    print(f.write(s))