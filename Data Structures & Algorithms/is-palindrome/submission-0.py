class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerstr = ''
        for i in s:
            if i.isalnum():
                lowerstr+= i.lower()
        if lowerstr == lowerstr[::-1]:
            return True
        else:
            return False