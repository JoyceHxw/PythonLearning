# 有两只老鼠和 n 块不同类型的奶酪，每块奶酪都只能被其中一只老鼠吃掉。
# 下标为 i 处的奶酪被吃掉的得分为：
# 如果第一只老鼠吃掉，则得分为 reward1[i] 。
# 如果第二只老鼠吃掉，则得分为 reward2[i] 。
# 给你一个正整数数组 reward1 ，一个正整数数组 reward2 ，和一个非负整数 k 。
# 请你返回第一只老鼠恰好吃掉 k 块奶酪的情况下，最大 得分为多少。


class Solution:
    def miceAndCheese(self, reward1: list[int], reward2: list[int], k: int) -> int:
        s=0
        # dif=[]
        # for i in range(len(reward1)):
        #     dif.append(reward1[i]-reward2[i])
        # dif.sort(reverse=True)
        # r1=sorted(reward1, key=lambda x:dif[reward1.index(x)], reverse=True)
        dif=[2,1,4,5,3]
        r2=sorted(reward2, key=lambda x:dif[reward2.index(x)])
        i=0
        # print(r1)
        print(r2)
        print(dif)
        # while i<k:
        #     s+=r1[i]
        #     i+=1
        # while i<len(reward1):
        #     s+=r2[i]
        #     i+=1
        # return s
S=Solution()
print(S.miceAndCheese([4,1,5,3,3],[3,4,1,5,2],3))