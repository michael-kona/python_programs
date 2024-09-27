class Parent:
    def add(self,a,b):
        return(a+b)
class Child(Parent):
    def sub(self,a,b):
        return(a-b)

c=Child()
a,b=input().split()
print("Addition of the Integers :",c.add(int(a),int(b)))
print("Subtraction of the Integers :",c.sub(int(a),int(b)))
