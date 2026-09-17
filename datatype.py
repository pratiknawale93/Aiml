
#list in the python
"""marks=[10,40,30,70,50]

marks.append(60)
print(marks)

marks.extend([30,80])
print(marks)

marks.sort()
print(marks)

point=[10,20,30,40,50,60]

for var in point:
    print(var)"""


#tuple in the python

'''marks=(10,20,20,40,20,80)

print("The elements of Tuple : ",marks)

print("The length od tuple : ",len(marks))


print(marks.count(20))

print(marks.index(20))

print(tuple([9.1,9.3,"ketan"]))

print("The max of the tuple : ", max(marks))
print("The max of the tuple : ", min(marks))

'''
# dictionary in python 
'''
data={"name" :"pratik" , "Rollno" :"12", "age":"21", "gender":"Male"}

print(data.get("name"))
print(data.keys())
print(data.values())
print(data.items())
data.update({'marks':12})
print(data)
'''

#sets in the python 
'''
s1={1,2,3,4,5}
s2={4,5,6,7,8,9,10}

s1.add(0)
print(s1)

print(s1.union(s2))
print(s1.intersection(s2))'''


student=[("pratik","System Design"),("soham", "java"),("amir", "python"),("sahil", "java"),("pratik","java"),("pratik","python")]
'''
u_set=set()

for var in student:
    u_set.add(var[1])

print(u_set)  '''  


dict={}

for name,course in student:
    if(dict.get(name)==None):
        dict.update({name:set()})
        dict[name].add(course)
    else:
        dict[name].add(course) 
print(dict)        

           


















