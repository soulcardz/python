str = 'python quiz practice code'

def opstr (a):
    lis = ""
    c = a.split()
    b = len(c) - 1 
    lis = lis + c[b]
    while b > 0:
        lis = lis + " " + c[b - 1]
        b = b - 1
    return lis
    
print (opstr(str))
