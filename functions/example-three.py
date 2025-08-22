def parrot(voltage, state='a staff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's ", state, "!")

# parrot(1000)
# parrot(voltage=100)
# parrot(voltage=1000000, action='VOOOOOM')
parrot('a million', state='pushing up the daises')