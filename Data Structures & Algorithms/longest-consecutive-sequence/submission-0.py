class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        max_len=0
        for num in nums_set:
            count=1
            ele=num
            if num-1 not in nums_set:
                while(ele+1 in nums_set):
                    count+=1
                    ele+=1
            max_len=max(max_len,count)
        return max_len

                
        