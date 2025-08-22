def concat(*args, seperator='/'):
    return seperator.join(args)

print(concat('earth', 'mars', 'venus', seperator='.'))