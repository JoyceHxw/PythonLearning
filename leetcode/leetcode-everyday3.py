
def countStudents(students: list[int], sandwiches: list[int]) -> int:
    while True:
        s1=len(students)
        for n in range(0,len(students)):
            print(len(students))
            if sandwiches[0]==students[0]:
                sandwiches=sandwiches[1:]
                students=students[1:]
            else:
                st1=students.pop(0)
                students.append(st1)
        s2=len(students)
        print('students=',students)
        print('sandwiches=',sandwiches)
        if s1==s2:
            break
    return len(students)

print(countStudents([1,1,0,0],[0,1,0,1]))

