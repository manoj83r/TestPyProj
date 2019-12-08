pos = 0


def search(list2, s1):
    for i in list2:
        globals() ['pos'] += 1
        if s1 == i:
            return True
    return False


list1 = [34, 56, 44, 21, 8, 4, 87, 36]
s = 8
if search(list1, s):
    print("Value Found at " + str(pos))
else:
    print("Value Not Found")
