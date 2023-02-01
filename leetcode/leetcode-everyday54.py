# 给你字符串 key 和 message ，分别表示一个加密密钥和一段加密消息。解密 message 的步骤如下：

# 使用 key 中 26 个英文小写字母第一次出现的顺序作为替换表中的字母 顺序 。
# 将替换表与普通英文字母表对齐，形成对照表。
# 按照对照表 替换 message 中的每个字母。
# 空格 ' ' 保持不变。

from string import ascii_lowercase


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet="abcdefghijklmnopqrstuvwxyz"
        lst=[]
        for l in key:
            if l not in lst and l!=" ":
                lst.append(l)
        decode=""
        for l in message:
            if l!=" ":
                a=lst.index(l)
                decode+=alphabet[a]
            else:
                decode+=l
        return decode

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {" ": " "}
        i = 0
        for c in key:
            if c not in d:
                d[c] = ascii_lowercase[i]
                i += 1
            print(d)
        return "".join(d[c] for c in message)

S=Solution()
print(S.decodeMessage("the quick brown fox jumps over the lazy dog","vkbs bs t suepuv"))