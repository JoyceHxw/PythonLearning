# 在一个有向图中，节点分别标记为 0, 1, ..., n-1。图中每条边为红色或者蓝色，且存在自环或平行边。
# red_edges 中的每一个 [i, j] 对表示从节点 i 到节点 j 的红色有向边。类似地，blue_edges 中的每一个 [i, j] 对表示从节点 i 到节点 j 的蓝色有向边。
# 返回长度为 n 的数组 answer，其中 answer[X] 是从节点 0 到节点 X 的红色边和蓝色边交替出现的最短路径的长度。如果不存在这样的路径，那么 answer[x] = -1。


# 广度优先搜索
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        g = [[] for _ in range(n)]
        for x, y in redEdges:
            g[x].append((y, 0))    # 到点y的红色边
        print(g)
        for x, y in blueEdges:
            g[x].append((y, 1))    # 到点y的蓝色边
        print(g)

        dis = [-1] * n   # 用来存储每个节点到起点的最短距离。初始时所有元素初始化为 −1，表示所有节点到起点的距离都未知。
        vis = {(0, 0), (0, 1)}    # 用来存储已经搜索过的节点，以及当前边的颜色；
        q = [(0, 0), (0, 1)]    # 用来存储当前搜索到的节点，以及当前边的颜色；
        level = 0   # 用来表示当前搜索的层数，即当前搜索到的节点到起点的距离；
        while q:
            tmp = q
            q = []
            for x, color in tmp:
                print("x=",x)
                print("color=",color)
                if dis[x] == -1:
                    dis[x] = level
                print("dis=",dis)
                for p in g[x]:
                    print("p=",p)
                    if p[1] != color and p not in vis:   # 如果颜色不同，且没有遍历过
                        vis.add(p)
                        q.append(p)
            print("q=",q)
            level += 1
        print(vis)
        return dis

S=Solution()
print(S.shortestAlternatingPaths(3,[[0,1],[0,2]],[[1,0]]))