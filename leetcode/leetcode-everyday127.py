# 我们有一个 n 项的集合。给出两个整数数组 values 和 labels ，第 i 个元素的值和标签分别是 values[i] 和 labels[i]。还会给出两个整数 numWanted 和 useLimit 。
# 从 n 个元素中选择一个子集 s :
# 子集 s 的大小 小于或等于 numWanted 。
# s 中 最多 有相同标签的 useLimit 项。
# 一个子集的 分数 是该子集的值之和。
# 返回子集 s 的最大 分数 。


from cmath import inf
from collections import Counter


class Solution:
    def largestValsFromLabels(self, values: list[int], labels: list[int], numWanted: int, useLimit: int) -> int:
        # 贪心算法，每次从所有标签中选择可以选择的最大数
        # c={}
        # s=set(labels)
        # d={}
        # max_index={}
        # for n in s:
        #     l=[]
        #     for i in range(len(values)):
        #         if labels[i]==n:
        #             l.append(values[i])
        #     l=sorted(l,reverse=True)
        #     d[n]=l
        #     max_index[n]=0
        #     c[n]=0
        # ans=0
        # cnt1=0
        # while cnt1<numWanted:
        #     isflag=False
        #     temp=-inf
        #     max_n=labels[0]
        #     for n in s:
        #         if max_index[n]<len(d[n]) and c[n]<useLimit:
        #             isflag=True
        #             if d[n][max_index[n]]>temp:
        #                 temp=d[n][max_index[n]]
        #                 max_n=n
        #     if(isflag==False):
        #         return ans
        #     ans+=temp
        #     cnt1+=1
        #     c[max_n]+=1
        #     max_index[max_n]+=1
        # return ans

        # 上述方法超时，先对values进行排序，注意是对其index排序（values和labels对应的index相同）
        n = len(values)
        idx = list(range(n))
        idx.sort(key=lambda i: -values[i])
        cnt=Counter()
        c=0
        i=0
        ans=0
        while c<numWanted and i<n:
            if cnt[labels[idx[i]]]<useLimit:
                ans+=values[idx[i]]
                c+=1
                cnt[labels[idx[i]]]+=1
            i+=1
        return ans

    
S=Solution()
print(S.largestValsFromLabels([9,8,8,7,6],[0,0,0,1,1],3,1))