# 这里有一幅服务器分布图，服务器的位置标识在 m * n 的整数矩阵网格 grid 中，1 表示单元格上有服务器，0 表示没有。
# 如果两台服务器位于同一行或者同一列，我们就认为它们之间可以进行通信。
# 请你统计并返回能够与至少一台其他服务器进行通信的服务器的数量。

# 思路很直接
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        rows=[0]*m
        columns=[0]*n
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    rows[i]+=1
                    columns[j]+=1
        ans=0
        for i in range(m):
            if rows[i]>1:
                ans+=rows[i]
        for j in range(n):
            if columns[j]>1:
                ans+=columns[j]
        for i in range(m):
            for j in range(n):
                if rows[i]>1 and columns[j]>1 and grid[i][j]==1:
                    ans-=1
        return ans