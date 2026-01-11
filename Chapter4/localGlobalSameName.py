def spam():
    eggs = 'spam local'
    print(eggs) # Prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs) # Prints 'bacon local'
    spam() # Calls the spam() function
    print(eggs) # Prints 'bacon local' again

eggs = 'global'
bacon()
print(eggs) # Prints 'global' since this is the global eggs variable