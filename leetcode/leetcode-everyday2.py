import math


def atMostNGivenDigitSet(digits, n):
    # digits=[int(x) for x in digits]
    # # numberlist=[]
    # a=0
    # if int(n/10)==0:
    #     for i in digits:
    #         if i<=n:
    #             a+=1
    #         # numberlist.append(i)
    # elif int(n/10)<10:
    #     for i in digits:
    #         a+=1
    #         # numberlist.append(i)
    #         for j in digits:
    #             if i*10+j <=n:
    #                 a+=1
    #             # numberlist.append(i*10+j)
    # elif int(n/10)<100:
    #     for i in digits:
    #         a+=1
    #         # numberlist.append(i)
    #         for j in digits:
    #             a+=1
    #             # numberlist.append(i*10+j)
    #             for k in digits:
    #                 if i*100+j*10+k <=n:
    #                     a+=1
    #                 # numberlist.append(i*100+j*10+k)
    # elif int(n/10)<1000:
    #     for i in digits:
    #         a+=1
    #         # numberlist.append(i)
    #         for j in digits:
    #             a+=1
    #             # numberlist.append(i*10+j)
    #             for k in digits:
    #                 a+=1
    #                 # numberlist.append(i*100+j*10+k)
    #                 for l in digits:
    #                     if i*1000+j*100+k*10+l<=n:
    #                         a+=1
    #                     # numberlist.append((i*1000+j*100+k*10+l))
    # elif int(n/10)<10000:
    #     for i in digits:
    #         a+=1
    #         # numberlist.append(i)
    #         for j in digits:
    #             a+=1
    #             # numberlist.append(i*10+j)
    #             for k in digits:
    #                 a+=1
    #                 # numberlist.append(i*100+j*10+k)
    #                 for l in digits:
    #                     a+=1
    #                     # numberlist.append((i*1000+j*100+k*10+l))
    #                     for m in digits:
    #                         if i*10000+j*1000+k*100+l*10+m <=n:
    #                             a+=1
    #                         # numberlist.append(i*10000+j*1000+k*100+l*10+m)
    # elif int(n/10)<100000:
    #     for i in digits:
    #         a+=1
    #         # numberlist.append(i)
    #         for j in digits:
    #             a+=1
    #             # numberlist.append(i*10+j)
    #             for k in digits:
    #                 a+=1
    #                 # numberlist.append(i*100+j*10+k)
    #                 for l in digits:
    #                     a+=1
    #                     # numberlist.append((i*1000+j*100+k*10+l))
    #                     for m in digits:
    #                         a+=1
    #                         # numberlist.append(i*10000+j*1000+k*100+l*10+m)
    #                         for s in digits:
    #                             if i*100000+j*10000+k*1000+l*100+m*10+s<=n:
    #                                 a+=1
    #                             # numberlist.append(i*100000+j*10000+k*1000+l*100+m*10+s)
    # elif int(n/10)<1000000:
    #     for i in digits:
    #         a+=1
    #         # numberlist.append(i)
    #         for j in digits:
    #             a+=1
    #             # numberlist.append(i*10+j)
    #             for k in digits:
    #                 a+=1
    #                 # numberlist.append(i*100+j*10+k)
    #                 for l in digits:
    #                     a+=1
    #                     # numberlist.append((i*1000+j*100+k*10+l))
    #                     for m in digits:
    #                         a+=1
    #                         # numberlist.append(i*10000+j*1000+k*100+l*10+m)
    #                         for s in digits:
    #                             a+=1
    #                             # numberlist.append(i*100000+j*10000+k*1000+l*100+m*10+s)
    #                             for o in digits:
    #                                 if i*1000000+j*100000+k*10000+l*1000+m*100+s*10+o<=n:
    #                                     a+=1
    #                                 # numberlist.append(i*1000000+j*100000+k*10000+l*1000+m*100+s*10+o)
    # elif int(n/10)<10000000:
    #     for i in digits:
    #         a+=1
    #         # numberlist.append(i)
    #         for j in digits:
    #             a+=1
    #             # numberlist.append(i*10+j)
    #             for k in digits:
    #                 a+=1
    #                 # numberlist.append(i*100+j*10+k)
    #                 for l in digits:
    #                     a+=1
    #                     # numberlist.append((i*1000+j*100+k*10+l))
    #                     for m in digits:
    #                         a+=1
    #                         # numberlist.append(i*10000+j*1000+k*100+l*10+m)
    #                         for s in digits:
    #                             a+=1
    #                             # numberlist.append(i*100000+j*10000+k*1000+l*100+m*10+s)
    #                             for o in digits:
    #                                 a+=1
    #                                 # numberlist.append(i*1000000+j*100000+k*10000+l*1000+m*100+s*10+o)
    #                                 for p in digits:
    #                                     if i*10000000+j*1000000+k*100000+l*10000+m*1000+s*100+o*10+p<=n:
    #                                         a+=1
    #                                         # numberlist.append(i*10000000+j*1000000+k*100000+l*10000+m*1000+s*100+o*10+p)           
    # elif int(n/10)<100000000:
    #     for i in digits:
    #         a+=1
    #         # numberlist.append(i)
    #         for j in digits:
    #             a+=1
    #             # numberlist.append(i*10+j)
    #             for k in digits:
    #                 a+=1
    #                 # numberlist.append(i*100+j*10+k)
    #                 for l in digits:
    #                     a+=1
    #                     # numberlist.append((i*1000+j*100+k*10+l))
    #                     for m in digits:
    #                         a+=1
    #                         # numberlist.append(i*10000+j*1000+k*100+l*10+m)
    #                         for s in digits:
    #                             a+=1
    #                             # numberlist.append(i*100000+j*10000+k*1000+l*100+m*10+s)
    #                             for o in digits:
    #                                 a+=1
    #                                 # numberlist.append(i*1000000+j*100000+k*10000+l*1000+m*100+s*10+o)
    #                                 for p in digits:
    #                                     a+=1
    #                                         # numberlist.append(i*10000000+j*1000000+k*100000+l*10000+m*1000+s*100+o*10+p)    
    #                                     for q in digits:
    #                                         if i*100000000+j*10000000+k*1000000+l*100000+m*10000+s*1000+o*100+p*10+q<=n:
    #                                             a+=1
    #                                         # numberlist.append(i*100000000+j*10000000+k*1000000+l*100000+m*10000+s*1000+o*100+p*10+q) 
    # elif int(n/10)<1000000000:
    #     for i in digits:
    #         a+=1
    #         # numberlist.append(i)
    #         for j in digits:
    #             a+=1
    #             # numberlist.append(i*10+j)
    #             for k in digits:
    #                 a+=1
    #                 # numberlist.append(i*100+j*10+k)
    #                 for l in digits:
    #                     a+=1
    #                     # numberlist.append((i*1000+j*100+k*10+l))
    #                     for m in digits:
    #                         a+=1
    #                         # numberlist.append(i*10000+j*1000+k*100+l*10+m)
    #                         for s in digits:
    #                             a+=1
    #                             # numberlist.append(i*100000+j*10000+k*1000+l*100+m*10+s)
    #                             for o in digits:
    #                                 a+=1
    #                                 # numberlist.append(i*1000000+j*100000+k*10000+l*1000+m*100+s*10+o)
    #                                 for p in digits:
    #                                     a+=1
    #                                         # numberlist.append(i*10000000+j*1000000+k*100000+l*10000+m*1000+s*100+o*10+p)    
    #                                     for q in digits:
    #                                         a+=1
    #                                         # numberlist.append(i*100000000+j*10000000+k*1000000+l*100000+m*10000+s*1000+o*100+p*10+q) 
    #                                         for r in digits:
    #                                             if i*1000000000+j*100000000+k*10000000+l*1000000+m*100000+s*10000+o*1000+p*100+q*10+r<=n:
    #                                                 a+=1
    #                                             # numberlist.append(i*1000000000+j*100000000+k*10000000+l*1000000+m*100000+s*10000+o*1000+p*100+q*10+r) 
    # else:
    #     pass
    
    # print(int(n/10))
    # # numberlist=list(filter(lambda x:x<=n,numberlist))
    # # print(numberlist)

    # # return len(numberlist)
    # return a



# 本题为典型的数位动态规划题目。
# 我们称满足 x \le nx≤n 且仅包含 \textit{digits}digits 中出现的数字的 xx 为合法的，则本题需要找出所有合法的 xx 的个数。
# 设 nn 是一个十进制的 kk 位数，所有数字位数小于 kk 且由 \textit{digits}digits 组成的数字则一定是小于 nn 的。我们用 \textit{dp}[i][0]dp[i][0] 表示由 \textit{digits}digits 构成且 nn 的前 ii 位的数字的个数，dp[i][1]dp[i][1] 表示由 \textit{digits}digits 构成且等于 nn 的前 ii 位的数字的个数，可知 \textit{dp}[i][1]dp[i][1] 的取值只能为 00 和 11。
# 例如：n = 2345, \textit{digits} = \text{[``1",``2",``3",``4"]}n=2345,digits=[“1",“2",“3",“4"]。
# 则 \textit{dp}[1][0], \textit{dp}[2][0], \textit{dp}[3][0], \textit{dp}[4][0]dp[1][0],dp[2][0],dp[3][0],dp[4][0] 分别表示小于 2, 23, 234, 23452,23,234,2345 的合法数的个数，\textit{dp}[1][1], \textit{dp}[2][1], \textit{dp}[3][1], \textit{dp}[4][1]dp[1][1],dp[2][1],dp[3][1],dp[4][1] 分别表示等于 2, 23, 234, 23452,23,234,2345 的合法数的个数。
# 设 \textit{digits}digits 中的字符数目为 mm 个，数字 nn 的前 jj 位构成的数字为 \textit{num}[j]num[j]，数字 nn 的第 jj 个字符为 s[j]s[j]，当遍历到 nn 的第 ii 位时：
# 当满足 i > 1i>1 时，此时任意数字 dd 构成的数字一定满足 d < \textit{num}[i]d<num[i]；
# 设数字 a < \textit{num}[i-1]a<num[i−1]，则此时在 aa 的末尾追加一个数字 dd 构成的数为 a \times 10 + da×10+d，此时可以知道 dd 取 0,1,\cdots,90,1,⋯,9 中任意数字均满足小于 a \times 10 + d < \textit{num}[i] = \textit{num}[i-1] \times 10 + s[i]a×10+d<num[i]=num[i−1]×10+s[i]；
# 设数字 a = \textit{num}[i-1]a=num[i−1]，则此时在 aa 的末尾追加一个数字 dd 构成的数为 a \times 10 + da×10+d，此时可以知道 d < s[i]d<s[i] 时，才能满足 a \times 10 + d < \textit{num}[i] = \textit{num}[i-1] \times 10 + s[i]a×10+d<num[i]=num[i−1]×10+s[i]；
# 初始化时令 \textit{dp}[0][1] = 1dp[0][1]=1，如果前 ii 位中存在某一位 jj ，对于任意数字 dd 均不能满足 d = s[j]d=s[j]，则此时 \textit{dp}[i][1] = 0dp[i][1]=0；
# 根据上述描述从小到到计算 dpdp，设 C[i]C[i] 表示数组 \textit{digits}digits 中小于 nn 的第 ii 位数字的元素个数，则状态转移方程为：
# dp[i][0] = \begin{cases} C[i], & i = 1 \\ m + dp[i-1][0] \times m + dp[i-1][1] \times C[i], & i > 1 \\ \end{cases}
# dp[i][0]={ 
# C[i],
# m+dp[i−1][0]×m+dp[i−1][1]×C[i],
# ​
  
# i=1
# i>1
# 

# 我们计算出前 kk 位小于 nn 的数字的个数 \textit{dp}[k][0]dp[k][0]，前 kk 位等于 nn 的数字的个数 \textit{dp}[k][1]dp[k][1]，最终的答案为 \textit{dp}[k][0] + \textit{dp}[k][1]dp[k][0]+dp[k][1]。


    m = len(digits)
    s = str(n)
    k = len(s)
    dp = [[0, 0] for _ in range(k + 1)]
    print(dp)
    dp[0][1] = 1
    print(dp)
    for i in range(1, k + 1):
        for d in digits:
            print('d=',d)
            print('s[i-1]=',s[i-1])
            if d == s[i - 1]:
                dp[i][1] = dp[i - 1][1]
            elif d < s[i - 1]:
                dp[i][0] += dp[i - 1][1]
            else:
                break
        if i > 1:
            dp[i][0] += m + dp[i - 1][0] * m
    print(dp)
    return sum(dp[k])


print(atMostNGivenDigitSet(["1","3","5","7"],100))