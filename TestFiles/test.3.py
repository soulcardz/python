def prime (a,b):
    lis = []
    if a < 0:
        return lis
    if a > b :
        return lis
    while a <= b:
        if a == 2:
            lis.append(a)
            a = a + 1    
            continue
        if a % 2 == 0:
            a = a + 1
            continue
        i = 3
        primeNum = True
        while i < a/2:
            if a % i == 0:
                primeNum = False
                break
            i = i + 2
        if primeNum == True:
            lis.append(a)
        a = a + 1
    return lis

print (prime(1,25))
