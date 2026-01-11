import time, sys
indent = 0
indent_increasing = True

try:
    while True: # Main program loop
        print(' ' * indent, end='') # Print spaces for indentation
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second

        if indent_increasing:
            # Increase the number of spaces for indentation
            indent += 1
            if indent == 20:
                # Change direction
                indent_increasing = False
        else:
            # Decrease the number of spaces for indentation
            indent -= 1
            if indent == 0:
                # Change direction
                indent_increasing = True

except KeyboardInterrupt:
    sys.exit() # When Ctrl-C is pressed, end the program