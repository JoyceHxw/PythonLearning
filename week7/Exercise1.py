from atexit import register


class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd


class Account:
    def __init__(self):
        self.user_list = [] # 用户列表，数据格式：[User 对象, User 对象, User 对象]
    
    def login(self):
        """
        用户登录，用户输入用户名和密码并去 self.user_list 中检查用户是否合法
        """
        lst=[]
        for user in self.user_list:
            lst1=[]
            lst1.append(user.name)
            lst1.append(user.pwd)
            lst.append(lst1)
        dic=dict(lst)
        print("请输入用户名:")
        name=input()
        print("请输入密码:")
        pwd=input()
        if name in dic.keys():
            if pwd==dic[name]:
                print("登录成功!")
                return True
            else:
                print("密码错误")
                return False
        else:
            print("用户名不存在")
            return False

    def register(self):
        """
        用户注册，动态创建 User 对象，并添加到 self.user_list 中
        """
        print("请输入您要创建的用户名:")
        name=input()
        print("请设置密码:")
        pwd=input()
        user=User(name,pwd)
        self.user_list.append(user)
        print("注册成功")

    def run(self):
        """
        主程序，先进行 2 次用户注册注册两个不同的用户，再进行用户登录（3 次重试机会）
        """
        self.register()
        self.register()
        cnt=1
        while cnt<=3:
            if self.login()==True:
                break
            else:
                print(f"您还有{3-cnt}次机会")
                cnt+=1


if __name__ == "__main__":
    obj = Account()
    obj.run()