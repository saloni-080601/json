# import json
# stu='{"Name":"Ram", "Class":"IV", "Age":9 }'
# passed=json.loads(stu)
# print(passed)




# import json
# stu={"name": "David",
#      "class":"I",
#      "age": 6  }
# with open("que.json","w") as h:
#     f=json.dump(stu,h,indent=10)
#     print(f)






# import json
# x={'4': 5, '6': 7, '1': 3, '2': 4}
# print( json.dumps(x, indent=4, sort_keys=True))



import json
stu='{"a":  1,"a":  2,"a":  3, "a": 4,   "b": 1, "b": 2}'
print(json.loads(stu))



