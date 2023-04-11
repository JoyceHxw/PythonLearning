# 在无限的平面上，机器人最初位于 (0, 0) 处，面朝北方。注意:
# 北方向 是y轴的正方向。
# 南方向 是y轴的负方向。
# 东方向 是x轴的正方向。
# 西方向 是x轴的负方向。
# 机器人可以接受下列三条指令之一：
# "G"：直走 1 个单位
# "L"：左转 90 度
# "R"：右转 90 度
# 机器人按顺序执行指令 instructions，并一直重复它们。
# 只有在平面中存在环使得机器人永远无法离开时，返回 true。否则，返回 false。


# 模拟分析总结
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos=[0,0]
        direction=0
        for ins in instructions:
            if ins=="G":
                r=direction%4
                if r==0:
                    pos[1]+=1
                elif r==1:
                    pos[0]+=1
                elif r==2:
                    pos[1]-=1
                elif r==3:
                    pos[0]-=1
            elif ins=="L":
                direction+=3
            else:
                direction+=1
        if pos==[0,0]:
            return True
        elif direction%4!=0:
            return True
        else:
            return False