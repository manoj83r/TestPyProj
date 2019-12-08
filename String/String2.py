"""5) Write a Python program to count the number of occurrences of each character in a string?"""
# string1 = input("Enter a sentence and pgm will count number of words in it:")
string1 = 'This is sentence i am writing     to count'
dict1 = {}
count = 1
for char in range(len(string1)):
    key = string1[char]
    if key in dict1.keys():
        count = dict1.get(key)
        dict1.update({key: count + 1})
    else:
        dict1.update({key: 1})
print("Each character occurrence:" + str(dict1))
for (k, v) in dict1.items():
    print("Character \'" + k + "\' count is:" + str(v))
print(sum(dict1.values()))
print(len(string1))
