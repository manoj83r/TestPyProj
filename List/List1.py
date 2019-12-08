'''a.) Write a Python Code to print all negative elements in an List.
 b.) Write a Python Code to find sum of all List elements.
 c.) Write a Python Code to find maximum and minimum element in an List.
 d.) Write a Python Code to find second largest element in an List
 e.) Write a Python Code to count total number of even and odd elements in an List.
 f.) Write a Python Code to count total number of negative elements in an List.
 g.) Write a Python Code to copy all elements from an List to another List'''
list1 = [4, -3, 8, -10, -4, 23, 45, 67, -8]
list2 = []
sumOfList = 0
countOfNegativeNumber = 0
countOfEvenNumber = 0
countOfOddNumber = 0
maxValue = list1[0]
minValue = list1[0]
for element in list1:
    list2.append(element)
    if element < 0:
        print('Negative Element in the list:' + str(element))
        countOfNegativeNumber=countOfNegativeNumber+1
    sumOfList = sumOfList + element
    if maxValue < element:
        maxValue = element
    if minValue > element:
        minValue = element
    if element % 2 == 0:
        countOfEvenNumber=countOfEvenNumber+1
    elif element % 2 == 1:
        countOfOddNumber = countOfOddNumber + 1
print("Sum of List Element is:" + str(sumOfList))
print("Max Value:" + str(maxValue))
print("Max Value:" + str(minValue))
list1.sort(reverse=1)
print("2nd Largest Value in the list:" + str(list1[1]))
print("Count of total Negative numbers in the list:"+str(countOfNegativeNumber))
print("Count of total Even numbers in the list:"+str(countOfEvenNumber))
print("Count of total Odd numbers in the list:"+str(countOfOddNumber))
print("New list:"+str(list2))
