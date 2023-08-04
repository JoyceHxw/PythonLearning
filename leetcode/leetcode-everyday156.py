# 在二维网格 grid 上，有 4 种类型的方格：
# 1 表示起始方格。且只有一个起始方格。
# 2 表示结束方格，且只有一个结束方格。
# 0 表示我们可以走过的空方格。
# -1 表示我们无法跨越的障碍。
# 返回在四个方向（上、下、左、右）上行走时，从起始方格到结束方格的不同路径的数目。
# 每一个无障碍方格都要通过一次，但是一条路径中不能重复通过同一个方格。

 
# 回溯，现在能很顺利地做出来了
class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        visit=[[0]*len(grid[0]) for _ in range(len(grid))]
        cnt=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==-1:
                    visit[i][j]=1
                elif grid[i][j]==1:
                    start_i=i
                    start_j=j
                    cnt+=1
                elif grid[i][j]==2:
                    end_i=i
                    end_j=j
                    cnt+=1
                else:
                    cnt+=1
        ans=0
        def recursion(i,j,cnt):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or visit[i][j]==1:
                return
            if i==end_i and j==end_j:
                if cnt==1:
                    print(111)
                    nonlocal ans
                    ans+=1
                    return
                else:
                    return
            cnt-=1
            visit[i][j]=1
            recursion(i+1,j,cnt)
            recursion(i-1,j,cnt)
            recursion(i,j+1,cnt)
            recursion(i,j-1,cnt)
            cnt+=1
            visit[i][j]=0
        recursion(start_i,start_j,cnt)
        return ans