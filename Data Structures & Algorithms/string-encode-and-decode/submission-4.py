class Solution:

    def encode(self, strs: List[str]) -> str:
        string=""
        for s in strs:
            string=string+str(len(s))+"#"+s
        print(string)
        return string

    def decode(self, s: str) -> List[str]:
        strs=[]
        pos=0
        for i in range(len(s)):
            if s[i]=='#':
                if s[i-1].isdigit():
                    num=int(s[pos:i])
                    strs.append(s[i+1:num+i+1])
                    pos=num+i+1
        return strs
