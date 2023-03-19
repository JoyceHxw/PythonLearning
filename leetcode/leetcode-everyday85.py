# 给你一个字符串 s 以及两个整数 a 和 b 。其中，字符串 s 的长度为偶数，且仅由数字 0 到 9 组成。
# 你可以在 s 上按任意顺序多次执行下面两个操作之一：
# 累加：将  a 加到 s 中所有下标为奇数的元素上（下标从 0 开始）。数字一旦超过 9 就会变成 0，如此循环往复。例如，s = "3456" 且 a = 5，则执行此操作后 s 变成 "3951"。
# 轮转：将 s 向右轮转 b 位。例如，s = "3456" 且 b = 1，则执行此操作后 s 变成 "6345"。
# 请你返回在 s 上执行上述操作任意次后可以得到的 字典序最小 的字符串。
# 如果两个字符串长度相同，那么字符串 a 字典序比字符串 b 小可以这样定义：在 a 和 b 出现不同的第一个位置上，字符串 a 中的字符出现在字母表中的时间早于 b 中的对应字符。例如，"0158” 字典序比 "0190" 小，因为不同的第一个位置是在第三个字符，显然 '5' 出现在 '9' 之前。


# 注意队列和字符串的操作
from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        q = deque([s])
        vis = {s}
        ans = s
        while q:  # 说明还存在操作之后更小的数
            print(q)
            s = q.popleft()
            print(s)
            if ans > s:
                ans = s
            t1 = ''.join([str((int(c) + a) % 10) if i & 1 else c for i, c in enumerate(s)])
            t2 = s[-b:] + s[:-b]
            print("t1=",t1)
            print("t2=",t2)
            for t in (t1, t2):
                if t not in vis:
                    vis.add(t)
                    q.append(t)
        return ans
    
S=Solution()
S.findLexSmallestString("5525",9,2)
