# 给你一个字符串 word ，该字符串由数字和小写英文字母组成。
# 请你用空格替换每个不是数字的字符。例如，"a123bc34d8ef34" 将会变成 " 123  34 8  34" 。注意，剩下的这些整数为（相邻彼此至少有一个空格隔开）："123"、"34"、"8" 和 "34" 。
# 返回对 word 完成替换后形成的 不同 整数的数目。
# 只有当两个整数的 不含前导零 的十进制表示不同， 才认为这两个整数也不同

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        # s=set()
        # i=0
        # print(len(word))
        # while i <len(word):
        #     print(i)
        #     print("word[i]=",word[i])
        #     if word[i].isdigit():
        #         start=i
        #         end=0
        #         if start+1==len(word):
        #             s.add(int(word[i]))
        #             break
        #         for j in range(start+1,len(word)):
        #             print("i=",i)
        #             print("j=",j)
        #             print("word[j]=",word[j])
        #             print(word[j].isdigit())
        #             # break
        #             if word[j].isdigit()==False:
        #                 s.add(int(word[start:j]))
        #                 print("s=",s)
        #                 i=j
        #                 break
        #             if word[j].isdigit()==True and j==len(word)-1:
        #                 s.add(int(word[start:j+1]))
        #             end=j
        #         if end==len(word)-1:
        #             break
        #     else:
        #         i+=1

        # return len(s)

        s = set()
        n = len(word)
        p1 = 0
        while True:
            while p1 < n and not word[p1].isdigit():
                p1 += 1

            if p1 == n:
                break

            p2 = p1

            while p2 < n and word[p2].isdigit():
                p2 += 1

            while p2 - p1 > 1 and word[p1] == '0':  # 去除前导 0
                p1 += 1

            s.add(word[p1:p2])
            p1 = p2
        return len(s)

S=Solution()
print(S.numDifferentIntegers("a123bc34d8ef34"))
print(S.numDifferentIntegers("4"))
print(S.numDifferentIntegers("0a0"))