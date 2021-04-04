correctlis = [5,7,12,50]
wronglis = [5,2,3,1,5000]

def orglist (a):
    length = len(a)
    i = 0
    b = 1
    flag = True
    while i < (length - 1) :
        b = i + 1
        if a[i] > a[b]:
            flag = False
            break
        i = i+1
    return flag

g = orglist(correctlis) 
f = orglist(wronglis)
print (g)
print (f)