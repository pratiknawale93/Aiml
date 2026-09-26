#The instance method and the class method 

class Student:
    college_name= "The new English School"

    def __init__(self, name,gpa): #instance
        self.name=name
        self.gpa=gpa

stu1=Student("Pratik", 9.9)
stu2=Student("Rahul",9.1)

print(stu1.name)
print(stu1.gpa)
print(Student.college_name)



#instance method example 

class laptop:
    storage_type="ssd"

    def __init__(self, Ram, storage ):
        self.Ram=Ram
        self.storage=storage

    def get_info(self):
        print(f"The laptop has {lap1.Ram} Ram and {lap1.storage} Storage ")

    def get_storage_type():
        print(f"The storage type is {laptop.storage_type}")    

    @staticmethod
    def get_discount(price, discount):
        final_price=price-(discount*price/100)
        print(f"The discounted price is : {final_price}")


lap1=laptop("16Gb", "512Gb" )
lap2=laptop("8Gb", "216Gb")

lap1.get_info()
laptop.get_storage_type()
lap1.get_discount(40000,10)


# product store 


class Product:

    count=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        Product.count+=1

    def get_info(self):
        print(f"The {self.name} price is Rs {self.price}")


    @classmethod
    def the_count(cls):
        print(f"The count of the product is : {cls.count}")


    @staticmethod
    def get_discount(price,discount):
        final_discount=price-(discount*price/100)
        print(f"The final discount on the product is the {final_discount}")    


p1=Product("Phone", 20000)
p2=Product("Tablet", 30000)  
p3=Product("washing machine", 40000)

p1.get_info()
p2.get_info()
p3.get_info()
p1.get_discount(20000,10)

Product.the_count()         


