# 你会得到一个字符串 text 。你应该把它分成 k 个子字符串 (subtext1, subtext2，…， subtextk) ，要求满足:
# subtexti 是 非空 字符串
# 所有子字符串的连接等于 text ( 即subtext1 + subtext2 + ... + subtextk == text )
# 对于所有 i 的有效值( 即 1 <= i <= k ) ，subtexti == subtextk - i + 1 均成立
# 返回k可能最大值。

class Solution:
    def longestDecomposition(self, text: str) -> int:
        # 双指针
        # n=len(text)
        print(n)
        left=0
        right=n-1
        cnt=0
        while left<right:
            while text[left]!=text[right]:
                right-=1
            isFlag=True
            for i in range(n-right):
                if text[left+i]!=text[right+i]:
                    isFlag=False
                    right-=1 #单词内可能有相同字母
                    break
            if left<right and isFlag==True:
                cnt+=1
                left+=(n-right)
                n=right
                right-=1
                # print("right=",right)
                # print("left=",left)
        if left==right+1:
            return 2*cnt
        else:
            return 2*cnt+1
