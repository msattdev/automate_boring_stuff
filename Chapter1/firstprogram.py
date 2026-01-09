# This program says hello and asks for my name.

print("Hello, World!")
print('What is your name?') # Ask for their name.
my_name = input('>') # Get their name and store it as the my_name variable.
print('It is good to meet you, ' + my_name) 
print('The length of your name is: ')
print(len(my_name)) # Print the length of their name.
print('What is your age?') # Ask for their age.
my_age = input('>') 
print('You will be ' + str(int(my_age) + 1) + ' in a year.') # Tell them how old they will be in a year.