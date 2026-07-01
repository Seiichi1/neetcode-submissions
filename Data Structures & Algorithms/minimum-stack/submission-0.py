class MinStack:

    def __init__(self):
        self.items=[]

    def push(self, val: int) -> None:
        return self.items.append(val)
        

    def pop(self) -> None:
        if len(self.items)==0:
            return "Can't pop an empty stack"
        x=self.items.pop()
        return x
        

    def top(self) -> int:
        if len(self.items)==0:
            return "Can't return an empty stack"
        return self.items[-1]
        
        

    def getMin(self) -> int:
        if len(self.items)==0:
            return "Can't return an empty stack"
        return min(self.items)

        
