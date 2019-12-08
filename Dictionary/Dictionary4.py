'''4.) How to add the key if and only if it is not present inside the dictionary ?'''
dict1 = {4: 'Ram', 3: 'Sam', 5: 'John', 2: 'Raj'}
while True:
    key_input = input('Enter the Key:')
    if key_input == 'x':
        break
    elif int(key_input) in dict1.keys():
        print('Dictionary already has the key:' + str(key_input))
        break
    else:
        print("List value:" + str(dict1.keys()))
        value_input = input('Enter the Value:')
        dict1.update({int(key_input): value_input})
print('Dictionary Value:' + str(dict1))

