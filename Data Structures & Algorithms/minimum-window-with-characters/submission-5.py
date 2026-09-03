class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l=0
        tMap={}
        sMap={}
        have=0
        res=""

        for i in range(len(t)):
            tMap[t[i]]=1+tMap.get(t[i],0)

        need=len(tMap)

        for r in range(len(s)):
            sMap[s[r]]=1+sMap.get(s[r],0)
            if s[r] in tMap and tMap[s[r]]==sMap[s[r]]:
                have+=1
            while have==need:
                sMap[s[l]]=sMap.get(s[l],0)-1

                if s[l] in tMap and sMap[s[l]] < tMap[s[l]]:
                    have-=1
                if not res:
                    res=s[l:r+1]
                if len(res) > r-l+1:
                    res=s[l:r+1]
                l+=1

        return res




