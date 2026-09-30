student={
    "name":"Rahul",
    "age":20,
    "department":"BCA",
    "empid":2
    }

print("The dictionary is:",student)
student["marks"]=85
print("after adding:",student)
student["age"]=24
print("after updating",student)
del student["department"]
print("after deleting",student)

#methods
print("keys:")
print(student.keys())
print("values:")
print(student.values())
print("items:")
print(student.items())
print("Name:",student.get("name"))
print("Marks:",student.get("marks","not available"))
student.update({"age":21,"marks":85})
print("after updating:",student)

#frequency
text=input("enter a string:")
frequency={}
for ch in text:
    if ch in frequency:
        frequency[ch]=frequency[ch]+1
    else:
        frequency[ch]=1
print("character frequency:")
for ch, count in frequency.items():
    print(ch,":",count)
 
"""
The dictionary is: {'name': 'Rahul', 'age': 20, 'department': 'BCA', 'empid': 2}
after adding: {'name': 'Rahul', 'age': 20, 'department': 'BCA', 'empid': 2, 'marks': 85}
after updating {'name': 'Rahul', 'age': 24, 'department': 'BCA', 'empid': 2, 'marks': 85}
after deleting {'name': 'Rahul', 'age': 24, 'empid': 2, 'marks': 85}
keys:
dict_keys(['name', 'age', 'empid', 'marks'])
values:
dict_values(['Rahul', 24, 2, 85])
items:
dict_items([('name', 'Rahul'), ('age', 24), ('empid', 2), ('marks', 85)])
Name: Rahul
Marks: 85
after updating: {'name': 'Rahul', 'age': 21, 'empid': 2, 'marks': 85}
enter a string:sneha
character frequency:
s : 1
n : 1
e : 1
h : 1
a : 1
"""
