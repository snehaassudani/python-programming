import re
data=input("enter email or mobile number:")
email= r'^[a-zA-Z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-zA-Z]{2,}$'
mob= r'^[0-9]{10}$'
if re.fullmatch(email,data):
    print("valid email")
elif re.fullmatch(mob,data):
    print("valid phone number")
else:
    print("invalid input")
