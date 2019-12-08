'''5) How do you add key-value pairs to dictionary?'''
dict1 = {4: 'Ram', 3: 'Sam', 5: 'John', 2: 'Raj'}
while True:
    key_input = input('Enter the Key:')
    if key_input == 'x':
        break
    else:
        value_input = input('Enter the Value:')
        dict1.update({int(key_input): value_input})
print('Dictionary Value:' + str(dict1))


