# You are using Python
def find_Diameter(r):
    return(2*r)
def find_Circumference(r):
    return(2*3.14*r)
def find_area(r):
    return(3.14*r*r)

radius=float(input())
print("Diameter of a circle =%.2f"%find_Diameter(radius))
print("Circumference of a circle = %.2f"%find_Circumference(radius))
print("Area of a circle = %.2f"%find_area(radius))
