# Script that asks Joe for the password "swordfish" and keeps asking until he gets it right.
while True:
    print('Who are you?')
    name = input('> ')
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input('> ')
    if password == 'swordfish':
        break
print('Access granted. Thanks, Joe!')