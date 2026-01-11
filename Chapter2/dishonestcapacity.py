print("Enter 'TB' or 'GB' for the advertised unit of storage:")
unit = input('> ').lower()

# Calculate the amount that the advertisted capacity lies:
if unit == 'tb':
    discrepancy = 1000000000000 / 1099511627776
elif unit == 'gb':
    discrepancy = 1000000000 / 1073741824

print("Enter the advertised capacity:")
advertised_capacity = input('> ')
advertised_capacity = float(advertised_capacity)

# Calculate the real capacity, round it to the nearest hundreths:
# and convert it to a string so that it can be concatenated to the output
real_capacity = str(round(advertised_capacity * discrepancy, 2))

print(f"The actual capacity is {real_capacity} {unit.upper()}")