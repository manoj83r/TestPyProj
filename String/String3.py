"""7) Write a Python program to find duplicate characters in a string?"""


# string1 = input("Enter a sentence and pgm will count number of words in it:")
def dup_char(s1, d1):
    for char in range(len(s1)):
        key = s1[char]
        if key in d1.keys():
            c = d1.get(key)
            d1.update({key: c + 1})
        else:
            d1.update({key: 1})
    print("Each character occurrence:" + str(d1))
    for (k, v) in d1.items():
        if v > 1:
            print("Character \'" + k + "\' occurred duplicate in the sentence and count of occurrence is:" + str(v))


string1 = 'This is sentence i am writing     to count'
dict1 = {}
dup_char(string1, dict1)
print(sum(dict1.values()))
print(len(string1))
