
def next(price) -> int:
    result=[]
    print(price)
    for j in price:
        s=0
        if j==[]:
            s=None
        else:
            for i in range(0,price.index(j)+1):
                print(price.index(j))
                if (price[price.index(j)-i]==j or price[price.index(j)-i]<j) and price[price.index(j)-i]!=[] :
                    print(price[price.index(j)-i])
                    s+=1
                    print(s)
                else:
                    print('break')
                    break
        result.append(s)
        print(result)
    return s

# next([[],[28],[14],[28],[35],[46],[53],[66],[80],[87],[88]])
next([28,14,28,35,46,53,66,80,87,88])



# 我们用单调栈维护一个单调递减的价格序列，并且对于每个价格，存储一个 weight 表示它离上一个价格之间（即最近的一个大于它的价格之间）的天数。
# 如果是栈底的价格，则存储它本身对应的天数。例如 [11, 3, 9, 5, 6, 4, 7] 对应的单调栈为 (11, weight=1), (9, weight=2), (7, weight=4)。
# 当我们得到了新的一天的价格，例如 10，我们将所有栈中所有小于等于 10 的元素全部取出，将它们的 weight 进行累加，再加上 1 就得到了答案。在这之后，我们把 10 和它对应的 weight 放入栈中，得到 (11, weight=1), (10, weight=7)。
class StockSpanner(object):
    def __init__(self):
        self.stack = []

    def next(self, price):
        weight = 1
        if self.stack!=[]:
            print('最后一个',self.stack[-1])
        while self.stack and self.stack[-1][0] <= price:
            weight += self.stack.pop()[1]
            print('weight=',weight)
            # print(self.stack.pop())

        print('self.stack前=',self.stack)
        self.stack.append((price, weight))
        print('self.stack=',self.stack)
        return weight


