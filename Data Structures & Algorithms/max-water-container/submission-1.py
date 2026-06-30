class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        prod=0
        l,r=0,n-1
        while l<r:
            prod=max(prod,min(heights[l],heights[r])*abs(l-r))
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return prod

            

            

        