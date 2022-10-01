# 展示系统功能
from re import T


def show():
    print('《通讯录管理系统》')
    print('a: 增加记录')
    print('d: 删除记录')
    print('c: 修改记录')
    print('f: 查找记录')
    print('s: 展示记录')
    print('e: 退出系统')

# 添加功能
def add():
    info=[]
    print('请输入姓名：')
    while True: 
        name=input()
        if name.isalpha()==True:
            info.append(name)
            break
        else:
            print('输入错误，请重新输入：')
        
    print('请输入QQ：')
    while True: 
        qq=input()
        if qq.isdigit()==True and 5<=len(qq)<=10:
            info.append(qq)
            break
        else:
            print('输入错误，请重新输入：')

    print('请输入电话：')
    while True: 
        phone=input()
        if phone.isdigit()==True and len(phone)==11:
            info.append(phone)
            break
        else:
            print('输入错误，请重新输入：')

    print('请输入邮箱：')
    while True: 
        email=input()
        if '@' in email and email.split('@')[0]==qq and email.split('@')[1]=='qq.com':
            info.append(email)
            break
        else:
            print('输入错误，请重新输入：') 
    
    print('增加成功')
    return info

information=[]
# 删除功能
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
def change(num):
    print('请输入要修改的子项：')
    print('n: 修改姓名')
    print('q: 修改QQ')
    print('p: 修改电话')
    print('m: 修改邮箱')
    while True:
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
            new_qq=input()
            if new_qq==' ':
                pass
            else:
                information[num-1][1]=new_qq
                print('修改成功')
            break
        elif choice1=='p':
            print('请输入新的电话，若不修改输入空格：')
            new_phone=input()
            if new_phone==' ':
                pass
            else:
                information[num-1][2]=new_phone
                print('修改成功')
            break
        elif choice1=='m':
            print('请输入新的邮箱，若不修改输入空格：')
            new_email=input()
            if new_email==' ':
                pass
            else:
                information[num-1][3]=new_email
                print('修改成功')
            break
        else:
            print('输入错误，请重新输入：')
    return information
    
# 查找功能
def find(num):
    print('查找成功，结果为：')
    print('--------------------------------------------------------------------------------')
    print('No.','\t','Name','\t','\t','QQ','\t','\t','Phone','\t','\t','Email')
    print(num,'\t',information[num-1][0],'\t','\t',information[num-1][1],'\t',information[num-1][2],'\t',information[num-1][3])
    print('--------------------------------------------------------------------------------')
    return information

# 展示功能
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
        info=add()
        information.append(info)
        print('--------------------------------------------------------------------------------')
        print('No.','\t','Name','\t','\t','QQ','\t','\t','Phone','\t','\t','Email')
        # print(information)
        i=0
        while i < len(information):
            print(i+1,'\t',information[i][0],'\t','\t',information[i][1],'\t',information[i][2],'\t',information[i][3])
            i+=1
        print('--------------------------------------------------------------------------------')

    elif choice=='d':
        print('请输入要删除的记录序号：')
        while True:
            num=int(input())
            if num<=0 or num>len(information):
                print('输入的序号不存在，请重新输入：')
            else:
                delete(num)
                break
    
    elif choice=='c':
        print('请输入要修改的记录序号：')
        while True:
            num=int(input())
            if num<=0 or num>len(information):
                print('输入的序号不存在，请重新输入：')
            else:
                change(num)
                break

    elif choice=='f':
        print('请输入要查找的记录序号：')
        while True:
            num=int(input())
            if num<=0 or num>len(information):
                print('输入的序号不存在，请重新输入：')
            else:
                find(num)
                break
    
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


