# 给你一个正整数数组 price ，其中 price[i] 表示第 i 类糖果的价格，另给你一个正整数 k 。
# 商店组合 k 类 不同 糖果打包成礼盒出售。礼盒的 甜蜜度 是礼盒中任意两种糖果 价格 绝对差的最小值。
# 返回礼盒的 最大 甜蜜度。


class Solution:
    def maximumTastiness(self, price: list[int], k: int) -> int:
        price.sort()
        # 检查满足差值的个数
        def check(mid: int):
            # print("mid=",mid)
            pre=-mid
            cnt=0
            for i in range(len(price)):
                if price[i]-pre>=mid:
                    # print(price[i])
                    cnt+=1
                    pre=price[i]
            return cnt>=k
        # 最大差值和最小差值
        left=0
        right=price[-1]-price[0]
        # 二分法遍历，看是否找到能满足条件的最大差值
        while left<right:
            mid=int((right-left+1)/2+left)
            if check(mid):
                left=mid
            else:
                right=mid-1
        return left