# 可迭代对象：每次能返回一个成员的对象（实现了__iter__()或__getitem__()）
#       包括：序列对象（list, str, tuple）和非序列对象（dict, file, objects）
#       可迭代对象可用于for循环，以及其他需要序列的地方（如zip()，map()）
# 迭代器：用来表示一连串数据流的对象（包含方法__iter__()和__next__()）

# 生成器是特殊的迭代器：生成器表达式，生成器函数
# 想要对生成器进行迭代有以下几种方法：
#       第一种：for循环，for循环的本质就是调用了iter和next方法进行了迭代
#       第二种：调用next方法
#       第三种：调用send方法
#       第四种：数据类型强制转换，比如使用list()强制转换。
l=[i*2 for i in range(10) if i%2==0]  # 列表表达式
s={i*2 for i in "abcd"}   # 集合表达式
d={k: v for k, v in zip(("one","two","three"),(1,2,3))}  # 字典表达式
g=(i*i for i in range(10))   # 生成器表达式
print(l)
print(s)
print(d)
print(g)   # <generator object <genexpr> at 0x000002A5CBDB9A10>


# example1
def add(n,i):
    return n+i

def test():
    for i in range(4):
        yield i
# 生成器函数，yield会记住当前位置执行状态，当该生成器恢复时，继续执行

g=test()
for n in [1,10]:
    g=(add(n,i) for i in g)   # 生成器表达式，不进行运算
print(list(g))  # 数据类型强制转换，比如使用list()强制转换，触发生成器进行迭代
# 当执行print(list(g))语句时，生成器才开始输出数据，此时执行最后一个g的赋值语句:
# g=(add(n,i) for i in (add(n,i) for i in test()))
# 这时 n 的值等于10（因为代码是按照流程执行的，for循环已经执行完了，n的最终结果就是10），其中后面的(add(n,i) for i in test())这段代码的结果依然是个生成器，迭代后应为[10,11,12,13]

# example2
def flatten_list(nested):
    if isinstance(nested,list):
        for sublist in nested:
            print("ccc")
            for item in flatten_list(sublist):
                print("ppp")
                yield item
                print("yyy")
    else:
        print("uuu")
        yield nested
        print("xxx")

def main():
    raw_list=["a",["b","c",["d"]]]
    g=flatten_list(raw_list)
    print(next(g),1111)
    print(next(g),2222)
    print(next(g),3333)
    print(next(g),4444)
    print("flatten_list is: ", list(flatten_list(raw_list))) 

main()


# example3
# 生成器对象」的send(value)函数会恢复执行「生成器函数」，同时把参数作为当前恢复的「yield表达式」的返回值，
# 而next()（其内部调用了「生成器对象」的__next__()函数）相等于send(None)，即，当通过next()恢复时，当前恢复的「yield表达式」的值为None。
# generator.throw(type[,value[,traceback]])：从「生成器函数」挂起的地方抛出一个type类型的异常，并返回下一个「yield值」，如果「生成器函数」没有返回「yield值」就退出了，那么会抛出StopIteration异常。
# generator.close()：从「生成器函数」挂起的地方抛出一个GeneratorExit异常。如果此 后「生成器函数」正常执行结束则关闭(此时抛出的GeneratorExit异常被捕获了)，如果继续返回「yield值」则会抛出RuntimeError。
def echo(value=None):
    print("Execution starts when 'next()' is called for the first time.")
    try:
        while True:
            try:
                value=(yield value)
                print("*****")
            except Exception as e:
                value=e
    finally: 
        print("Don't forget to clean up when 'close()' is called.")

generator=echo(1)
print(next(generator))
print(next(generator))
print(generator.send(2))
print(generator.throw(TypeError, "spam"))
generator.close