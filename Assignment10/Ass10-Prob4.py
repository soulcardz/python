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


def base10to2 (a):
    myStack = Stack()
    while (a > 0):
        myStack.push(str(a%2))
        a = int(a/2)
    num = ""
    while (not myStack.is_empty()):
        num = num + myStack.pop()
    return num
print ("Your number in base 2 is :")
print(base10to2(75))

