# 在桌子上有 N 张卡片，每张卡片的正面和背面都写着一个正数（正面与背面上的数有可能不一样）。
# 我们可以先翻转任意张卡片，然后选择其中一张卡片。
# 如果选中的那张卡片背面的数字 X 与任意一张卡片的正面的数字都不同，那么这个数字是我们想要的数字。
# 哪个数是这些想要的数字中最小的数（找到这些数中的最小值）呢？如果没有一个数字符合要求的，输出 0。
# 其中, fronts[i] 和 backs[i] 分别代表第 i 张卡片的正面和背面的数字。
# 如果我们通过翻转卡片来交换正面与背面上的数，那么当初在正面的数就变成背面的数，背面的数就变成正面的数。

class Solution:
    def flipgame(self, fronts: list[int], backs: list[int]) -> int:
        # 是否正反面相同
        # 集合保存
        s=set()
        usable=set()
        for i in range(len(fronts)):
            # 可选答案
            if fronts[i]!=backs[i]:
                if fronts[i] in s and backs[i] not in s:
                    usable.add(backs[i])
                elif backs[i] in s and fronts[i] not in s:
                    usable.add(fronts[i])
                elif backs[i] in s and fronts[i] in s:
                    continue
                else:
                    usable.add(backs[i])
                    usable.add(fronts[i])
            # 剔除答案
            else: 
                s.add(fronts[i])
                if fronts[i] in usable:
                    usable.remove(fronts[i])
        if len(usable)==0:
            return 0
        else:
            return min(usable)
         