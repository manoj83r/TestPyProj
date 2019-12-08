person1Age = int(input("Enter 1st persons age:"))
person2Age = int(input("Enter 2nd persons age:"))
person3Age = int(input("Enter 3rd persons age:"))
if (person1Age <= person2Age) and (person1Age <= person3Age) :
    print("1st person is youngest")
elif (person2Age <= person1Age) and (person2Age <= person3Age) :
    print("2nd person is youngest")
else :
    print("3rd person is youngest")

if (person1Age >= person2Age) and (person1Age >= person3Age):
    print("1st person is oldest")
elif (person2Age >= person1Age) and (person2Age >= person3Age):
    print("2nd person is oldest")
else:
    print("3rd person is oldest")

