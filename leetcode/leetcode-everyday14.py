class Solution:
    def interpret(self, command: str) -> str:
        lst=list(command)
        lst1=[]
        for i in range(0,len(lst)):
            if lst[i]=="G":
                lst1.append("G")
            elif lst[i]=="(":
                if lst[i+1]==")":
                    lst1.append("o")
                if lst[i+1]=="a" and lst[i+2]=="l" and lst[i+3]==")":
                    lst1.append("al")
            else:
                pass
        s=''.join(lst1)
        return s

S=Solution()
print(S.interpret("G()(al)"))