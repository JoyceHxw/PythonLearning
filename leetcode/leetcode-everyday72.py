# 你正在经营一座摩天轮，该摩天轮共有 4 个座舱 ，每个座舱 最多可以容纳 4 位游客 。你可以 逆时针 轮转座舱，但每次轮转都需要支付一定的运行成本 runningCost 。摩天轮每次轮转都恰好转动 1 / 4 周。
# 给你一个长度为 n 的数组 customers ， customers[i] 是在第 i 次轮转（下标从 0 开始）之前到达的新游客的数量。这也意味着你必须在新游客到来前轮转 i 次。每位游客在登上离地面最近的座舱前都会支付登舱成本 boardingCost ，一旦该座舱再次抵达地面，他们就会离开座舱结束游玩。
# 你可以随时停下摩天轮，即便是 在服务所有游客之前 。如果你决定停止运营摩天轮，为了保证所有游客安全着陆，将免费进行所有后续轮转 。注意，如果有超过 4 位游客在等摩天轮，那么只有 4 位游客可以登上摩天轮，其余的需要等待 下一次轮转 。
# 返回最大化利润所需执行的 最小轮转次数 。 如果不存在利润为正的方案，则返回 -1 。

class Solution:
    def minOperationsMaxProfit(self, customers: list[int], boardingCost: int, runningCost: int) -> int:
        # cnt=0
        # profit=0
        # people=0
        # for customer in customers:
        #     customer+=people
        #     if customer==0:  //中途没有等待的人
        #         cnt+=1
        #     # if 4>customer>0 and customer*boardingCost-runningCost>0: 
        #     #     cnt+=1
        #     while customer>4:
        #         customer-=4
        #         cnt+=1
        #         profit+=4*boardingCost-runningCost
        #         print("cnt=",cnt)
        #         print("profit=",profit)
        #     people=customer
        # print("customer=",customer)
        # print("sum_people=",sum(customers))
        # profit+=customer*boardingCost-runningCost
        # if customer*boardingCost-runningCost>0:
        #     cnt+=1
        # if profit>0:
        #     return cnt
        # else:
        #     return -1

        ans = -1
        mx = t = 0
        wait = 0
        i = 0
        while wait or i < len(customers):
            wait += customers[i] if i < len(customers) else 0
            up = wait if wait < 4 else 4
            wait -= up
            t += up * boardingCost - runningCost
            i += 1
            if t > mx:
                mx = t
                ans = i
        return ans

     

S=Solution()
# print(S.minOperationsMaxProfit([8,3],5,6))
# print(S.minOperationsMaxProfit([10,9,6],6,4))
# print(S.minOperationsMaxProfit([10,10,6,4,7],3,8))
# print(S.minOperationsMaxProfit([2],2,4))
# print(S.minOperationsMaxProfit([0,43,37,9,23,35,18,7,45,3,8,24,1,6,37,2,38,15,1,14,39,27,4,25,27,33,43,8,44,30,38,40,20,5,17,27,43,11,6,2,30,49,30,25,32,3,18,23,45,43,30,14,41,17,42,42,44,38,18,26,32,48,37,5,37,21,2,9,48,48,40,45,25,30,49,41,4,48,40,29,23,17,7,5,44,23,43,9,35,26,44,3,26,16,31,11,9,4,28,49,43,39,9,39,37,7,6,7,16,1,30,2,4,43,23,16,39,5,30,23,39,29,31,26,35,15,5,11,45,44,45,43,4,24,40,7,36,10,10,18,6,20,13,11,20,3,32,49,34,41,13,11,3,13,0,13,44,48,43,23,12,23,2],43,54))
print(S.minOperationsMaxProfit([1,2,1,2,1,2,1,1],90,46))
