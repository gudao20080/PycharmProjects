
class Student(object):
    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age

    @classmethod
    def do_stu(cls, name, age):
        stu = cls(name, age)
        print(stu)

    def __str__(self) -> str:
        return "name: " + self._name + ", age " + str(self._age)


stu = Student.do_stu("wang", 999)
