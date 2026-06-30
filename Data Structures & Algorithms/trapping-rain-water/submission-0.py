class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        ar=0
        prefix=[0]*n
        prefix[0]=0
        suffix=[0]*n
        suffix[n-1]=0
        max_n=0
        for i in range(1,n):
            max_n=max(max_n,height[i-1])
            prefix[i]=max_n
        
        max_n=0
        for i in range(n-2,-1,-1):
            max_n=max(max_n,height[i+1])
            suffix[i]=max_n
        
        #print(prefix)
        #print(suffix)
            
            
        for i in range(n):
            #print(i)
            ar_n=min(prefix[i],suffix[i])-height[i]
            if ar_n<0:
                ar_n=0
            ar=ar+ar_n
        return ar
            

            
        