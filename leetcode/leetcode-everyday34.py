# 给你一个二维整数数组 orders ，其中每个 orders[i] = [pricei, amounti, orderTypei] 表示有 amounti 笔类型为 orderTypei 、价格为 pricei 的订单。
# 订单类型 orderTypei 可以分为两种：
# 0 表示这是一批采购订单 buy
# 1 表示这是一批销售订单 sell

# 注意，orders[i] 表示一批共计 amounti 笔的独立订单，这些订单的价格和类型相同。对于所有有效的 i ，由 orders[i] 表示的所有订单提交时间均早于 orders[i+1] 表示的所有订单。
# 存在由未执行订单组成的 积压订单 。积压订单最初是空的。提交订单时，会发生以下情况：
# 如果该订单是一笔采购订单 buy ，则可以查看积压订单中价格 最低 的销售订单 sell 。如果该销售订单 sell 的价格 低于或等于 当前采购订单 buy 的价格，则匹配并执行这两笔订单，并将销售订单 sell 从积压订单中删除。否则，采购订单 buy 将会添加到积压订单中。
# 反之亦然，如果该订单是一笔销售订单 sell ，则可以查看积压订单中价格 最高 的采购订单 buy 。如果该采购订单 buy 的价格 高于或等于 当前销售订单 sell 的价格，则匹配并执行这两笔订单，并将采购订单 buy 从积压订单中删除。否则，销售订单 sell 将会添加到积压订单中。
# 输入所有订单后，返回积压订单中的 订单总数 。由于数字可能很大，所以需要返回对 109 + 7 取余的结果。

# 没有判断销售订单价格最低和采购订单价格最高
# class Solution:
#     def getNumberOfBacklogOrders(self, orders: list[list[int]]) -> int:
#         stock=[]
#         cnt=0
#         for order in orders:
#             print(order)
#             if stock==[]:
#                 stock.append(order)
#             else:
#                 for order_s in stock:
#                     # print(order_s[2])
#                     if order_s[2]==0 and order[2]==1 and order_s[0]>=order[0]:
#                         if order_s[1]>=order[1]:
#                             order_s[1]-=order[1]
#                             order[1]=0
#                         else:
#                             order[1]-=order_s[1]
#                             order_s[1]=0
#                     # elif order_s[2]==0 && order[2]==1 && order_s[0]<order[0]:
#                     elif order_s[2]==1 and order[2]==0 and order_s[0]<=order[0]:
#                         if order_s[1]<=order[1]:
#                             order[1]-=order_s[1]
#                             order_s[1]=0
#                         else:
#                             order_s[1]-=order[1]
#                             order[1]=0
#                     # elif order_s[2]==1 && order[2]==0 && order_s[0]>order[0]:
#                     else:
#                         pass
#                 stock.append(order)
#                 print(stock)
#         for order_s in stock:
#             cnt+=order_s[1]
        
#         return cnt%(10**9+7)

from heapq import heappop, heappush
class Solution:
    def getNumberOfBacklogOrders(self, orders: list[list[int]]) -> int:
        MOD = 10 ** 9 + 7
        buyOrders, sellOrders = [], []
        for price, amount, type in orders:
            if type == 0:
                while amount and sellOrders and sellOrders[0][0] <= price:
                    if sellOrders[0][1] > amount:
                        sellOrders[0][1] -= amount
                        amount = 0
                        break
                    amount -= heappop(sellOrders)[1]
                if amount:
                    heappush(buyOrders, [-price, amount])
            else:
                while amount and buyOrders and -buyOrders[0][0] >= price:
                    if buyOrders[0][1] > amount:
                        buyOrders[0][1] -= amount
                        amount = 0
                        break
                    amount -= heappop(buyOrders)[1]
                if amount:
                    heappush(sellOrders, [price, amount])
            print(buyOrders, sellOrders)
        return (sum(x for _, x in buyOrders) + sum(x for _, x in sellOrders)) % MOD

                        
S=Solution()
# print(S.getNumberOfBacklogOrders([[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]))
# print(S.getNumberOfBacklogOrders([[26,7,0],[16,1,1],[14,20,0],[23,15,1],[24,26,0],[19,4,1],[1,1,0]]))
print(S.getNumberOfBacklogOrders([[30,27,1],[18,9,1],[11,4,0],[21,11,0],[1,1,1],[24,20,1],[15,13,1],[13,3,0],[30,11,1]]))