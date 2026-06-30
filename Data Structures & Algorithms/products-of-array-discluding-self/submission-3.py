class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]
        suffix=[1]*len(nums)
        prod=1
        for i in range(len(nums)-1):
            prod*=nums[i]
            prefix.append(prod)
        prod=1
        for i in range(len(nums)-1,-1,-1):
            suffix[i]=prod
            prod*=nums[i]

        print(prefix)
        print(suffix)
        ans=[]
        for i in range(len(nums)):
            ans.append(prefix[i]*suffix[i])

        return ans



        

            

        