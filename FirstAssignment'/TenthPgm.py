a = input("Enter an Character:")
if a.isupper() and len(a) == 1:
    print("Its an upper Character")
elif a.islower() and len(a) == 1:
    print("Its an lower Character")
else:
    print("Other type of character")