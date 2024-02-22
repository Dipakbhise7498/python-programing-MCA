class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    
    def __add__(self,other):
        s1=self.m1+other.m1
        s2=self.m2+other.m2
        s3=Student(s1,s2)
        return s3
    
    def __gt__(self,other):
        s1=self.m1+self.m2
        s2=other.m1+other.m2
        if s1>s2:
            return True
    
    def __lt__(self,other):
        s1=self.m1+self.m2
        s2=other.m1+other.m2
        if s1<s2:
            return True 
     
    def __ge__(self,other):
        s1=self.m1+self.m2
        s2=other.m1+other.m2
        if s1>=s2:
            return True   
    
    def __le__(self,other):
        s1=self.m1+self.m2
        s2=other.m1+other.m2
        if s1<=s2:
            return True
        
s1=Student(100,20)
s2=Student(20,300)
s3=s1+s2
if s1>s2:
    print("s1 is greater")
else:
    print("s2 is greater")
    
if s1<s2:
    print("s1 is smaller")
else:
    print("s2 is smaller")

if s1>=s2:
    print("s1 is greater than equal to s2")
else:
    print("s2 is greater than equal to s1")

if s1<=s2:
    print("s1 is less than equal to s2")
else:
    print("s2 is less than equal to s1")
# print(s3.m1)
# print(s3.m2)


        