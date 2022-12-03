# 1-----------------------------
list_1=[1,2,3,4] 
# print(list_1[20])
try:
    print(list_1[20])
except IndexError:
    print("Index out of bound!")

# 2-----------------------------
def fun():
    try:
        print('try--start')
        a=1/0
    except ValueError as ret:
        print(ret)
    finally:
        return 'finally'
print(fun())


# 3-----------------------------
# 返回finally的return
def func():
    try:
        return 123
    finally:
        return 321
print(func())


# 4-----------------------------
def func1():
    a=1
    try:
        a=a+10
    except:
        a=a+10
    else:
        a=a+10
    finally:
        a=a+10
    return a
print(func1())


# 5-----------------------------
def func2():
    try:
        return 123
    except:
        return 111
    else:
        print(222)
    finally:
        print(321)
print(func2())