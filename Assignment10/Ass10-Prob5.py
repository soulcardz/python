class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)             

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items

def remdup (a):
    if (len(a) == 1):
        return a
    if (len(a) == 2):
        if (a[0 : 1] == a[1 : 2]):
            return ""
        else:
            return a
    myStack = Stack()
    sss = a
    while(True):
        flag = 0
        index = 0
        while index < (len(sss) -1 ):
            if (sss[index] == sss[index + 1]):
                index = index + 1
                flag = 1
            else:
                myStack.push(sss[index])
            index += 1
        if (index == (len(sss) - 1)):
            myStack.push(sss[index])
        if (flag == 1):
            sss = ""
            while (not myStack.is_empty()):
                sss = myStack.pop() + sss
        else:
            break
    return sss


strrr= "abbacaa"
print(remdup(strrr))