# 给定字符串 s 和字符串数组 words, 返回  words[i] 中是s的子序列的单词个数 。
# 字符串的 子序列 是从原始字符串中生成的新字符串，可以从中删去一些字符(可以是none)，而不改变其余字符的相对顺序。
# 例如， “ace” 是 “abcde” 的子序列。

from collections import defaultdict, deque


class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        # cnt=0
        # for w in words:
        #     s1=s
        #     is_flag=True
        #     for l in w:
        #         if l in s1:
        #             s1=s1[s1.index(l)+1:] 
        #         else:
        #             is_flag=False
        #             continue
        #     if is_flag==True:
        #         cnt+=1
        # return cnt

# 我们不妨将 wordswords 中的所有单词根据首字母来分桶，即：把所有单词按照首字母分到 2626 个桶中，每个桶中存储的是所有以该字母开头的所有单词。
# 然后我们从 ss 的第一个字符开始遍历，假设当前字符为 'a'，我们从 'a' 开头的桶中取出所有单词。对于取出的每个单词，如果此时单词长度为 11，说明该单词已经匹配完毕，我们将答案加 11；否则我们将单词的首字母去掉，然后放入下一个字母开头的桶中
        d = defaultdict(deque)
        for w in words:
            d[w[0]].append(w)
        ans = 0
        print(d)
        for c in s:
            for _ in range(len(d[c])):
                print(d[c])
                t = d[c].popleft()
                print("t=",t)
                if len(t) == 1:
                    ans += 1
                else:
                    d[t[1]].append(t[1:])
        return ans

S=Solution()
S.numMatchingSubseq("dsahjpjauf",["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"])
