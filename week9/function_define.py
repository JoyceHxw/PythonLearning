from class_define import School
from class_define import People
from class_define import Student
from class_define import Teacher
from class_define import Employee
from class_define import Course

class PeopleList:
    def __init__(self,student_lst=None,teacher_lst=None,employee_lst=None) -> None:
        if student_lst is None:
            self.student_lst=[]
        if teacher_lst is None:
            self.teacher_lst=[]
        if employee_lst is None:
            self.employee_lst=[]
    
    def add(self,*args:People):
        for a in args:
            if a.__class__.__name__=="Student":
                self.student_lst.append(a)
            if a.__class__.__name__=="Teacher":
                self.teacher_lst.append(a)
            if a.__class__.__name__ in ("Accountant","Logistics","Management"):
                self.employee_lst.append(a)
            # NK.add_student(a)
            # if s.school=="泰达校区":
            #     NKTD.add_student(s)
            # if s.school=="津南校区":
            #     NKJN.add_student(s)
            # if s.school=="八里台校区":
            #     NKBLT.add_student(s)

    def delete(self,p):
        if p.__class__.__name__=="Student":
                self.student_lst.remove(p)
        if p.__class__.__name__=="Teacher":
            self.teacher_lst.remove(p)
        if p.__class__.__name__ in ("Accountant","Logistics","Management"):
            self.employee_lst.remove(p)

    def get_people_list(self,identity):
        if identity=="Student":
            return self.student_lst
        if identity=="Teacher":
            return self.teacher_lst
        if identity=="Employee":
            return self.employee_lst

    def get_people_num(self,identity):
        if identity=="Student":
            return len(self.student_lst)
        if identity=="Teacher":
            return len(self.teacher_lst)
        if identity=="Employee":
            return len(self.employee_lst)

class CourseList:
    def __init__(self,lst=None) -> None:
        if lst is None:
            self.lst=[]

    def add(self,*args:Course):
        for a in args:
            self.lst.append(a)

    def delete(self,c):
        self.lst.remove(c)

    def get_course_list(self):
        return self.lst

    def get_courses_num(self):
        return len(self.lst)

