degree=int(input("Enter the Degree:"))
if degree <=20:
    print("Cold Weather")
elif degree >20 and degree <=38:
    print("Normal Weather")
print("Hot! Weather")
fahreheit=((degree*1.8)+32)
print("The Fahreheit value is ",fahreheit,"F")