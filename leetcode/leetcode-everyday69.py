# 给你两个二维整数数组 items1 和 items2 ，表示两个物品集合。每个数组 items 有以下特质：

# items[i] = [valuei, weighti] 其中 valuei 表示第 i 件物品的 价值 ，weighti 表示第 i 件物品的 重量 。
# items 中每件物品的价值都是 唯一的 。
# 请你返回一个二维数组 ret，其中 ret[i] = [valuei, weighti]， weighti 是所有价值为 valuei 物品的 重量之和 。

# 注意：ret 应该按价值 升序 排序后返回。

from collections import Counter
from itertools import chain

class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        # result=[]
        # l1=[]
        # l2=[]
        # for i in items1:
        #     l1.append(i[0])
        # for i in items2:
        #     l2.append(i[0]) 
        # for item1 in items1:
        #     if item1[0] not in l2:
        #         result.append(item1)
        #         print(result)
        #     else:
        #         for item2 in items2:
        #             if item1[0]==item2[0]:
        #                 result.append([item1[0],item1[1]+item2[1]])
        # for item2 in items2:
        #     if item2[0] not in l1:
        #         result.append(item2)

        # result.sort(key=lambda x:x[0])
        # return result

        cnt = Counter()
        print(list(chain(items1, items2)))
        for v, w in chain(items1, items2):   # 把两个可迭代对象连接成一个可迭代对象
            cnt[v] += w
        print(cnt.items())
        return sorted(cnt.items())


S=Solution()
print(S.mergeSimilarItems([[1,3],[2,2]],[[7,1],[2,2],[1,4]]))