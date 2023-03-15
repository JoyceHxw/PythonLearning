class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        # h={}
        # for road in roads:
        #     for city in road:
        #         if h.get(city,-1)==-1:
        #             h[city]=1
        #         else:
        #             h[city]+=1
        # print(h)
        # h_s=sorted(h.items(),key= lambda x:x[1],reverse=True)
        # print(h_s)
        # # print(h.keys())
        # m=0
        # for key1 in h.keys():
        #     for key2 in h.keys():
        #         if key1<key2:
        #             if [key1,key2]in roads or [key2,key1] in roads:
        #                 m=max(m,h[key1]+h[key2]-1)
        #             else:
        #                 m=max(m,h[key1]+h[key2])   
        #             # print(m)
        # return m

        # 每对城市之间是否有道路相连
        g = [[0] * n for _ in range(n)]
        # 每个城市的度
        cnt = [0] * n
        print(g)
        print(cnt)
        for a, b in roads:
            print(a)
            print(b)
            g[a][b] = g[b][a] = 1
            cnt[a] += 1
            cnt[b] += 1
        print(g)
        print(cnt)
        return max(cnt[a] + cnt[b] - g[a][b] for a in range(n) for b in range(a + 1, n))


S=Solution()
# S.maximalNetworkRank(4,[[0,1],[0,3],[1,2],[1,3]])
print(S.maximalNetworkRank(8,[[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]))