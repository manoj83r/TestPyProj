"""2) Write a Python program to count the number of words in a string?
3) Write a Python program to count the total number of occurrences of a given character in a string ?
4) Write a Python program to reverse a string?
6) Write a Python program to remove all white spaces from a string?"""
# string1 = input("Enter a sentence and pgm will count number of words in it:")
string1 = 'This is sentence i am writing     to count'
string2 = string1.replace(' ', '')
charToCount = input("Enter the Character to be counted:")
print("Total occurrence of the character:\'" + charToCount + "\' is:" + str(string1.count(charToCount)))
print("Number of word:" + str(len(string1.split())))
print("Reversed string:" + string1[::-1])
print("String after removing all white spaces:" + string2)
