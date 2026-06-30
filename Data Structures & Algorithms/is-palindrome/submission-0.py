class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new=s.lower()
        s_new=[s for s in s_new if s.isalnum()]
        print(s_new)
        return s_new==s_new[::-1]
        