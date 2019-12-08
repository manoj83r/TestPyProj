x = 2
y = 5
z = 0
if x == 2:
    print("Inside if loop and condition x == 2 is true")
else:
    print("Inside else loop and condition x == 2 is false")

if x != 5:
    print("Inside if loop and condition x != 5 is true")
else:
    print("Inside else loop and condition x != 5 is false")

if x != 5 and y >= 5 :
    print("Inside if loop and condition x != 5 and y >= 5 is true")
else:
    print("Inside else loop and condition x != 5 and y >= 5 is false")

if z != 0 or x == 2:
    print("Inside if loop and condition z != 0 or x == 2 is true")
else:
    print("Inside else loop and condition z != 0 or x == 2 is false")

if not (y < 10):
    print("Inside if loop and condition !(y < 10) is true")
else:
    print("Inside else loop and condition !(y < 10) is false")