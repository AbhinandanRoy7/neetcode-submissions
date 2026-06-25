class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        closetoOpen={
            ')':'(',
            '}':'{',
            ']':'['
        }
        for c in s:
            if c in closetoOpen:
                if st and st[-1]==closetoOpen[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)
        return True if not st else False


            
        