def spam(divide_by):
    try:
        # Any code that might cause an exception goes in the try block
        return 42 / divide_by
    except ZeroDivisionError:
        print('Error: Invalid argument. You tried to divide by zero.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
print(spam(8))
