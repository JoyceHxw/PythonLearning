# 请你将一些箱子装在 一辆卡车 上。给你一个二维数组 boxTypes ，其中 boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi] ：
# numberOfBoxesi 是类型 i 的箱子的数量。
# numberOfUnitsPerBoxi 是类型 i 每个箱子可以装载的单元数量。
# 整数 truckSize 表示卡车上可以装载 箱子 的 最大数量 。只要箱子数量不超过 truckSize ，你就可以选择任意箱子装到卡车上。
# 返回卡车可以装载 单元 的 最大 总数。


class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes=sorted(boxTypes, key=lambda c: c[1], reverse=True)
        print(boxTypes)
        num=0
        cnt=0
        for j in range(0,len(boxTypes)):
            left_num=truckSize-cnt
            cnt+=boxTypes[j][0]
            print("left_num=",left_num)
            print("cnt=",cnt)
            if cnt<=truckSize:
                num+=boxTypes[j][0]*boxTypes[j][1]
                print("num=",num)
            else:
                num+=left_num*boxTypes[j][1]
                print("num=",num)
                break
        return num

S=Solution()
S.maximumUnits([[5,10],[2,5],[4,7],[3,9]],10)