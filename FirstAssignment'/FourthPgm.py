salary = int(input("Enter your salary:"))
serviceYear = int(input ("Enter number of years of your service in the company:"))
if serviceYear>5:
    bonusAmount = salary * 0.05
    print("Your Bonus Amount is:", str(bonusAmount))
else:
    print("Sorry there is no Bonus")
