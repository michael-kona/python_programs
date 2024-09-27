basic=int(input("Enter Basic Salary:"))
if(basic>0 and basic<=10000):
    hra=0.2*basic
    da=0.8*basic
elif(basic<=20000):
    hra=0.25*basic
    da=0.9*basic
elif(basic>20000):
    hra=0.3*basic
    da=0.95*basic
gross=basic+da+hra
print("gross Salary:",gross)
