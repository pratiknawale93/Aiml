'''class name:
    name1="Pratik"
    name2="rajesh"

n1=name()
print(n1.name1)'''

'''
text=input("Enter the value of String : ")

seen=set()
duplicate=set()
count=0

for ch in text:
    if ch in seen:
        duplicate.add(ch)
    else:
        seen.add(ch)
        count+=1
print(f"The unique count of elements : {count} and the char are {seen}")  '''


text=input("Enter the value of the text :")
print(f"The given text is  : {text} ")

count=0
seen=set()
duplicate=set()
for ch in text:
    if ch in seen:
        duplicate.add(ch)
    else:
        seen.add(ch)
        count+=1

if (count%2==0):
    print("The count is even !")
else:
    print("The count is odd !")

print(f" The unique elements in the string are : {seen} and  count is {count}" )        






