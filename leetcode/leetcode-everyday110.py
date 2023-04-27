# 给出一个单词数组 words ，其中每个单词都由小写英文字母组成。
# 如果我们可以 不改变其他字符的顺序 ，在 wordA 的任何地方添加 恰好一个 字母使其变成 wordB ，那么我们认为 wordA 是 wordB 的 前身 。
# 例如，"abc" 是 "abac" 的 前身 ，而 "cba" 不是 "bcad" 的 前身
# 词链是单词 [word_1, word_2, ..., word_k] 组成的序列，k >= 1，其中 word1 是 word2 的前身，word2 是 word3 的前身，依此类推。一个单词通常是 k == 1 的 单词链 。
# 从给定单词列表 words 中选择单词组成词链，返回 词链的 最长可能长度 。

class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        # 动态规划
        # 求n个单词的最长词链需要基于前n-1个单词的最长词链
        # 枚举单词去掉一个字母后的单词是否存在，哈希表
        # 按字符串长度排序
        s_words=sorted(words,key=lambda x:len(x))
        # print(s_words)
        f={}
        for word in s_words:
            f[word]=1
            for i in range(len(word)):
                prev=word[:i]+word[i+1:]
                if prev in f.keys():
                    f[word]=max(f[word],f[prev]+1)
        return max(f.values())

S=Solution()
print(S.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))      