# 在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
# 你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
# 给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

class Solution:
    def maxValue(self, grid: list[list[int]]) -> int:
        # i=0
        # j=0
        # n=len(grid)
        # value=0
        # while i!=n-1 or j!=n-1:
        #     value+=grid[i][j]
        #     # print(i,j)
        #     if i==n-1:
        #         j+=1
        #     elif j==n-1:
        #         i+=1
        #     else:
        #         if grid[i+1][j] > grid[i][j+1]:
        #             i+=1
        #         else:
        #             j+=1
        # return value+grid[n-1][n-1]
        
        n_r=len(grid)
        n_c=len(grid[0])
        for i in range(n_r):
            for j in range(n_c):
                if i==0 and j==0:
                    pass
                elif i==0 and j!=0:
                    grid[i][j]+=grid[i][j-1]
                elif i!=0 and j==0:
                    grid[i][j]+=grid[i-1][j]
                else:
                    grid[i][j]+=max(grid[i-1][j],grid[i][j-1])
        return grid[n_r-1][n_c-1]
S=Solution()
print(S.maxValue([[1,2,5],[3,2,1]]))