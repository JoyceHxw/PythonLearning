# 定义类--------------------------------------------------------------------
# 一、课程
class Course:
    def __init__(self,name,hours,price) -> None:
        self.name=name
        self.hours=hours
        self.price=price


# 二、人员
class People:
    def __init__(self,name,ID,school) -> None:
        self.name=name
        self.ID=ID
        self.school=school
    
    def identity(self):
        print(f"I am {self.__class__.__name__}")

# 1.学生
class Student(People):
    def __init__(self, name, ID, school,major,*courses) -> None:
        super().__init__(name, ID, school)
        self.major=major
        self.courses=courses

    def identity(self):
        return super().identity()

# 2.老师
class Teacher(People):
    __salary=0
    # all_student_list=[]

    def __init__(self, name, ID, school,*courses) -> None:
        super().__init__(name, ID, school)
        self.courses=courses
    
    def identity(self):
        return super().identity()
    
    def set_salary(self,salary):
        self.__salary=salary
        return self.__salary
    
    def get_salary(self):
        return self.__salary

# 3.员工
class Employee(People):
    def __init__(self, name, ID, school,job,salary) -> None:
        super().__init__(name, ID, school)
        self.job=job
        self.salary=salary
        
    def identity(self):
        return super().identity()
    
    def get_salary(self):
        return self.salary

class Accountant(Employee):
    def __init__(self, name, ID, school, job="财务", salary=500) -> None:
        super().__init__(name, ID, school, job, salary)

    def identity(self):
        print(f"I am {self.job}")
    
    def get_salary(self):
        return super().get_salary()

class Logistics(Employee):
    def __init__(self, name, ID, school, job="后勤", salary=350) -> None:
        super().__init__(name, ID, school, job, salary)
    
    def identity(self):
        print(f"I am {self.job}")
    
    def get_salary(self):
        return super().get_salary()

class Management(Employee):
    def __init__(self, name, ID, school, job="行政", salary=200) -> None:
        super().__init__(name, ID, school, job, salary)
    
    def identity(self):
        print(f"I am {self.job}")
    
    def get_salary(self):
        return super().get_salary()


# 三、校区
class School:
    __balance_income=0
    __balance_outcome=0
    __balance=0

    def __init__(self,name,location,area,student_list=None,teacher_list=None,employee_list=None) -> None:
        self.name=name
        self.location=location
        self.area=area
        if student_list is None:
            self.student_list=[]
        if teacher_list is None:
            self.teacher_list=[]
        if employee_list is None:
            self.employee_list=[]
    
    def add_student(self,student:Student):
        self.student_list.append(student)
        return self.student_list
    def add_teacher(self,teacher:Teacher):
        self.teacher_list.append(teacher)
        return self.teacher_list
    def add_employee(self,employee:Employee):
        self.employee_list.append(employee)
    
    def del_student(self,student:Student):
        self.student_list.remove(student)
        return self.student_list
    def del_teacher(self,teacher:Teacher):
        self.teacher_list.remove(teacher)
        return self.teacher_list
    def del_employee(self,employee:Employee):
        self.employee_list.remove(employee)

    def get_student_num(self):
        return len(self.student_list)
    def get_teacher_num(self):
        return len(self.teacher_list)
    def get_employee_num(self):
        return len(self.employee_list)
        
    def get_balance_income(self):
        self.__balance_income=0
        for s in self.student_list:
            sum_stu=0
            for course in s.courses:
                h=course.hours
                p=course.price
                fee=h*p
                sum_stu+=fee
            self.__balance_income+=sum_stu
        return self.__balance_income
    
    def get_balance_outcome(self):
        self.__balance_outcome=0
        for t in self.teacher_list:
            self.__balance_outcome+=t.get_salary()
        for e in self.employee_list:
            self.__balance_outcome+=e.get_salary()
        return self.__balance_outcome


    def get_balance(self):
        self.__balance=0
        self.__balance=self.__balance_income-self.__balance_outcome
        return self.__balance

