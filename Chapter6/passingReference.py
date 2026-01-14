def eggs(some_parameter): # Argument is a reference to the list spam
    some_parameter.append('Hello') # Modifies the list referred to by some_parameter

spam = [1, 2, 3]
eggs(spam)
print(spam)  # Prints [1, 2, 3, 'Hello']