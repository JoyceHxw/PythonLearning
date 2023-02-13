# 有一个只含有 'Q', 'W', 'E', 'R' 四种字符，且长度为 n 的字符串。
# 假如在该字符串中，这四个字符都恰好出现 n/4 次，那么它就是一个「平衡字符串」。
# 给你一个这样的字符串 s，请通过「替换一个子串」的方式，使原字符串 s 变成一个「平衡字符串」。
# 你可以用和「待替换子串」长度相同的 任何 其他字符串来完成替换。
# 请返回待替换子串的最小可能长度。
# 如果原字符串自身就是一个平衡字符串，则返回 0。

# 注意是连续子串
# class Solution:
#     def balancedString(self, s: str) -> int:
#         q=0
#         w=0
#         e=0
#         r=0
#         for l in s:
#             if l=='Q':
#                 q+=1
#             if l=='W':
#                 w+=1
#             if l=='E':
#                 e+=1
#             if l=='R':
#                 r+=1
#         lst=[]
#         lst.append(q)
#         lst.append(w)
#         lst.append(e)
#         lst.append(r)
#         print(lst)
#         lst.sort()
#         c=0
#         for n in lst:
#             if n>(len(s)/4):
#                 c+=int(n-len(s)/4)
#         return c

# 对于本题，设子串的左右端点为 left 和 right，枚举 right，
# 如果子串外的任意字符的出现次数都不超过 m，则说明从 left 到 right 的这段子串可以是待替换子串，
# 用其长度right−left+1 更新答案的最小值，并向右移动 left，缩小子串长度。

from cmath import inf
from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        cnt, m = Counter(s), len(s) // 4
        print(cnt)
        print(m)
        if all(cnt[x] == m for x in "QWER"):  # all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False
            return 0
        ans, left = inf, 0
        for right, c in enumerate(s):  # 枚举子串右端点
            cnt[c] -= 1
            print(all(cnt[x] <= m for x in "QWER"))
            while all(cnt[x] <= m for x in "QWER"):
                ans = min(ans, right - left + 1)
                print(right - left + 1)
                cnt[s[left]] += 1
                left += 1  # 缩小子串
                print("right=",right)
                print("left=",left)
        return ans


S=Solution()
print(S.balancedString("WWEQERQWQWWRWWERQWEQ"))