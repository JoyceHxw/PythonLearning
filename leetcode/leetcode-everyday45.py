# 一个句子是由一些单词与它们之间的单个空格组成，且句子的开头和结尾没有多余空格。比方说，"Hello World" ，"HELLO" ，"hello world hello world" 都是句子。每个单词都 只 包含大写和小写英文字母。
# 如果两个句子 sentence1 和 sentence2 ，可以通过往其中一个句子插入一个任意的句子（可以是空句子）而得到另一个句子，那么我们称这两个句子是 相似的 。比方说，sentence1 = "Hello my name is Jane" 且 sentence2 = "Hello Jane" ，我们可以往 sentence2 中 "Hello" 和 "Jane" 之间插入 "my name is" 得到 sentence1 。
# 给你两个句子 sentence1 和 sentence2 ，如果 sentence1 和 sentence2 是相似的，请你返回 true ，否则返回 false 。


# class Solution:
#     def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
#         l1=sentence1.split(" ")
#         l2=sentence2.split(" ")

#         if len(l1)>=len(l2):
#             try:
#                 for i,word in enumerate(l2):
#                     print(l1)
#                     print(word)
#                     print(l1.index(word))
#                     print(i)
#                     print(len(l1)-1-(len(l2)-i-1))
#                     if l1.index(word)==0 or l1.index(word)==len(l1)-1-(len(l2)-i-1):
#                         l1.remove(word)
#                         pass
#                     else:
#                         print("!!!")
#                         return False
#                 return True
#             except:
#                 return False
#         elif len(l1)<len(l2):
#             try:
#                 for i,word in enumerate(l1):
#                     print(l2)
#                     print(word)
#                     print(l2.index(word))
#                     print(len(l2)-1-(len(l1)-i-1))
#                     if l2.index(word)==0 or l2.index(word)==len(l2)-1-(len(l1)-i-1):
#                         l2.remove(word)
#                         pass
#                     else:
#                         print("!!!")
#                         return False
#                 print("where are you")
#                 return True
#             except:
#                 print("???")
#                 return False


# 根据题意，两个句子 sentence1和sentence2，如果是相似的，那么这两个句子按空格分割得到的字符串数组words1和words2
# ，一定能通过往其中一个字符串数组中插入某个字符串数组（可以为空），得到另一个字符串数组。这个验证可以通过双指针完成。
# i 表示两个字符串数组从左开始，最多有 i 个字符串相同。j 表示剩下的字符串数组从右开始，最多有 j 个字符串相同。
# 如果 i+j 正好是某个字符串数组的长度，那么原字符串就是相似的。

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()
        print(words1)
        print(words2)
        i, j = 0, 0
        while i < len(words1) and i < len(words2) and words1[i] == words2[i]:
            i += 1
        while j < len(words1) - i and j < len(words2) - i and words1[-j - 1] == words2[-j - 1]:
            j += 1
        print(i)
        print(j)
        return i + j == min(len(words1), len(words2))


S=Solution()
# print(S.areSentencesSimilar("Luky","Lucccky"))
# print(S.areSentencesSimilar("c h p Ny","c BDQ r h p Ny"))
# print(S.areSentencesSimilar("d T d ED uXW L U J n klIe","d T d ED uXW L U J klIe"))
print(S.areSentencesSimilar("A","a A b A"))   # 原算法index函数不能区分
