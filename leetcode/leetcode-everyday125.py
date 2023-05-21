from cmath import inf
from math import ceil

class Solution:
    def storeWater(self, bucket: list[int], vat: list[int]) -> int:
        # 先确定升级次数不能求得最优解
        # cnt=0
        # while True:
        #     max_c=0
        #     max_c_i=0
        #     l=[]
        #     for i in range(len(bucket)):
        #         if bucket[i]!=0:
        #             t=ceil(vat[i]/bucket[i])
        #         else:
        #             t=inf
        #         if max_c<t:
        #             max_c=t
        #             max_c_i=i
        #         l.append(t)
        #     if max_c==0:
        #         return 0
        #     c=Counter(l)
        #     if (c[max_c]==1 and len(c)>1) or (len(c)==1 and max_c==inf):
        #         bucket[max_c_i]+=1
        #         cnt+=1
        #     else:
        #         cnt+=max_c
        #         return cnt

        # 逆向思维，枚举蓄水次数
        # 每一个升级容量次数=ceil(vat[i]/k)-bucket[i]
        max_k=max(vat)
        if max_k == 0:
            return 0
        res=inf
        for i in range(1,max_k+1):
            t=0
            for j in range(len(bucket)):
                t+=max(0,ceil(vat[j]/i)-bucket[j])
            res=min(res,t+i)
        return res   

S=Solution()
print(S.storeWater([16,29,42,70,42,9],[89,44,50,90,94,91]))