class Solution:
    def reachNumber(self, target: int) -> int:
        # 假设1：向一个方向移动，正好可以到达target
        # 假设2：向两个方向移动，才能到达target
        # 将任何数字A由加号变成减号，都会使原总和减少2*A，2*A一定是偶数
        # 我们就可以首先只朝一个方向移动（由于target会有负数的情况，所以为了统一计算方式，我们将target取绝对值即可，即：t = Math.abs(target)），
        # 只有当移动的总距离 num 的值大于等于 t （target的绝对值），并且 num 减 t 是偶数，才表示当前情况满足题目要求，
        # 即：满足到达 target 所需的最小移动次数。
        # position=0
        # i=0
        # while position!=target:
        #     i+=1
        #     print('i=',i)
        #     if target>=0:
        #         if position+i<=target:
        #             position+=i
        #         else:
        #             position-=i
        #         print('position=',position)
        #     else:
        #         if position-i>=target:
        #             position-=i
        #         else:
        #             position+=i
        #         print('position=',position)
        # return i
        target = abs(target)
        s = n = 0
        while s < target or (s - target) % 2: 
            n += 1
            s += n
            print('n=',n)
            print('s=',s)
        return n


s=Solution()
print(s.reachNumber(4))