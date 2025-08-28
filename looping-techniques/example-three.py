questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for question, answer in zip(questions, answers):
    print('What is your {0}? It is {1}'.format(question, answer))