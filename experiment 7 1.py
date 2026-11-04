class stud:
    m1=int(input("enter marks 1:"))
    m2=int(input("enter marks 2:"))
    m3=int(input("enter marks 3:"))
    total=m1+m2+m3
    def findper(self):
        avg=self.total/3
    def gradcal(self):
        if(self.total>=100 and self.total<=200):
            print("grade a+")
        elif(self.total>=90 and self.total<=99):
            print("grade a")
        elif (self.total>=80 and self.total<=89):
            print("grade b")
        else:
            print("grade c")
sneha=stud()
sneha.findper()
sneha.gradcal()
