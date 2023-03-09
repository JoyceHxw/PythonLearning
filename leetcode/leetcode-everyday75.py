# 给你一个长度为 n 下标从 0 开始的字符串 blocks ，blocks[i] 要么是 'W' 要么是 'B' ，表示第 i 块的颜色。字符 'W' 和 'B' 分别表示白色和黑色。
# 给你一个整数 k ，表示想要 连续 黑色块的数目。
# 每一次操作中，你可以选择一个白色块将它 涂成 黑色块。
# 请你返回至少出现 一次 连续 k 个黑色块的 最少 操作次数。

from cmath import inf


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # m=len(blocks)
        # for i in range(len(blocks)-k+1):
        #     cnt=0
        #     for i in range(i,i+k):
        #         if blocks[i]=="W":
        #             cnt+=1
        #     m=min(m,cnt)
        # return m

        # real滑动窗口
        ans = inf 
        cnt = 0 
        for i, ch in enumerate(blocks): 
            if ch == 'W':
                cnt += 1
            if i >= k and blocks[i-k] == 'W':
                cnt -= 1
            if i >= k - 1:
                ans = min(ans, cnt)
        return ans



S=Solution()
print(S.minimumRecolors("BWWWBB",6))
print(S.minimumRecolors("WWBBBWBBBBBWWBWWWB",16))