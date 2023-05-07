# 在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。
# 返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。形式上，我们希望下标数字 i 和 j 满足  i < j 且有 (time[i] + time[j]) % 60 == 0。

class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        # 两首歌组合，双指针
        # 超时
        # cnt=0
        # for i in range(len(time)-1):
        #     for j in range(i+1,len(time)):
        #         if (time[i]+time[j])%60==0:
        #             cnt+=1
        # return cnt
        
        # 哈希表储存余数
        f={}
        for t in time:
            if f.get(t%60,-1)==-1:
                f[t%60]=1
            else:
                f[t%60]+=1
        cnt=0
        for r in range(1,30):
            if f.get(r,-1)!=-1 and f.get(60-r,-1)!=-1:
                cnt+=f[r]*f[60-r]
        for r in [0,30]:
            if f.get(r,-1)!=-1:
                cnt+=int(f[r]*(f[r]-1)/2)
        return cnt