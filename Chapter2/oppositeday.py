today_is_opposite_day = True

# Set say_its_opposite_day based on today_is_opposite_day
if today_is_opposite_day:
    say_its_opposite_day = True
else:
    say_its_opposite_day = False

# If it is opposite day, print the opposite of the statement
if say_its_opposite_day:
    say_its_opposite_day = not say_its_opposite_day

# Say what day it is
if say_its_opposite_day:
    print("Today is Opposite day.")
else:
    print("Today is not Opposite day")