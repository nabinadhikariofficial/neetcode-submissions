class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp=[]
        for i in range(len(s)):
            temp.append(s[i])
        for j in range(len(t)):
            if t[j] in temp:
                temp.remove(t[j])
        return len(temp) ==0 and i==j
