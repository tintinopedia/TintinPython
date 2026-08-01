student = {"name":"Ahaan","age":11}
print(student)
print(student["name"])
print(student.get("age"))
student["school"]="Hiranandani Foundation school"# Addition of value
print(student)
print(student.keys())
print(student.values())
print(student.items())
student.update({"roll.no":9,"age":6})
print(student)
student["age"]=8
print(student)
student.pop("age")
print(student)
del student["name"]
print(student)
student.clear()
print(student)
student["roll.no"]=9
print(student)
print(student.keys())