class Solution:

    def encode(self, strs: List[str]) -> str:
        string=""
        for s in strs:
            string=string+str(len(s))+"#"+s
        return string

    def decode(self, s: str) -> List[str]:
        strs=[]
        i=0

        while i< len(s):
            j=i
            while s[j] !='#':
                j+=1
            length=int(s[i:j])
            i=j+1
            j=i+length
            strs.append(s[i:j])
            i=j

        # for i in range(len(s)):
        #     if s[i]=='#':
        #         if s[i-1].isdigit():
        #             num=int(s[pos:i])
        #             strs.append(s[i+1:num+i+1])
        #             pos=num+i+1
        return strs
