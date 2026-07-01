class Stack:
    def __init__(self):
        self.items=[]
  
    def is_empty(self):
        return len(self.items)==0
  
    def pop(self):
        if len(self.items)==0:
            return "Can't return, when stack is empty"
        x=self.items.pop()
        return x
  
    def push(self,x):
        return self.items.append(x)
  
    def top(self):
        if len(self.items)==0:
            return "Can't return, when stack is empty"
        return self.items[-1]
    def size(self):
        return len(self.items)


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=Stack()
        for ele in tokens:
            #print(ele)
            if ele=="+":
                stack.push(int(stack.pop())+int(stack.pop()))
            elif ele=="-":
                stack.push(-1*(int(stack.pop())-int(stack.pop())))
            elif ele=="*":
                stack.push(int(stack.pop())*int(stack.pop()))
            elif ele=="/":
                a,b=int(stack.pop()),int(stack.pop())
                stack.push(int(b/a))
            else:
                stack.push(ele)
            #print(stack.top())
            print(stack.items)
        return int(stack.top())
        
        
        