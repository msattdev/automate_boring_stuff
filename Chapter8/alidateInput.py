while True:
    print('Enter your age:')
    age = input() # User inputs age
    if age.isdecimal(): # Check if input is all digits
        break # Exit loop if input is all digits
    print('Please enter a number for your age.') # If input is not all digits, prompt again

while True:
    print('Select a new password (letters and numbers only):')
    password = input() # User inputs password
    if password.isalnum(): # Check if input is alphanumeric
        break # Exit loop if input is alphanumeric
    print('Passwords can only have letters and numbers.') # If input is not alphanumeric, prompt again