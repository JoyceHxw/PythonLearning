# 机器人在一个无限大小的 XY 网格平面上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令 commands ：
# -2 ：向左转 90 度
# -1 ：向右转 90 度
# 1 <= x <= 9 ：向前移动 x 个单位长度
# 在网格上有一些格子被视为障碍物 obstacles 。第 i 个障碍物位于网格点  obstacles[i] = (xi, yi) 。
# 机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续尝试进行该路线的其余部分。
# 返回从原点到机器人所有经过的路径点（坐标为整数）的最大欧式距离的平方。（即，如果距离为 5 ，则返回 25 ）

class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        # # 模拟，一步一步考虑，超出时间限制
        # # 起始原点
        # p=[0,0]
        # # 哈希表提高查询速度
        # mp = set([tuple(i) for i in obstacles])
        # # 返回所有路径点的最大距离
        # distance=0
        # # 右转加一，左转减一，求4的余数
        # direction=0
        # for c in commands:
        #     if c>0:
        #         i=0
        #         if direction%4==0:
        #             while i<c:
        #                 if tuple([p[0],p[1]+1]) in mp:
        #                     break
        #                 else:
        #                     p[1]+=1
        #                     i+=1
        #                     distance=max(distance,p[0]**2+p[1]**2)
        #         elif direction%4==1:
        #             while i<c:
        #                 if tuple([p[0]+1,p[1]]) in mp:
        #                     break
        #                 else:
        #                     p[0]+=1
        #                     i+=1
        #                     distance=max(distance,p[0]**2+p[1]**2)
        #         elif direction%4==2:
        #             while i<c:
        #                 if tuple([p[0],p[1]-1]) in mp:
        #                     break
        #                 else:
        #                     p[1]-=1
        #                     i+=1
        #                     distance=max(distance,p[0]**2+p[1]**2)
        #         else:
        #             while i<c:
        #                 if tuple([p[0]-1,p[1]]) in mp:
        #                     break
        #                 else:
        #                     p[0]-=1
        #                     i+=1
        #                     distance=max(distance,p[0]**2+p[1]**2)
        #     elif c==-1:
        #         direction+=1
        #     else:
        #         direction-=1
        # return distance

        # 代码简化
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        px, py, d = 0, 0, 1
        mp = set([tuple(i) for i in obstacles])
        res = 0
        for c in commands:
            if c < 0:
                d += 1 if c == -1 else -1
                d %= 4
            else:
                for i in range(c):
                    if tuple([px + dirs[d][0], py + dirs[d][1]]) in mp:
                        break
                    px, py = px + dirs[d][0], py + dirs[d][1]
                    res = max(res, px * px + py * py)
        return res

