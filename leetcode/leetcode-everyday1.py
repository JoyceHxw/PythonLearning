
from collections import defaultdict


def totalFruit(fruits):
    # d1={}
    # for i in range(0,len(fruits)):
    #     if i-1>=0 and fruits[i-1]==fruits[i]:
    #         continue
    #     l1=[]
    #     s=0
    #     for j in range(i,len(fruits)):
    #         if fruits[j] in l1:
    #             pass
    #         else:
    #             l1.append(fruits[j])

    #         if len(l1)<=2:
    #             s+=1
    #         else:
    #             break

    #     print("i=",i)
    #     print("l1=",l1)   
    #     print("s=",s) 
    #     d1[i]=s
    #     print('index(i)=',i)
    #     print('d1=',d1)
    #     print('--------')
    
    # # l2=sorted(d1.items(),key=lambda x:x[1],reverse=True)
    # # print(l2)

    #     d1[i]=s
    #     m=max(d1.values())

    #     if len(fruits)-i-1<=m:
    #         break
    # # return l2[0][1]
    # return max(d1.values())


    n, ans = len(fruits), 0
    j, tot = 0, 0
    cnts = defaultdict(int)
    for i in range(n):
        cnts[fruits[i]] += 1
        if cnts[fruits[i]] == 1:
            tot += 1
        while tot > 2:
            cnts[fruits[j]] -= 1
            if cnts[fruits[j]] == 0:
                tot -= 1
            j += 1
        ans = max(ans, i - j + 1)
        print('i=',i)
        print('j=',j)
        print('tot=',tot)
        print('ans=',ans)
        print('i-j+1=',i-j+1)
        print(cnts)
        print('------------------------')
    return ans

fruits=[7,8,8,9,9,10,10,10,11,12,12]
print(totalFruit(fruits))

