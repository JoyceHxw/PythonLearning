# 你有一套活字字模 tiles，其中每个字模上都刻有一个字母 tiles[i]。返回你可以印出的非空字母序列的数目。
# 注意：本题中，每个活字字模只能使用一次。

from collections import Counter

# 回溯，注意递归函数有返回值如何使用
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)
        tile = set(tiles)

        def dfs(i):
            if i == 0:
                return 1
            res = 1
            for t in tile:
                if count[t] > 0:
                    count[t] -= 1
                    res += dfs(i - 1)
                    count[t] += 1
            return res

        return dfs(len(tiles)) - 1
S=Solution()
print(S.numTilePossibilities("AAB"))