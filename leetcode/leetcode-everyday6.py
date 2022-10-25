
from collections import deque


def shortestBridge(grid) -> int:
    # # 标记第一个岛
    # island=[]
    # for i in range(0,len(grid)):
    #     for j in range(0,len(grid[i])):
    #         if grid[i][j]!=1:
    #             continue
    #         else:
    #             grid[i][j]=2
    #             island.append([i,j])
    #             for ni, nj in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
    #                 if 0 <= ni < len(grid) and 0 <= nj < len(grid) and grid[ni][nj]==0:
    #                     break
    #                 else:
    #                     pass
    # # 向外扩展
    # s=0
    # is_flag=True
    # while is_flag==True:
    #     s+=1
    #     print(s)
    #     for [i,j] in island:
    #         temp=[]
    #         for ni, nj in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
    #             if 0 <= ni < len(grid) and 0 <= nj < len(grid):
    #                 if grid[ni][nj]==0:
    #                     grid[ni][nj]=2
    #                     temp.append([ni,nj])  
    #                 if grid[ni][nj]==1:
    #                     break
    #     island=island+temp
    #     print(island)
    #     print("after",grid)
    #     is_flag=False                      
    # return s

    # return 跳出所有循环，但对于两层以上的循环不适用
    
    n = len(grid)
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            if v != 1:
                continue
            island = []
            grid[i][j] = -1
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                island.append((x, y))
                for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = -1
                        q.append((nx, ny))

            step = 0
            q = island
            while True:
                tmp = q
                q = []
                for x, y in tmp:
                    for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                        if 0 <= nx < n and 0 <= ny < n:
                            if grid[nx][ny] == 1:
                                return step
                            if grid[nx][ny] == 0:
                                grid[nx][ny] = -1
                                q.append((nx, ny))
                step += 1


print(shortestBridge([[0,1,0],[0,0,0],[0,0,1]]))
