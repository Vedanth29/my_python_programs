#using init constructor
class student:
    college = "AIET"

    def __init__(self,name,age):
        print('student is created')
        self.name = name
        self.age = age

    def info(self):
        print(f'the student {self.name} age:{self.age}')

    @staticmethod
    def greet():
        print(f'good morning sir')

    @staticmethod
    def sayhi():
        print('hello ,thank you')

vedanth =student('vedanth',20)
vedanth.info()
