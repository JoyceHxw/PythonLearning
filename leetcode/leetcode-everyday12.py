def maxRepeating(sequence: str, word: str) -> int:
    cnt=0
    # 不是连续重复
    # while sequence.find(word)>=0:
    #     cnt+=1
    #     print('cnt=',cnt)
    #     print("befor:",sequence)
    #     print(sequence.find(word))
    #     # sequence=sequence.replace(word,'')
    #     sequence=sequence[0:sequence.find(word)]+sequence[sequence.find(word)+len(word):]
    #     print("after:",sequence)

    # 连续重复
    word0=word
    while sequence.find(word)>=0:
        cnt+=1
        word1=word+word0
        word=word1
        print(word1)
    return cnt

print(maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba",'aaaba'))

# sequence='ababc'
# word='ba'
# s=sequence.replace(word,'')
# print(s)