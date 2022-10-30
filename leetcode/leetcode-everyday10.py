def letterCasePermutation(s):
    result=[]
    s=list(s)
    def recursion(s,i):
        while i<len(s) and s[i].isdigit()==True:
            i+=1
        if i==len(s):
            s_new=''.join(s)
            print("添加...")
            print(s_new)
            result.append(s_new)
            return
        print(i)

# 递归语句前的代码是按由外到内的顺序执行的
        recursion(s,i+1)
# 位于递归语句后的代码是按由内到外的顺序执行的
        print(i)
        s[i]=s[i].swapcase() 
        print(s)

        recursion(s,i+1)
        s[i]=s[i].swapcase()
        print(s)
    
    recursion(s,0)
    return result

print(letterCasePermutation('a1b2C'))