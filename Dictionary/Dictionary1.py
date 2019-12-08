''' 1.) take user input and fill the key as Integer and values as String and then create the dictionary ?'''
dict1 = {}
while True:
    key_input = input('Enter the Key:')
    if key_input == 'x':
        break
    else:
        value_input = input('Enter the Value:')
        dict1.update({int(key_input): value_input})
print('Dictionary Value:' + str(dict1))
