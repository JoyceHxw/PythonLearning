# 给你两个整数 x 和 y ，表示你在一个笛卡尔坐标系下的 (x, y) 处。同时，在同一个坐标系下给你一个数组 points ，其中 points[i] = [ai, bi] 表示在 (ai, bi) 处有一个点。当一个点与你所在的位置有相同的 x 坐标或者相同的 y 坐标时，我们称这个点是 有效的 。
# 请返回距离你当前位置 曼哈顿距离 最近的 有效 点的下标（下标从 0 开始）。如果有多个最近的有效点，请返回下标 最小 的一个。如果没有有效点，请返回 -1 。
# 两个点 (x1, y1) 和 (x2, y2) 之间的 曼哈顿距离 为 abs(x1 - x2) + abs(y1 - y2) 。

from cmath import inf


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        # lst_x=[]
        # lst_y=[]
        # for n,p in enumerate(points):
        #     if p[0]==x:
        #         lst_x.append([abs(y-p[1]),n])

        #     if p[1]==y:
        #         lst_y.append([abs(x-p[0]),n])
        # x_m=min(map(lambda x:x[0], lst_x)) if lst_x!=[] else -1
        # y_m=min(map(lambda y:y[0], lst_y)) if lst_y!=[] else -1
        # print('x_m=',x_m)
        # print('y_m=',y_m)
        # x_p_m=min(map(lambda x:x[1],filter(lambda x:x[0]==x_m,lst_x))) if lst_x!=[] else -1
        # y_p_m=min(map(lambda y:y[1],filter(lambda y:y[0]==y_m,lst_y))) if lst_y!=[] else -1
        # print("x_p_m=",x_p_m)
        # print("y_p_m=",y_p_m)
        # x_m_n=list(map(lambda x:x[0], lst_x)).count(x_m)
        # y_m_n=list(map(lambda y:y[0], lst_y)).count(y_m)
        # print("x_m_n=",x_m_n)
        # print("y_m_n=",y_m_n)

        # if x_p_m!=-1 and y_p_m!=-1:
        #     return x_p_m if x_m<y_m else y_p_m if x_m>y_m else min(x_p_m,y_p_m)
        # if x_p_m!=-1 and y_p_m==-1:
        #     return x_p_m 
        # if x_p_m==-1 and y_p_m!=-1:
        #     return y_p_m 
        # if x_p_m==-1 and y_p_m==-1:
        #     return -1
        
        ans, mi = -1, inf
        for i, (a, b) in enumerate(points):
            if a == x or b == y:
                d = abs(a - x) + abs(b - y)
                if mi > d:
                    ans, mi = i, d
        return ans


S=Solution()
print(S.nearestValidPoint(3,4,[[2,3]]))
print(S.nearestValidPoint(3,4,[[1,2],[3,1],[2,4],[2,3],[4,4]]))
print(S.nearestValidPoint(3,4,[[3,4]]))
print(S.nearestValidPoint(1,1,[[1,2],[3,3],[3,3]]))