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
 
