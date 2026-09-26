#inheritance code 

class College:
    def __init__(self,name, rollno, subjects):
        self.name=name
        self.rollno=rollno
        self.subjects=subjects


class student(College):
    def show_data(self):
        print(f"The name of student is {self.name} and roll no is {self.rollno} and subject are :{self.subjects} ") 


stud1=student("Pratik", 63, "java")
stud1.show_data()




# data abstractions 

from abc import ABC, abstractmethod

class animals(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Lion(animals):
    def make_sound(self):
        print("The Lions Roar !")

l1=Lion()
l1.make_sound()


        


