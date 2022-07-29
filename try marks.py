
while True:
    try:
        maths=int(input("MATHS:"))
        physics=int(input("physics:"))
        english=int(input("english:"))
        hindi=int(input("hindi:"))
    except ValueError:
        print("enter any digit")
    else:
        y=maths+physics+english+hindi
        print(y)
        
       