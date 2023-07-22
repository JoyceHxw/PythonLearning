# 在柠檬水摊上，每一杯柠檬水的售价为 5 美元。顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
# 每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。
# 注意，一开始你手头没有任何零钱。
# 给你一个整数数组 bills ，其中 bills[i] 是第 i 位顾客付的账。如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

# 简单的贪心算法
class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        # 只有找15块或5块的情况
        d={5:0,10:0,20:0}
        for b in bills:
            d[b]+=1
            change=b-5
            while change>0:
                if d[10]>0 and change>10:
                    change-=10
                    d[10]-=1
                elif d[5]>0:
                    change-=5
                    d[5]-=1
                else:
                    return False
        return True