import json
x = [1, 'simple', 'list']
print(json.dumps(x))

# with open('list.json', 'w', encoding='utf-8') as f:
#     json.dump(x, f)

with open('list.json', 'r', encoding='utf-8') as f:
    y = json.load(f)
    print(y)