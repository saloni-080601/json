import json
stu={"shopping_list":{ "chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20",}}

user=input("enter your choice")
user2=int(input("enter quantity"))


for i in stu:
    
    for j in stu[i]:
        if j==user:
            num=int(stu[i][j])*user2
            print(num)
stu[i].pop(user)
user3=input("enter a name")
user4=input("enter a key")
stu[i][user3]=user4

with open ("ques.json","w") as h:
    add=json.dump(stu,h,indent=10)
                


        



