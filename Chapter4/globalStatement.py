def spam():
    global eggs
    eggs = 'spam global'

eggs = 'global'
spam()
print(eggs) # Prints 'spam global' since spam() changed the global eggs variable