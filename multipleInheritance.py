class A:
    def __init__(self):
        print("Constructor of class A")
    def feature1(self):
        print("Feature 1 of class A")

class B:
    def __init__(self):
        print("Constructor of class B")
    def feature2(self):
        print("Feature 2 of class B")
        

class C(A,B):
    def __init__(self):
        super().__init__()
        print("Constructor of class C")
    def feature3(self):
        print("Feature 3 of class C")
        
c1=C()
c1.feature1()
c1.feature2()