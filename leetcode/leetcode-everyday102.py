# 如果我们可以将小写字母插入模式串 pattern 得到待查询项 query，那么待查询项与给定模式串匹配。（我们可以在任何位置插入每个字符，也可以插入 0 个字符。）
# 给定待查询列表 queries，和模式串 pattern，返回由布尔值组成的答案列表 answer。只有在待查项 queries[i] 与模式串 pattern 匹配时， answer[i] 才为 true，否则为 false。

class Solution:
    def camelMatch(self, queries: list[str], pattern: str) -> list[bool]:
        # ans=[]
        # for word in queries:
        #     pos=[0]
        #     i=0
        #     isFlag=True
        #     for l in pattern:
        #         if word.find(l,i)!=-1:
        #             i=word.find(l,i)+1
        #             pos.append(i)
        #         else:
        #             isFlag=False
        #             break
        #     # 开头和中间是否有其他的大写字母
        #     # print(pos)
        #     for j in range(1,len(pos)):
        #         for k in range(pos[j-1],pos[j]-1):
        #             if word[k].isupper():
        #                 isFlag=False
        #                 break
        #     # 后面是否有大写字母
        #     for k in range(pos[-1],len(word)):
        #         if word[k].isupper():
        #             isFlag=False
        #             break
        #     ans.append(isFlag)
        # return ans

        # 双指针（字符串是按一定顺序排列的）
        n = len(queries)
        res = [True] * n
        for i in range(n):
            p = 0
            # 如果不相等，判断是否是大写字母
            for c in queries[i]:
                if p < len(pattern) and pattern[p] == c:
                    p += 1
                elif c.isupper():
                    res[i] = False
                    break
            # pattern中还有字符未被包含
            if p < len(pattern):
                res[i] = False
        return res

S=Solution()
print(S.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FB"))