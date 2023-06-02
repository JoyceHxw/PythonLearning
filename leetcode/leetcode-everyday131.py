from itertools import accumulate


class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        # 超时
        # letters=['a','e','i','o','u']
        # isflag=[]
        # for word in words:
        #     if word[0] in letters and word[-1] in letters:
        #         isflag.append(1)
        #     else:
        #         isflag.append(0)
        # ans=[]
        # for l,r in queries:
        #     cnt=sum(isflag[l:r+1])
        #     ans.append(cnt)
        # return ans

        # 前缀和，提前处理
        letters=['a','e','i','o','u']
        isflag=[]
        for word in words:
            if word[0] in letters and word[-1] in letters:
                isflag.append(1)
            else:
                isflag.append(0)
        acc= list(accumulate(isflag, initial=0))
        ans=[]
        for l,r in queries:
            cnt=acc[r]-acc[l]
            ans.append(cnt)
        return ans