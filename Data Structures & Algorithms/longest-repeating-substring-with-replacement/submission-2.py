class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        l,r=0,0
        max_f,max_len=0,0
        hash_l=[0]*26
        while r<n:
            hash_l[ord(s[r])-ord('A')]+=1
            max_f=max(max_f,hash_l[ord(s[r])-ord('A')])
            if (r-l+1)-max_f>k:
                hash_l[ord(s[l])-ord('A')]-=1
                max_f=0
                l+=1
            if (r-l+1)-max_f<=k:
                max_len=max(max_len,r-l+1)
            r+=1
        return max_len



                    
                
        