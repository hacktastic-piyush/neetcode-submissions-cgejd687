class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        dic2 = {}
        for i in s:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        for j in t:
            if j in dic2:
                dic2[j] +=1
            else:
                dic2[j] = 1
        if dic == dic2:
            return True
        else:
            return False

            