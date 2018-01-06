# object-oriented programming

# access protected
# 在变量前加__(两个下划线)


class Student(object):
    def __init__(self):
        pass
    
    def __str__(self):
        return 'Student'


print(Student())
s = Student()
print(s)
