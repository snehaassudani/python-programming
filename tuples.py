def EmpCalc():
    Name=input("Enter name:")
    Age=int(input("Enter Age:"))
    sal=float(input("Enter salary:"))
    HRA=(sal*35)/100
    PF=(sal*25)/100
    netsal=sal+HRA+PF
    if(netsal>=30000) and (netsal<=100000):
        print("Senior Manager")
    elif(netsal>=20000)and(netsal<=29999):
        print("Manager")
    else:
        print("Front level job")
    return Name,Age,netsal
Name,Age,netsal=EmpCalc()
print("Employee name:",Name)
print("Employee age:",Age)
print("Net Salary:",netsal)
