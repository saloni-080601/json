import json
emp1=[["neelam","programer","24","2400"],["komal","trainer","24","20000"],["anuradha","HR","25","40000"],["Abhishek","manager","29","63000"] ] 
list1=["name","Designation","Age","salary"]
dict1={}
dict2={}
for i in range(0,len(emp1)):
    for j in range(0,len(emp1)):
        dict1.update({list1[j]:emp1[i][j]})
for i in range(0,4):
    u=input("enter keys")
    dict2.update({u:dict1})
print(dict2)
add=open("emp.json","w")
s=json.dump(dict2,add,indent=4)


        
    
