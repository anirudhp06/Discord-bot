"""book={'ping':'pong','pong':'ping','andrew':'andrew senpai'}
inp=input('Enter something:').lower()
if inp in book:
    print(book[inp])
else:
    print('Nothing')"""
from os import path
act=path.isfile('rest.txt')
print(act)