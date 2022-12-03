from datetime import datetime
import os


# 读取并用字典数据结构储存用户名密码
t=open('user_info.txt',encoding='utf-8')
txt=t.read()
lst=txt.split('\n')
lst2=[]
for w in lst:
    lst1=w.split( )
    # print(lst1)
    lst2.append(lst1)
dic=dict(lst2)
dic.pop('user_name')
dic1={i:0 for i in dic.keys()}


# 验证用户是否登录
def authorization(fn):
    def inner(*args):
        s=0
        for i in dic1.values():
            s+=i
        if s==0:
            print("您未登录，请输入用户名（输入-1则退出登录）：")
            is_flag1=True
            while is_flag1==True:
                username=input()
                if username=="-1":
                    print("您退出了登录！")
                    is_flag1=False
                elif username in dic.keys():
                    print("用户名输入正确，请继续输入密码：")
                    is_flag2=True
                    while is_flag2==True:
                        password=input()
                        if password==dic[username]:
                            print("登录成功！")
                            fn(*args)
                            dic1[username]=1
                            # print(dic1)
                            is_flag2=False
                            is_flag1=False
                        else:
                            print("密码输入错误，请重新输入：")
                else:
                    print("用户名输入错误，请重新输入：")
                
        elif s>0:
            print("您已登录！")
            fn(*args)
            
    return inner

# @authorization
# def hello():
#     print("hello")

# hello()

# 创建txt文档
filepath=os.getcwd()
filename='log'
filepath=filepath+'\\'+filename+'.txt'
file=open(filepath,'w')

# 日志装饰器
def logger(fn):
    def inner(*args):
        called_at=datetime.now()
        to_execute=fn(*args)
        file.write(f'{fn.__name__} executed. Logged at {called_at} \n')
        return to_execute
    return inner


information=[]
# 展示系统功能
def show():
    print('《通讯录管理系统》')
    print('a: 增加记录')
    print('d: 删除记录')
    print('c: 修改记录')
    print('f: 查找记录')
    print('s: 展示记录')
    print('e: 退出系统')

# 添加功能
@authorization
@logger
def add():
    info=[]
    print('请输入姓名（输入-1则退出该功能）：')
    while True: 
        name=input()
        if name=="-1":
            return None
        elif name.isalpha()==True:
            info.append(name)
            break
        else:
            print('输入错误，请重新输入：')
        
    print('请输入QQ（输入-1则退出该功能）：')
    while True: 
        qq=input()
        if qq=="-1":
            return None
        # -------------------------------try-except-------------------------------
        try: 
            int(qq)
            if 5<=len(qq)<=10:
                info.append(qq)
                break
            else:
                print("输入长度错误，请重新输入：")
        except ValueError:
            print('输入格式错误，请重新输入：')

    print('请输入电话（输入-1则退出该功能）：')
    while True: 
        phone=input()
        if phone=="-1":
            return None
        # -------------------------------try-except-------------------------------
        try:
            int(phone)
            if len(phone)==11:
                info.append(phone)
                break
            else:
                print('输入长度错误，请重新输入：')
        except ValueError:
            print('输入格式错误，请重新输入')

    print('请输入邮箱（输入-1则退出该功能）：')
    while True: 
        email=input()
        if email=="-1":
            return None
        elif '@' in email and email.split('@')[0]==qq and email.split('@')[1]=='qq.com':
            info.append(email)
            break
        else:
            print('输入错误，请重新输入：') 
    
    print('增加成功')
    information.append(info)
    return info

# 删除功能
@authorization
@logger
def delete(num):
    print('您确认要删除该条记录吗？（y/n）')
    while True:
        yn=input()
        if yn=='y':
            del information[num-1]
            print('删除成功')
            break
        elif yn=='n':
            break
        else:
            print('错误输入，请重新输入：')
    return information

# 修改功能
@authorization
@logger
def change(num):
    print('请输入要修改的子项：')
    print('n: 修改姓名')
    print('q: 修改QQ')
    print('p: 修改电话')
    print('m: 修改邮箱')
    print('-1: 退出该功能')
    is_Flag2=True
    while is_Flag2:
        choice1=input()
        if choice1=='n':
            print('请输入新的姓名，若不修改输入空格：')
            new_name=input()
            if new_name==' ':
                pass
            else:
                information[num-1][0]=new_name
                print('修改成功')
            break
        elif choice1=='q':
            print('请输入新的QQ，若不修改输入空格：')
            while True:
                new_qq=input()
                if new_qq==' ':
                    pass
                else:
                    # -------------------------------try-except-------------------------------
                    try: 
                        int(new_qq)
                        if 5<=len(new_qq)<=10:
                            information[num-1][1]=new_qq
                            print('修改成功')
                            is_Flag2=False
                            break
                        else:
                            print("输入长度错误，请重新输入：")
                    except ValueError:
                        print('输入格式错误，请重新输入：')
                # break
        elif choice1=='p':
            print('请输入新的电话，若不修改输入空格：')
            while True:
                new_phone=input()
                if new_phone==' ':
                    pass
                else:
                    # -------------------------------try-except-------------------------------
                    try:
                        int(new_phone)
                        if len(new_phone)==11:
                            information[num-1][2]=new_phone
                            print('修改成功')
                            is_Flag2=False
                            break
                        else:
                            print('输入长度错误，请重新输入：')
                    except ValueError:
                        print('输入格式错误，请重新输入')
        elif choice1=='m':
            print('请输入新的邮箱，若不修改输入空格：')
            new_email=input()
            if new_email==' ':
                pass
            else:
                information[num-1][3]=new_email
                print('修改成功')
            break
        elif choice1=="-1":
            break
        else:
            print('输入错误，请重新输入：')
    return information
    
# 查找功能
@authorization
@logger
def find(num):
    print('查找成功，结果为：')
    print('--------------------------------------------------------------------------------')
    print('No.','\t','Name','\t','\t','QQ','\t','\t','Phone','\t','\t','Email')
    print(num,'\t',information[num-1][0],'\t','\t',information[num-1][1],'\t',information[num-1][2],'\t',information[num-1][3])
    print('--------------------------------------------------------------------------------')
    return information

# 展示功能
@authorization
@logger
def show_info():
    print('--------------------------------------------------------------------------------')
    print('No.','\t','Name','\t','\t','QQ','\t','\t','Phone','\t','\t','Email')
    i=0
    while i < len(information):
        print(i+1,'\t',information[i][0],'\t','\t',information[i][1],'\t',information[i][2],'\t',information[i][3])
        i+=1
    print('--------------------------------------------------------------------------------')
    return information



# ----------------------------------------------------------------------------
# 运行代码
is_Flag=True
while is_Flag:
    show()
    print('请输入功能对应的代号：')
    choice=input()

    if choice=='a':
        add()
        print('--------------------------------------------------------------------------------')
        print('No.','\t','Name','\t','\t','QQ','\t','\t','Phone','\t','\t','Email')
        # print(information)
        i=0
        while i < len(information):
            print(i+1,'\t',information[i][0],'\t','\t',information[i][1],'\t',information[i][2],'\t',information[i][3])
            i+=1
        print('--------------------------------------------------------------------------------')

    elif choice=='d':
        print('请输入要删除的记录序号（输入-1则退出该功能）：')
        while True:
            # -------------------------------try-except-------------------------------
            try:
                num=int(input())
                if num==-1:
                    break
                elif num<=0 or num>len(information):
                    print('输入的序号不存在，请重新输入：')
                else:
                    delete(num)
                    break
            except ValueError:
                print("输入格式错误，请重新输入")
    
    elif choice=='c':
        print('请输入要修改的记录序号（输入-1则退出该功能）：')
        while True:
            # -------------------------------try-except-------------------------------
            try:
                num=int(input())
                if num==-1:
                    break
                elif num<=0 or num>len(information):
                    print('输入的序号不存在，请重新输入：')
                else:
                    change(num)
                    break
            except ValueError:
                print("输入格式错误，请重新输入")

    elif choice=='f':
        print('请输入要查找的记录序号（输入-1则退出该功能）：')
        while True:
            # -------------------------------try-except-------------------------------
            try:
                num=int(input())
                try:
                    if num==-1:
                        break
                    information[num-1]
                    find(num)
                    break
                except IndexError:
                    print("输入的序号不存在，请重新输入：")
            except ValueError:
                print("输入格式错误，请重新输入")
    
    elif choice=='s':
        show_info()

    elif choice=='e':
        print('您确定要退出系统吗？（y/n）')
        is_Flag1=True
        while is_Flag1:
            yn2=input()
            if yn2=='y':
                is_Flag1=False
                is_Flag=False
            elif yn2=='n':
                is_Flag1=False
            else:
                print('错误输入，请重新输入：')

    else:
        print('错误输入，请重新输入：')