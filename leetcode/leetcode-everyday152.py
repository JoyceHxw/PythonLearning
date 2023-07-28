from collections import defaultdict, deque


class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        # # 构建邻接矩阵，不需要关键路径
        # matrix=[[0]*(n+1) for _ in range(n+1)]
        # 优化：邻接表
        g=defaultdict(list)
        # 各节点的入度
        indegree=[0]*(n+1)
        # 最早结束时间
        ee=[0]*(n+1)
        for _,(x,y) in enumerate(relations):
            indegree[y]+=1
            g[x].append(y)
        # print(indegree)
        q=deque()
        # print(ee)
        ans=0
        for i in range(1,n+1):
            ee[i]=time[i-1]
            ans=max(ans,ee[i])
            if indegree[i]==0:
                q.append(i)
        while q:
            t=q.popleft()
            for y in g[t]:
                indegree[y]-=1
                if indegree[y]==0:
                    q.append(y)
                ee[y]=max(ee[t]+time[y-1],ee[y])
                ans=max(ee[y],ans)
        # print(ee)
        # print(q)
        return ans

S=Solution()
print(S.minimumTime(9,[[3,2],[3,1],[1,7],[2,7],[4,6],[2,9],[3,9],[4,9],[6,9],[8,9]],[3,5,7,1,8,2,5,7,4]))