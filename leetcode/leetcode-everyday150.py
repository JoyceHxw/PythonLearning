# 给你一个正整数数组 nums 。每一次操作中，你可以从 nums 中选择 任意 一个数并将它减小到 恰好 一半。（注意，在后续操作中你可以对减半过的数继续执行操作）
# 请你返回将 nums 数组和 至少 减少一半的 最少 操作数。


from heapq import heappop, heappush


# 对优先队列的使用和熟悉还不够
# 优先队列为最大堆/最小堆，整理最大/小元素的时间复杂度为O(logn)
class Solution:
    def halveArray(self, nums: list[int]) -> int:
        # 贪心算法
        # 数组排序和元素替换
        # cnt=0
        # s=sum(nums)
        # s_half=s/2
        # nums.sort(reverse=True)
        # while s>s_half:
        #     #超时
        #     # temp=nums[0]/2
        #     # s-=temp
        #     # nums.pop(0)
        #     # i=0
        #     # while i<len(nums)-1 and temp<nums[i] :
        #     #     i+=1
        #     # nums.insert(i,temp)
        #     nums[0]/=2
        #     s-=nums[0]
        #     cnt+=1
        #     nums.sort(reverse=True)
        # return cnt

        pq = []
        for num in nums:
            heappush(pq, -num)
        res = 0
        sum1 = sum(nums)
        sum2 = 0
        while sum2 < sum1 / 2:
            x = -heappop(pq)
            sum2 += x / 2
            heappush(pq, -(x / 2))
            res += 1
        return res

       