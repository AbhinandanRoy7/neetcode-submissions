class Solution:
    def encode(self, strs: List[str]) -> str:
        w=''
        for word in strs:
            w+=str(len(word))+'#'+word
        return w
            

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            l=int(s[i:j])
            word=s[j+1:j+1+l]
            res.append(word)
            i=j+1+l
        return res
            


