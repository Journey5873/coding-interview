class MyQueue():
    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self,  x):
        self.inStack.append(x)
    
    def pop(self):
        if not self.outStack:
            for _ in range(len(self.inStack)):
                self.outStack.append(self.inStack.pop())
        return self.outStack.pop()
    
    def peek(self):
        if not self.outStack:
            for _ in range(len(self.inStack)):
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]
    
    def empty(self):
        if not self.inStack and not self.outStack:
            return True
        else:
            return False