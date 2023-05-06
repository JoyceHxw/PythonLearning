# 给你一个字符串 croakOfFrogs，它表示不同青蛙发出的蛙鸣声（字符串 "croak" ）的组合。由于同一时间可以有多只青蛙呱呱作响，所以 croakOfFrogs 中会混合多个 “croak” 。
# 请你返回模拟字符串中所有蛙鸣所需不同青蛙的最少数目。
# 要想发出蛙鸣 "croak"，青蛙必须 依序 输出 ‘c’, ’r’, ’o’, ’a’, ’k’ 这 5 个字母。如果没有输出全部五个字母，那么它就不会发出声音。如果字符串 croakOfFrogs 不是由若干有效的 "croak" 字符混合而成，请返回 -1 。


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        # 不能用栈，可能相互穿插
        # 超出时间限制
        # croak="croak"
        # j=0
        # s=croakOfFrogs
        # ans=0
        # while s!="":
        #     t=""
        #     print("s=",s)
        #     ans+=1
        #     for i in range(len(s)):
        #         # print("i=",i)
        #         # print("j=",j)
        #         if j==5:
        #             j=0
        #         if s[i]==croak[j]:
        #             j+=1 
        #         else:
        #             t+=s[i]
        #     s=t
        #     if (s!="" and len(s)<5) or (s=="" and j!=5):
        #         return -1
        # return ans

        # 优化，哈希表
        if len(croakOfFrogs) % 5:
            return -1
        res, frog_num = 0, 0
        cnt = [0] * 4
        mp = {'c':0, 'r':1, 'o':2, 'a':3, 'k':4}
        for c in croakOfFrogs:
            t = mp[c]
            if t == 0:
                cnt[t] += 1
                frog_num += 1
                if frog_num > res: # 记录过程中最大值
                    res = frog_num
            else:
                if cnt[t - 1] == 0:  # 没有发出前一个音
                    return -1
                cnt[t - 1] -= 1
                if t == 4:  # 发出了最后一个音，完成鸣叫
                    frog_num -= 1  # 连续的叫声只记一次
                else:
                    cnt[t] += 1
        if frog_num > 0: # 没有完成鸣叫
            return -1
        return res
    
S=Solution()
# print(S.minNumberOfFrogs("croakcroak"))
print(S.minNumberOfFrogs("crcoakroak"))
# print(S.minNumberOfFrogs("croakcrook"))
# print(S.minNumberOfFrogs("croakcroa"))