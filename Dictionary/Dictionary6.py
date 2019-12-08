'''6) How do you add given key-value pair to dictionary if and only if it is not present in the dictionary?'''
'''7) How do you retrieve a value associated with a given key from the dictionary?'''
'''8) How do you check whether a particular key/value exist in a dictionary?'''
dict1 = {4: 'Ram', 3: 'Sam', 5: 'John', 2: 'Raj'}
while True:
    key_input = input('Enter the Key:')
    if key_input == 'x':
        break
    else:
        value_input = input('Enter the Value:')
        if int(key_input) in dict1.keys():
            print('Dictionary already has the key:' + str(key_input))
            if value_input in dict1.get(int(key_input)):
                print("Dictionary already has the same key-value pair:{" + str(key_input)+":'"+value_input+"'}")
                break
        else:
            dict1.update({int(key_input): value_input})
print('Dictionary Value:' + str(dict1))


