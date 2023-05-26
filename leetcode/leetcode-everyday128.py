from cmath import inf
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        # dfs超时
        # ans=-1
        # temp=inf
        # n=len(grid)
        # visit=[[0]*n for _ in range(n)]
        # print(visit)
        # def dfs(grid: list[list[int]], x: int, y: int, steps: int,visit:list[list[int]]):
        #     nonlocal ans
        #     nonlocal temp
        #     # 成功到达
        #     if x==len(grid)-1 and y==len(grid)-1 and grid[x][y]==0:
        #         steps+=1
        #         temp=min(steps,temp)
        #         return temp
        #     # 剪枝：越界的，不通的，已走过的
        #     if x<0 or x>=len(grid) or y<0 or y>=len(grid) or grid[x][y]==1 or visit[x][y]==1:
        #         return -1
        #     # 递归
        #     # 不能往回走
        #     visit[x][y]=1
        #     dfs(grid,x+1,y,steps+1,visit)
        #     dfs(grid,x-1,y,steps+1,visit)
        #     dfs(grid,x,y+1,steps+1,visit)
        #     dfs(grid,x,y-1,steps+1,visit)
        #     dfs(grid,x+1,y+1,steps+1,visit)
        #     dfs(grid,x+1,y-1,steps+1,visit)
        #     dfs(grid,x-1,y+1,steps+1,visit)
        #     dfs(grid,x-1,y-1,steps+1,visit)
        #     # 退回上一步
        #     visit[x][y]=0
        #     return temp
        # dfs(grid,0,0,0,visit)
        # if temp!=inf:
        #     ans=temp
        # return ans

        # BFS
        if grid[0][0]:
            return -1
        n = len(grid)
        grid[0][0] = 1
        q = deque([(0, 0)])
        ans = 1
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if i == j == n - 1:
                    return ans
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                            grid[x][y] = 1
                            q.append((x, y))
            ans += 1
        return -1

S=Solution()
print(S.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))