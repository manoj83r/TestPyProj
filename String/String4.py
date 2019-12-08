"""1.) Write a Python program to find the duplicate words and their number of occurrences in a string?"""
# string1 = input("Enter a sentence and pgm will count number of words in it:")
string1 = 'This is sentence is to writing  is   to count'
list1 = string1.split()
print(list1)
dict1 = {}
count = 1
for word in list1:
    if word in dict1.keys():
        count = dict1.get(word)
        dict1.update({word: count+1})
    else:
        dict1.update({word: 1})
print("Each character occurrence:"+str(dict1))
for (k, v) in dict1.items():
    if v > 1:
        print("Character \'"+k+"\' occurred duplicate in the sentence and count of occurrence is:"+str(v))
print(sum(dict1.values()))
print(len(string1))
'''
8) How do you convert string to integer and integer to string in Python?
9) Write a Python program to find the percentage of uppercase letters, lowercase letters, digits and special characters in a given string?
10) How to Get Index Of All Character in Strings In Python ?'''