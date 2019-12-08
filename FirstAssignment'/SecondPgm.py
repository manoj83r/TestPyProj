firstValue = input("Enter the 1st Integer Value:")
secondValue = input("Enter the 2nd Integer Value:")
firstValue = int(firstValue)
secondValue = int (secondValue)
if firstValue > secondValue :
    print("Greatest value is:", str(firstValue))
elif firstValue < secondValue :
    print("Greatest value is:", str(secondValue))
else:
    print("Both values are same:", str(firstValue))