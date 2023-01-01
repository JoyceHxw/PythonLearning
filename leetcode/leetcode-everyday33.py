# 给你一个由小写英文字母组成的字符串 s ，请你找出并返回第一个出现 两次 的字母。
# 注意：
# 如果 a 的 第二次 出现比 b 的 第二次 出现在字符串中的位置更靠前，则认为字母 a 在字母 b 之前出现两次。
# s 包含至少一个出现两次的字母。

# class Solution:
#     def repeatedCharacter(self, s: str) -> str:
#         letters=set(s)
#         dic={}
#         for l in letters:
#             dic[l]=[]
#             for num in range(len(s)):
#                 if l==s[num]:
#                     dic[l].append(num)
#         # filter函数对字典进行处理的时候，筛选的对象是字典的键，而不是字典的值
#         dic_1={i:j for i,j in dic.items() if i in list(filter(lambda x:len(dic[x])>=2,dic))}
#         return sorted(dic_1.items(),key=lambda x:x[1][1])[0][0]

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for ch in s:
            if ch in seen:
                return ch
            seen.add(ch)

S=Solution()
print(S.repeatedCharacter('abccbaacz'))
