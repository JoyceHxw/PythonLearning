# 给你一个下标从 0 开始的字符串 word ，字符串只包含小写英文字母。你需要选择 一个 下标并 删除 下标处的字符，使得 word 中剩余每个字母出现 频率 相同。
# 如果删除一个字母后，word 中剩余所有字母的出现频率都相同，那么返回 true ，否则返回 false 。
# 注意：
# 字母 x 的 频率 是这个字母在字符串中出现的次数。
# 你 必须 恰好删除一个字母，不能一个字母都不删除。

# 分类讨论
from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        # 哈希表
        f=Counter(word)
        d={}
        print(f)
        for x,y in f.items():
            a=d.get(y,-1)
            if a!=-1:
                d[y]+=1
            else:
                d[y]=1
        l=list(d.items())
        l.sort(key=lambda x: x[0])
        print(l)
        num=0
        if len(l)==2 and ((l[1][0]-l[0][0]==1 and l[1][1]==1) or(l[0][0]==l[0][1]==1)):
            return True
        if len(l)==1 and (l[0][0]==1 or l[0][1]==1):
            return True
        return False

# 枚举被删除的字符  
class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):  # 枚举删除的字符
            cnt = Counter(word[:i] + word[i + 1:])  # 统计出现次数
            if len(set(cnt.values())) == 1:  # 出现次数都一样
                return True
        return False
