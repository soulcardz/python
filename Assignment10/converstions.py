a = 75
def base10to2 (a):
    num = ""
    while (a > 0):
        num = str(a%2) + num
        a = int(a/2)
    return num


def base2to10 (a):
    num = 0
    i= len(a)
    place=0
    while (i > 0):
        num = int(a[i-1:i]) * (2 **(place)) + num
        #print (gggg + num)
        i =i-1
        place += 1
    return num
print ("Converting your number to base 2")
print(base10to2(a))
print ("Converting your number to base 10")
print(base2to10("1001011"))