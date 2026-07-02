class MinStack:

    def __init__(self):
        self.items=[]
        self.min_stack=[]


    def push(self, val: int) -> None:
        self.items.append(val)
        if len(self.min_stack)==0 or val<=self.min_stack[-1]:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        if len(self.items)==0:
            return "Can't pop an empty stack"
        x=self.items.pop()
        if x==self.min_stack[-1]:
            self.min_stack.pop()
        return x
        

    def top(self) -> int:
        if len(self.items)==0:
            return "Can't return an empty stack"
        return self.items[-1]
        
        

    def getMin(self) -> int:
        return self.min_stack[-1]

        
