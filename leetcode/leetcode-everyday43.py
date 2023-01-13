# 给你两个下标从 0 开始的字符串 s 和 target 。你可以从 s 取出一些字符并将其重排，得到若干新的字符串。
# 从 s 中取出字符并重新排列，返回可以形成 target 的 最大 副本数。


# class Solution:
#     def rearrangeCharacters(self, s: str, target: str) -> int:
#         s=list(s)
#         cnt=0
#         is_flag=True
#         while is_flag:
#             for l in target:
#                 if l in s:
#                     s.remove(l)
#                 else:
#                     is_flag=False
#                     break
#             cnt+=1
#         return cnt-1


# 这道题要求计算使用 s 中的字符可以形成的 target 的最大副本数，因此需要统计 target 中的每个字符的出现次数，以及统计这些字符在 s 中的出现次数。
# 如果一个字符在 target 中出现 x 次（x > 0），在 s 中出现 y 次，则在只考虑该字符的情况下，可以形成的 target 的最大副本数是 [y/x]。特别地，如果 y < x，则不能形成 target 的副本。

# 有两处可以优化。
# 由于只有在 target 中出现的字符才会影响最大副本数，因此统计 s 中的每个字符的出现次数时，只需要考虑在target 中出现的字符，忽略没有在 target 中出现的字符。
# 如果遇到一个在 target 中出现的字符对应的最大副本数是 0，则不能使用 s 中的字符形成target 的副本，此时可提前返回 0。
from collections import Counter
from math import inf


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        ans = inf
        cnt_s = Counter(s)
        for c, cnt in Counter(target).items():
            ans = min(ans, cnt_s[c] // cnt)
            if ans == 0:
                return 0
        return ans
