class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        storeSet=set()
        r=0
        res=0
        current=0
        for i in range(len(s)):
            while s[i] in storeSet:
                storeSet.remove(s[r])
                r+=1
            storeSet.add(s[i])
            res=max(res,i-r+1)   
        return res