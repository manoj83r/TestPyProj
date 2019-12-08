'''2.) How to reverse a dictionary ?'''
'''9) How do you find out the number of key-value dictionarypings present in a dictionary?'''
dict1 = {4: 'Ram', 3: 'Sam', 5: 'John', 2: 'Raj'}
print('Original value:', dict1)
dict2 = {}
for (k, v) in dict1.items():
    dict2.update({v: k})
print('Reversed Value:' + str(dict2))
print('dict1 Length:'+str(dict1.__len__()))

