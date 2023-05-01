# 公司里有 n 名员工，每个员工的 ID 都是独一无二的，编号从 0 到 n - 1。公司的总负责人通过 headID 进行标识。
# 在 manager 数组中，每个员工都有一个直属负责人，其中 manager[i] 是第 i 名员工的直属负责人。对于总负责人，manager[headID] = -1。题目保证从属关系可以用树结构显示。
# 公司总负责人想要向公司所有员工通告一条紧急消息。他将会首先通知他的直属下属们，然后由这些下属通知他们的下属，直到所有的员工都得知这条紧急消息。
# 第 i 名员工需要 informTime[i] 分钟来通知它的所有直属下属（也就是说在 informTime[i] 分钟后，他的所有直属下属都可以开始传播这一消息）。
# 返回通知所有员工这一紧急消息所需要的 分钟数 。

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        # 不是每一层的最大值
        # ans=informTime[headID]
        # par=[headID] # 保存父节点
        # while par!=[]:
        #     par_len=len(par)
        #     max_t=0 
        #     for j in range(len(par)):
        #         for i in range(n):
        #             if manager[i]==par[j]:
        #                 max_t=max(max_t,informTime[i])
        #                 par.append(i)
        #     print(max_t)
        #     ans+=max_t 
        #     par=par[par_len:]
        #     print(par)
        # return ans
        
        # 最长路径和dfs
        # 超出时间限制，每一次都要遍历一遍manager数组
        # def dfs(p: int):
        #     ans=0
        #     for i in range(n):
        #         if manager[i]==p:
        #             ans=max(ans,dfs(i)+informTime[p])
        #     return ans
        # return dfs(headID)

        # 优化
        g = [[] for _ in range(n)]
        for i, m in enumerate(manager):
            if m >= 0:
                g[m].append(i)  # 建树
        print(g)
        # 递归 自顶向下
        def dfs(x: int) -> int:
            max_path_sum = 0
            for y in g[x]:  # 遍历 x 的儿子 y（如果没有儿子就不会进入循环）
                print(g[x])
                print(max_path_sum)
                max_path_sum = max(max_path_sum, dfs(y))
            return max_path_sum + informTime[x]
        return dfs(headID)  # 从根节点 headID 开始递归
        # 迭代 自底向上
        # for i, m in enumerate(manager):
        #     if m<0:
        #         continue
        #     s=0
        #     x=i
        #     while manager[x]>=0:
        #         s+=informTime[x]
        #         x=manager[x]
        #     s+=informTime[x]
        #     x=i
        #     while manager[x]>=0:
        #         informTime[x],s=s,s-informTime[x]
        #         manager[x],x=-1,manager[x]
        # print(informTime)
        # return max(informTime)
        



S=Solution()
# print(S.numOfMinutes(15,0,[-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6],[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]))
# print(S.numOfMinutes(10,3,[8,9,8,-1,7,1,2,0,3,0],[224,943,160,909,0,0,0,643,867,722]))
print(S.numOfMinutes(11,4,[5,9,6,10,-1,8,9,1,9,3,4],[0,213,0,253,686,170,975,0,261,309,337]))