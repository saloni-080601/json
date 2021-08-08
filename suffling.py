import random 
list1=["saloni","chhaya","karuna","yogita","pooja","joyti","priyanka","neha","kajal","ankita p", "nikita s","nikita t", "lovely","sheetal","ishita","deepu","sanjhana","sanjhana jha","muskan","abhru","pihu","karti","sagrika","pooja M"]
no_room=[401,402,403,404,405,406,407,408,409,410,411,412]
list3=["bed no1","bed no2","bed no3","bed no4","bed no5","bed no6","bed no7","bed no8","bed no9","bed no10","bed no11","bed no12"]
length=len(list1)
for i in list1:
    c=random.shuffle(list1[i])
    print(c)
    