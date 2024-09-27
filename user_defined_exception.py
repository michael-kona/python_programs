#User Defined Exception
class RollError(Exception):
    #constructor 
    def __init__(self, message):
        super().__init__(message)
    
#function in which user defined Exception is raised
def print_roll(roll):
    if(roll>=1 and roll<=60):
        print("Student Roll:",roll)
    else:
        raise RollError("Roll shud b b/w 1 and 60 only")
#Handling user defined exception
try:
    roll=int(input("Enter Roll:"))
    print_roll(roll)
except RollError as re:
    print(re)
except:
    print("Error in the input")
finally:
    print("The END of the program - finally")
    
