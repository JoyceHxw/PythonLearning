# 给你 n 个二维平面上的点 points ，其中 points[i] = [xi, yi] ，请你返回两点之间内部不包含任何点的 最宽垂直区域 的宽度。
# 垂直区域 的定义是固定宽度，而 y 轴上无限延伸的一块区域（也就是高度为无穷大）。 最宽垂直区域 为宽度最大的一个垂直区域。
# 请注意，垂直区域 边上 的点 不在 区域内。



class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        # points.sort()
        # max_width=0
        # for i in range(0,len(points)-1):
        #     max_width=max(max_width,points[i+1][0]-points[i][0])
        # return max_width
        
        # 桶排序
        min_v=99999999
        max_v=-99999999
        for i in range(len(points)):
            min_v=min(min_v,points[i][0])
            max_v=max(max_v,points[i][0])
        # 桶大小
        bucket_size=max(1,(max_v-min_v)/(len(points)-1))
        # 桶数量
        bucket_cnt=int((max_v-min_v)/bucket_size)+1
        buckets=[[0,99999999,-99999999]]*bucket_cnt
        # print(buckets[0])
        for p in points:
            index=int((p[0]-min_v)/bucket_size)
            # print(index)
            # print(p[0])
            print(buckets[index][1])
            buckets[index]=[1,min(p[0],buckets[index][1]),max(p[0],buckets[index][2])]
            # buckets[index][1]=min(p[0],buckets[index][1])
            # buckets[index][2]=max(p[0],buckets[index][2])
        print(buckets)
        max_width=0
        last_max=min_v
        for i in range(bucket_cnt):
            if buckets[i][0]==1:
                max_width=max(max_width,buckets[i][1]-last_max)
                last_max=buckets[i][2]
        return max_width

S=Solution()
S.maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]])