# 给你两个字符串 start 和 target ，长度均为 n 。每个字符串 仅 由字符 'L'、'R' 和 '_' 组成，其中：
# 字符 'L' 和 'R' 表示片段，其中片段 'L' 只有在其左侧直接存在一个 空位 时才能向 左 移动，而片段 'R' 只有在其右侧直接存在一个 空位 时才能向 右 移动。
# 字符 '_' 表示可以被 任意 'L' 或 'R' 片段占据的空位。
# 如果在移动字符串 start 中的片段任意次之后可以得到字符串 target ，返回 true ；否则，返回 false 。

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # 相对顺序是固定的，顺序遍历比较即可
        # 分左右忽略了LR交替出现的情况
        i=0
        j=0
        n=len(start)
        while i<n and j<n:
            while i<n and start[i]=='_':
                i+=1
            while j<n and target[j]=='_':
                j+=1
            if i<n and j<n:
                if start[i]!=target[j]:
                    return False
                else:
                    if i<n and j<n and start[i]=='R' and i>j:
                        return False
                    if i<n and j<n and start[i]=='L' and i<j:
                        return False
                    i+=1
                    j+=1
        while i<n:
            if start[i]!='_':
                return False
            i+=1
        while j<n:
            if target[j]!='_':
                return False
            j+=1
        return True

S=Solution()
S.canChange("_L__R__R_L", "L______RR_")