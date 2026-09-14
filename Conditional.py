# age code

'''age=int(input("Enter Your Age :"))

if(age<13):
    print("You are Child")
elif (age>=13 and age<18):
    print("You are Teenager")  
else:
    print("You are Adult")'''


 # Authentication Code 

'''username=input("Enter your Username :  ")
password=input("Enter your password :  ")

if (username=="pratik" and password=="admin"):
    print(" Login Succesfull !")
elif(username!="pratik"):
    print(" Wrong Username ")    
else:
    print(" Wrong password")'''    


#To check the number is muliple of 5 or not

'''no= int(input("Enter your no : "))

if (no%5==0):
    print("The no is multiple of 5 ")
else:
    print("It is not multiple of 5 ")  

no1= int(input("Enter your no : "))  

if (no1%2==0):
    print("This is even no ")
else:
    print("This is odd no ")    '''


# nesting if 

'''name =input("Enter your name  ")
password= input("Enter your password ")

if(name=="admin" and  password=="pass"):
     print("Login successfull")
else: 
     if(name!="admin"):
          print("Wrong name ")
     else:
          print("Wrong password ") '''


 # while loop

'''no=int(input("Enter the Table No : "))

i=1
while i<=10:
    print(no*i)
    i+=1'''

''''
i=1

while i<=10:
    if(i%3==0):
        i+=1
        continue
    print(i)
    i+=1'''

'''
i=1
while i<=10:
    if(i%8==0):
        i+=1
        break
    print(i)
    i+=1'''


'''name="pratik"

for var in name:
    print(var)'''


''''string="artificial intelligence"
count=0

for var in string:
    if(var=="a" or var=="e" or var=="i" or var=="o" or var=="u" ):
        count+=1
print("The count of vovel is : ", count) '''


'''no =int(input("Enter your no : "))

i=1
while i<=10:
    print(no*i)
    i+=1'''


'''string= "my name is pratik ramdas nawale "
count=0

for var in string:
    if(var=="a"):
        count+=1
print("The count of a : ", count)'''


'''i=1

while i<=10:
    if(i%2==0):
        print(i)
    i+=1    '''



'''i=1
n=5
sum=0
while i<=n:
    sum=sum+i
    i=i+1    
print(sum)'''



# function for calculating the factorial of the number 

'''def factorial_no(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact    
n=int(input('Enter the value of n : '))
print(factorial_no(n))
'''
'''         
sal=float(input("Enter your salary : "))

if(sal<30000):
    print(f"The tax on salary {sal} : ",(sal*5)/100)
elif(sal>=30000 and sal<=70000):
      print(f"The tax on salary {sal} : ",(sal*15)/100) 
else:
     print(f"The tax on salary {sal} : ",(sal*25)/100)     



'''

'''
no1=int(input("Enter the value of no1 : "))
no2=int(input("Enter the value of no2 : "))
count=0

for i in range(no1, no2+1):
    if(i%2==0):
        print(i)
        count+=1
print(f"The even no between {no1} and {no2} is :  ",count)

'''
"""
value=1
def game(predict):
    while True:
         predict=int(input("Enter the value of predict :"))
         if(value==predict):
                print(f"Your are Right value {value} matches with prediction {predict} !")
         elif(predict>value)  :
                 print("You enter the greater no !")  
         else:
               print("You Enter the lower no !") 

         return predict    

game(2)"""

'''
#string slicing 
Subject="Machine Learning"
a=" Best"

print(Subject[0:13])

print(f"The {Subject} is {a} ")


'''


#list in python 

marks=[99,80,97,87,90,100,83]

print(marks[0:5])
marks.append(95)
print(marks)



