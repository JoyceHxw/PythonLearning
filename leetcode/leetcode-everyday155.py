# 给一个 C++ 程序，删除程序中的注释。这个程序source是一个数组，其中source[i]表示第 i 行源码。 这表示每行源码由 '\n' 分隔。
# 在 C++ 中有两种注释风格，行内注释和块注释。
# 字符串// 表示行注释，表示//和其右侧的其余字符应该被忽略。
# 字符串/* 表示一个块注释，它表示直到下一个（非重叠）出现的*/之间的所有字符都应该被忽略。（阅读顺序为从左到右）非重叠是指，字符串/*/并没有结束块注释，因为注释的结尾与开头相重叠。

# 模拟，分类讨论
# 注意情况考虑全面
# 优化考虑正则表达式
class Solution:
    def removeComments(self, source: list[str]) -> list[str]:
        ans=[]
        block=[]
        temp=""
        for string in source:
            i=0
            # 分为两类大情况，再细分
            while i<len(string):
                if string[i]!='/':
                    if len(block)==0:
                        temp+=string[i]
                        i+=1
                    elif i+1<len(string) and string[i]=='*' and string[i+1]=='/':
                        block.pop()
                        i+=2
                    else:
                        i+=1
                else:
                    if i+1<len(string) and string[i+1]=='/' and len(block)==0:
                        break
                    elif i+1<len(string) and string[i+1]=='*' and len(block)==0:
                        block.append(1)
                        i+=2
                    elif len(block)==0:
                        temp+=string[i]
                        i+=1
                    else:
                        i+=1
            if len(temp)>0 and len(block)==0:
                ans.append(temp)
                temp=""
        return ans 

S=Solution()
S.removeComments(["main() {", "/* here is commments", "  // still comments */", "   double s = 33;", "   cout << s;", "}"])