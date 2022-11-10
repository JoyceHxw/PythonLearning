# 在一个 n x n 的矩阵 grid 中，除了在数组 mines 中给出的元素为 0，其他每个元素都为 1。mines[i] = [xi, yi]表示 grid[xi][yi] == 0
# 返回  grid 中包含 1 的最大的 轴对齐 加号标志的阶数 。如果未找到加号标志，则返回 0 。
# 一个 k 阶由 1 组成的 “轴对称”加号标志 具有中心网格 grid[r][c] == 1 ，以及4个从中心向上、向下、向左、向右延伸，长度为 k-1，由 1 组成的臂。注意，只有加号标志的所有网格要求为 1 ，别的网格可能为 0 也可能为 1 。

# class Solution:
#     def orderOfLargestPlusSign(self, n: int, mines: list[list[int]]) -> int:
#         # matrix=[[1]*5]*5
#         dp = [[1] * n for _ in range(n)]
#         banned = set(map(tuple, mines))
#         num_all=[]
#         for x in banned:
#             r=x[0]
#             c=x[1]
#             dp[r][c]=0
#         # print(dp)
#         for i in range(n):
#             for j in range(n):
#                 print('i=',i,'j=',j)
#                 num=[]
#                 if dp[i][j]==1:
#                     cnt_right=1
#                     cnt_left=1
#                     cnt_up=1
#                     cnt_down=1
#                 else:
#                     cnt_right=0
#                     cnt_left=0
#                     cnt_up=0
#                     cnt_down=0
#                 # right
#                 print(cnt_right)
#                 print(cnt_left)
#                 print(cnt_up)
#                 print(cnt_down)

#                 is_right=True
#                 a=j+1
#                 while a<n and is_right==True:
#                     if dp[i][a]==1 and cnt_right<n-j:
#                         cnt_right+=1
#                         a+=1
#                         # print('cnt_right=',cnt_right)
#                     else:
#                         is_right=False
#                 print('right=',cnt_right)
#                 num.append(cnt_right)
#                 # down
#                 is_down=True
#                 b=i+1
#                 while b<n and is_down==True:
#                     if dp[b][j]==1 and cnt_down<n-i:
#                         cnt_down+=1
#                         b+=1
#                         # print('cnt_down=',cnt_down)
#                     else:
#                         is_down=False
#                 print('down=',cnt_down)
#                 num.append(cnt_down)
#                 # left
#                 is_left=True
#                 c=j-1
#                 while c>=-1 and is_left==True:
#                     if dp[i][c]==1 and cnt_left<j+1:
#                         cnt_left+=1
#                         c-=1
#                         # print('cnt_left=',cnt_left)
#                     else:
#                         is_left=False
#                 print('left=',cnt_left)
#                 num.append(cnt_left)
#                 # up
#                 is_up=True
#                 d=i-1
#                 while d>=-1 and is_up==True:
#                     if dp[d][j]==1 and cnt_up<i+1:
#                         cnt_up+=1
#                         d-=1
#                         # print('cnt_up=',cnt_up)
#                     else:
#                         is_up=False
#                 print('up=',cnt_up)
#                 num.append(cnt_up)
#                 print('num=',num)
#                 num_all.append(min(num))
#                 print('num_all=',num_all)
#         return max(num_all)


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: list[list[int]]) -> int:
        dp = [[n] * n for _ in range(n)]
        banned = set(map(tuple, mines))
        print(dp)
        print(banned)
        for i in range(n):
            # left
            count = 0
            for j in range(n):
                print('i=',i,'j=',j)
                count = 0 if (i, j) in banned else count + 1
                dp[i][j] = min(dp[i][j], count)
            # right
            print(dp)
            count = 0
            for j in range(n - 1, -1, -1):
                print('i=',i,'j=',j)
                count = 0 if (i, j) in banned else count + 1
                dp[i][j] = min(dp[i][j], count)
            print(dp)
        print(dp)
        for j in range(n):
            # up
            count = 0
            for i in range(n):
                count = 0 if (i, j) in banned else count + 1
                dp[i][j] = min(dp[i][j], count)
            # down
            count = 0
            for i in range(n - 1, -1, -1):
                count = 0 if (i, j) in banned else count + 1
                dp[i][j] = min(dp[i][j], count)
        print(dp)
        return max(map(max, dp))

S=Solution()
S.orderOfLargestPlusSign(3,[[0,0]])