class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in hashMap:
                hashMap[s[i]]+=1
            else:
                hashMap[s[i]]=1
        print(hashMap)
        for i in range(len(t)):
            if t[i] in hashMap and hashMap[t[i]]>0:
                hashMap[t[i]]-=1
            else:
                return False
        return True
        