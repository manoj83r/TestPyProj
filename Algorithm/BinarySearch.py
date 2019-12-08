pos = 0


def search(list2, s1):
    lb = 0
    ub = len(list2)
    while lb<=ub :
        mb = (lb+ub) // 2
        if list2[mb] == s1:
            globals()['pos'] = mb
            return True
        elif list2[mb] > s1:
            ub = mb -1
        else:
            ub = mb +1
    return False


list1 = [34, 56, 44, 21, 8, 4, 87, 36]
list1.sort(reverse=False)
s = 8
if search(list1, s):
    print("Value Found at " + str(pos+1))
else:
    print("Value Not Found")
