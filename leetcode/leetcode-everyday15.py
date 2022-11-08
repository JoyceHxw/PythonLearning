# 给你一个由不同字符组成的字符串 allowed 和一个字符串数组 words 。如果一个字符串的每一个字符都在 allowed 中，就称这个字符串是 一致字符串 。
# 请你返回 words 数组中 一致字符串 的数目。

class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        cnt=0
        for word in words:
            is_flag=True
            for letter in word:
                if letter not in allowed:
                    is_flag=False
                    break
            
            if is_flag==True:
                cnt+=1
        return cnt

S=Solution()
print(S.countConsistentStrings("ab",["ad","bd","aaab","baa","badab"]))