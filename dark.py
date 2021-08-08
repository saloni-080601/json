import json
start="Name Abhishek Designation CEO,of,navgurukul Gender male Age 29"

length=start.split()
dict1={}
for i in range(0,len(length),2):
    dict1.update({length[i]:length[i-7]})
print(dict1)
with open("stop.json","w") as h:
    f= json.dump(dict1,h,indent=10)
    print(f)