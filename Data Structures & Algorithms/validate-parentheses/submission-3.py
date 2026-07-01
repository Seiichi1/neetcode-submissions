class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        if len(self.items)==0:
            return "Can't pop, when stack is empty"
        x=self.items.pop()
        return x
    def top(self):
        if len(self.items)==0:
            return "Can't return top element, when stack is empty"
        return self.items[-1]
    def is_empty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)

class Solution:
    def isValid(self, s: str) -> bool:
        bracket={"{":"}","[":"]","(":")"}
        stack=Stack()
        if len(s)==1:
            return False
        for c in s:
            if c in bracket.keys():
                stack.push(c)
            if c in bracket.values():
                if stack.is_empty():
                    return False
                if bracket[stack.top()]==c:
                    stack.pop()
                else:
                    return False
        


        return stack.is_empty()

        