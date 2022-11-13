from class_define import School
from class_define import People
from class_define import Student
from class_define import Teacher
from class_define import Employee
from class_define import Accountant
from class_define import Logistics
from class_define import Management
from class_define import Course
from function_define import PeopleList
from function_define import CourseList

# 已有内容
# 总部和三个分校区
NK=School("南开大学","天津",366)
NKTD=School("南开大学泰达校区","滨海新区",6)
NKJN=School("南开大学津南校区","津南区",240)
NKBLT=School("南开大学八里台校区","八里台校区",120)
# 已有课程
c_python=Course("Python",16,30)
c_lisan=Course("离散数学",16,25)
c_xiandai=Course("线性代数",16,25)
c_mayuan=Course("马克思主义原理",8,10)
c_weiguan=Course("微观经济学",16,25)
c_hongguan=Course("宏观经济学",16,25)
c_guanli=Course("管理学",16,25)
c_fali=Course("法理学",16,20)
c_xingfa=Course("刑法总论",16,20)
# 已有教师
t1=Teacher("Gao","01","泰达校区",c_lisan,c_xiandai)
t2=Teacher("Wang","02","泰达校区",c_python)
t3=Teacher("Huang","03","津南校区",c_mayuan)
t4=Teacher("Zhang","04","八里台校区",c_hongguan,c_weiguan)
t5=Teacher("Jiao","05","八里台校区",c_guanli)
t6=Teacher("Jia","06","津南校区",c_fali)
t7=Teacher("Qiang","07","津南校区",c_xingfa)
# 已有学生
s1=Student("Mike","0001","泰达校区","软件工程",c_mayuan,c_python,c_lisan,c_xiandai)
s2=Student("Will","0002","八里台校区","经济学",c_mayuan,c_xiandai,c_hongguan,c_weiguan)
s3=Student("Jack","0003","八里台校区","工商管理",c_mayuan,c_guanli)
s4=Student("El","0004","津南校区","刑法",c_mayuan,c_fali,c_xingfa)
s5=Student("Joyce","0005","八里台校区","财政学",c_mayuan,c_hongguan,c_weiguan)
s6=Student("Jasen","0006","津南校区","金融学",c_mayuan,c_hongguan,c_weiguan,c_xiandai)
s7=Student("John","0007","八里台校区","工商管理",c_mayuan,c_guanli)
s8=Student("Laura","0008","八里台校区","财务管理",c_mayuan,c_guanli,c_xiandai)
s9=Student("Jay","0009","津南校区","法理",c_mayuan,c_fali,c_xingfa)
s10=Student("Li","0010","泰达校区","软件工程",c_mayuan,c_python,c_lisan,c_xiandai)
s11=Student("May","0011","泰达校区","软件工程",c_mayuan,c_python,c_lisan,c_xiandai)
s12=Student("Sally","0012","津南校区","金融学",c_mayuan,c_hongguan,c_weiguan,c_xiandai)
# 已有员工
e1=Logistics("A","001","泰达校区")
e2=Management("B","002","泰达校区")
e3=Accountant("D","003","津南校区")
e4=Logistics("E","004","津南校区")
e5=Logistics("F","005","津南校区")
e6=Management("H","006","津南校区")
e7=Accountant("I","007","八里台校区")
e8=Logistics("J","008","八里台校区")
e9=Management("K","009","八里台校区")
e10=Management("I","010","八里台校区")

c=CourseList()
c.add(c_python,c_lisan,c_xiandai,c_mayuan,c_weiguan,c_hongguan,c_guanli,c_fali,c_xingfa)

# 建立学生/老师/员工名单
p=PeopleList()
p.add(t1,t2,t3,t4,t5,t6,t7,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10)
# 分校区添加
def school_add_student(s:Student):
    NK.add_student(s)
    if s.school=="泰达校区":
        NKTD.add_student(s)
    if s.school=="津南校区":
        NKJN.add_student(s)
    if s.school=="八里台校区":
        NKBLT.add_student(s)

def school_add_teacher(t:Teacher):
    NK.add_teacher(t)
    if t.school=="泰达校区":
        NKTD.add_teacher(t)
    if t.school=="津南校区":
        NKJN.add_teacher(t)
    if t.school=="八里台校区":
        NKBLT.add_teacher(t)

def school_add_employee(e:Employee):
    NK.add_employee(e)
    if e.school=="泰达校区":
        NKTD.add_employee(e)
    if e.school=="津南校区":
        NKJN.add_employee(e)
    if e.school=="八里台校区":
        NKBLT.add_employee(e)

# 分校区删除
def school_del_student(s:Student):
    NK.del_student(s)
    if s.school=="泰达校区":
        NKTD.del_student(s)
    if s.school=="津南校区":
        NKJN.del_student(s)
    if s.school=="八里台校区":
        NKBLT.del_student(s)

def school_del_teacher(t:Teacher):
    NK.del_teacher(t)
    if t.school=="泰达校区":
        NKTD.del_teacher(t)
    if t.school=="津南校区":
        NKJN.del_teacher(t)
    if t.school=="八里台校区":
        NKBLT.del_teacher(t)

def school_del_employee(e:Employee):
    NK.del_employee(e)
    if e.school=="泰达校区":
        NKTD.del_employee(e)
    if e.school=="津南校区":
        NKJN.del_employee(e)
    if e.school=="八里台校区":
        NKBLT.del_employee(e)

# 添加已有的
for s in p.get_people_list("Student"):
    school_add_student(s) 
for t in p.get_people_list("Teacher"):
    school_add_teacher(t) 
for e in p.get_people_list("Employee"):
    school_add_employee(e) 

# 计算老师的工资：sum(所授课程对应的课时*单价*50%*学生人数)
def cal_salary(t:Teacher):
    salary=0
    for course in t.courses:
        for s in NK.student_list:
            if course in s.courses:
                salary+=course.hours*course.price*0.5
    return salary

def add_salary(t:Teacher,salary):
    t.set_salary(salary)

for t in p.get_people_list("Teacher"):
    add_salary(t,cal_salary(t))    


# 主程序--------------------------------------------------------------------------------
is_flag=True
while is_flag==True:
    print("------------欢迎登录南开大学系统------------")
    print("南开大学一共包括三个校区: 泰达校区,津南校区,八里台校区")
    print(f"三个校区的占地面积分别为: {NKTD.area}万平方米,{NKJN.area}万平方米,{NKBLT.area}万平方米")
    print("请选择操作")
    print("1.查询各校区人数")
    print("2.查询各校区账户")
    print("3.查看已有课程")
    print("4.查看学生名单")
    print("5.查看老师名单")
    print("6.查看员工名单")
    print("7.增加/删除学生")
    print("8.增加/删除老师")
    print("9.增加/删除员工")
    print("10.增加/删除课程")
    print("0.退出系统")
    choice=input()
    if choice=="1":
        print("学生人数:")
        print(f"南开大学一共有学生{NK.get_student_num()}人")
        print(f"泰达校区有学生{NKTD.get_student_num()}人")
        print(f"津南校区有学生{NKJN.get_student_num()}人")
        print(f"八里台校区有学生{NKBLT.get_student_num()}人")
        print("教师人数:")
        print(f"南开大学一共有教师{NK.get_teacher_num()}人")
        print(f"泰达校区有教师{NKTD.get_teacher_num()}人")
        print(f"津南校区有教师{NKJN.get_teacher_num()}人")
        print(f"八里台校区有教师{NKBLT.get_teacher_num()}人")
        print("员工人数:")
        print(f"南开大学一共有员工{NK.get_employee_num()}人")
        print(f"泰达校区有员工{NKTD.get_employee_num()}人")
        print(f"津南校区有员工{NKJN.get_employee_num()}人")
        print(f"八里台校区有员工{NKBLT.get_employee_num()}人")
    if choice=="2":
        print("账户收入:")
        print(f"南开大学总收入{NK.get_balance_income()}元")
        print(f"泰达校区收入{NKTD.get_balance_income()}元")
        print(f"津南校区收入{NKJN.get_balance_income()}元")
        print(f"八里台校区收入{NKBLT.get_balance_income()}元")
        print("账户支出:")
        print(f"南开大学总支出{NK.get_balance_outcome()}元")
        print(f"泰达校区支出{NKTD.get_balance_outcome()}元")
        print(f"津南校区支出{NKJN.get_balance_outcome()}元")
        print(f"八里台校区支出{NKBLT.get_balance_outcome()}元")
        print("账户余额:")
        print(f"南开大学总余额{NK.get_balance()}元")
        print(f"泰达校区余额{NKTD.get_balance()}元")
        print(f"津南校区余额{NKJN.get_balance()}元")
        print(f"八里台校区余额{NKBLT.get_balance()}元")
    if choice=="3":
        print(f"南开大学目前已开设{c.get_courses_num()}门课程:")
        for course in c.get_course_list():
            course_teacher=[]
            course_student=[]
            for t in NK.teacher_list:
                if course.name in [course_t.name for course_t in t.courses]:
                    course_teacher.append(t.name)
            for s in NK.student_list:
                if course.name in [course_s.name for course_s in s.courses]:
                    course_student.append(s.name)
            print(f"课程：{course.name}，课时：{course.hours}周，单价：{course.price}元/周，授课教师：{course_teacher}，选课学生：{course_student}")
    if choice=="4":
        print("请选择校区:")
        school=input()
        if school=="南开大学":
            for s in NK.student_list:
                print(f"学生:{s.name},ID:{s.ID},校区:{s.school},专业:{s.major},所选课程:{[course.name for course in s.courses]}")
        elif school=="泰达校区":
            for s in NKTD.student_list:
                print(f"学生:{s.name},ID:{s.ID},校区:{s.school},专业:{s.major},所选课程:{[course.name for course in s.courses]}")
        elif school=="津南校区":
            for s in NKJN.student_list:
                print(f"学生:{s.name},ID:{s.ID},校区:{s.school},专业:{s.major},所选课程:{[course.name for course in s.courses]}")
        elif school=="八里台校区":
            for s in NKBLT.student_list:
                print(f"学生:{s.name},ID:{s.ID},校区:{s.school},专业:{s.major},所选课程:{[course.name for course in s.courses]}")
    if choice=="5":
        print("请选择校区:")
        school=input()
        if school=="南开大学":
            for t in NK.teacher_list:
                print(f"教师:{s.name},ID:{s.ID},校区:{s.school},所授课程:{[course.name for course in t.courses]}")
        elif school=="泰达校区":
            for t in NKTD.teacher_list:
                print(f"教师:{s.name},ID:{s.ID},校区:{s.school},所授课程:{[course.name for course in t.courses]}")
        elif school=="津南校区":
            for t in NKJN.teacher_list:
                print(f"教师:{s.name},ID:{s.ID},校区:{s.school},所授课程:{[course.name for course in t.courses]}")
        elif school=="八里台校区":
            for t in NKBLT.teacher_list:
                print(f"教师:{s.name},ID:{s.ID},校区:{s.school},所授课程:{[course.name for course in t.courses]}")
    if choice=="6":
        print("请选择校区:")
        school=input()
        if school=="南开大学":
            for e in NK.employee_list:
                print(f"员工:{e.name},ID:{e.ID},校区:{e.school},工作类型:{e.job}")
        elif school=="泰达校区":
            for e in NKTD.employee_list:
                print(f"员工:{e.name},ID:{e.ID},校区:{e.school},工作类型:{e.job}")
        elif school=="津南校区":
            for e in NKJN.employee_list:
                print(f"员工:{e.name},ID:{e.ID},校区:{e.school},工作类型:{e.job}")
        elif school=="八里台校区":
            for e in NKBLT.employee_list:
                print(f"员工:{e.name},ID:{e.ID},校区:{e.school},工作类型:{e.job}")
    if choice=="7":
        print("请选择增加(a)还是删除(d)学生:")
        choice_7=input()
        if choice_7=="a":
            print("请输入姓名:")
            name=input()
            print("请输入ID:")
            ID=input()
            print("请输入校区:")
            school=input()
            print("请输入专业:")
            major=input()
            print("请输入所选课程名称:")
            courses=input()
            cour=courses.split( )
            course_list=[]
            print(cour)
            for co in cour:
                for cou in c.get_course_list():
                    if cou.name==co: 
                        course_list.append(cou)
            # print(course_list)
            course_tuple=tuple(course_list)
            student_new=Student(name,ID,school,major,course_tuple)
            student_new.courses=course_tuple
            # print(student_new.courses)
            school_add_student(student_new)
        if choice_7=="d":
            print("请输入要删除的学生ID:")
            ID_del=input()
            for s in NK.student_list:
                if s.ID==ID_del:
                    school_del_student(s)
    if choice=="8":
        print("请选择增加(a)还是删除(d)老师:")
        choice_8=input()
        if choice_8=="a":
            print("请输入姓名:")
            name=input()
            print("请输入ID:")
            ID=input()
            print("请输入校区:")
            school=input()
            print("请输入所选课程名称:")
            courses=input()
            cour=courses.split( )
            course_list=[]
            print(cour)
            for co in cour:
                for cou in c.get_course_list():
                    if cou.name==co: 
                        course_list.append(cou)
            course_tuple=tuple(course_list)
            teacher_new=Teacher(name,ID,school,course_tuple)
            teacher_new.courses=course_tuple
            add_salary(teacher_new,cal_salary(teacher_new))
            school_add_teacher(teacher_new)
        if choice_8=="d":
            print("请输入要删除的教师ID:")
            ID_del=input()
            for t in NK.teacher_list:
                if t.ID==ID_del:
                    school_del_teacher(t)
    if choice=="9":
        print("请选择增加(a)还是删除(d)员工:")
        choice_9=input()
        if choice_9=="a":
            print("请输入姓名:")
            name=input()
            print("请输入ID:")
            ID=input()
            print("请输入校区:")
            school=input()
            print("请输入工作类型:")
            job=input()
            if job=="财务":
                employee_new=Accountant(name,ID,school)
            elif job=="后勤":
                employee_new=Logistics(name,ID,school)
            elif job=="行政":
                employee_new=Management(name,ID,school)
            school_add_employee(employee_new)
        if choice_9=="d":
            print("请输入要删除的员工ID:")
            ID_del=input()
            for e in NK.employee_list:
                if e.ID==ID_del:
                    school_del_employee(e)    
    if choice=="10":
        print("请选择增加(a)还是删除(d)课程:")
        choice_10=input()
        if choice_10=="a":
            print("请输入名称:")
            name=input()
            print("请输入课时:")
            hours=int(input())
            print("请输入单价:")
            price=int(input())
            course_new=Course(name,hours,price)
            c.add(course_new)
        if choice_10=="d":
            print("请输入要删除的课程名称:")
            name=input()
            for course in c.get_course_list():
                if course.name==name:
                    c.get_course_list().remove(course)

    if choice=="0":
        is_flag=False