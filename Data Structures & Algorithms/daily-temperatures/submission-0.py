class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack=[]
        ans=[0]*n
        for i in range(n):
            while len(stack)!=0 and temperatures[i]>temperatures[stack[-1]]:
                prev=stack.pop()
                ans[prev]=abs(prev-i)
            stack.append(i)
        return ans
                    
                    





        