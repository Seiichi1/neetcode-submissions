class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        l,r=0,0
        lst=[-1]*256
        max_len=0
        while r<n:
            if lst[ord(s[r])]!=-1:
                if lst[ord(s[r])]>=l:
                    l=lst[ord(s[r])]+1
            lst[ord(s[r])]=r
            max_len=max(max_len,r-l+1)
            print(l,r)
            r+=1
        return max_len
        