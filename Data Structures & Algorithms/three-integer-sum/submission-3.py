class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted=sorted(nums)
        nums=nums_sorted
        n=len(nums)
        triplet=[]
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            num=nums[i]
            target=num*-1
            l,r=i+1,n-1
            while(l<r):
                sm=nums[l]+nums[r]
                if sm==target:
                    triplet.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                elif sm<target:
                    l+=1
                else:
                    r-=1
        return triplet
            


             

        