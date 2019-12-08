noOfClassHeld = int(input("Enter the number of class held:"))
noOfClassAttended = int(input("Enter the number of class attended:"))
perOfClassAttended = (noOfClassAttended/noOfClassHeld) * 100
if perOfClassAttended < 75:
    print("Your percentage of class attended is:", str(perOfClassAttended), "%")
    medicalCase = input("Low Attendance Because of Medical Illness(Y/N)?:")
    if medicalCase == 'Y':
        print("You are allowed to attend exam because of medical case")
    else:
        print("You are not allowed to attend exam because of poor attendance")
else:
    print("Your percentage of class attended is:", str(perOfClassAttended), "% So you are allowed to attend exam")
