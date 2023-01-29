# 给你一个字符串 s ，每 两个 连续竖线 '|' 为 一对 。换言之，第一个和第二个 '|' 为一对，第三个和第四个 '|' 为一对，以此类推。
# 请你返回 不在 竖线对之间，s 中 '*' 的数目。
# 注意，每个竖线 '|' 都会 恰好 属于一个对。

class Solution:
    def countAsterisks(self, s: str) -> int:
        lst=s.split("|")
        i=0
        cnt=0
        while i<len(lst):
            cnt+=lst[i].count("*")
            i+=2
        return cnt

class Solution:
    def countAsterisks(self, s: str) -> int:
        valid = True
        res = 0
        for c in s:
            if c == '|':
                valid = not valid
            elif c == '*' and valid:
                res += 1
        return res
