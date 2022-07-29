i=input("you want to continue:")

while(i=="y"):
    def marks_obtain():
        maths=int(input("enter the marks of maths:"))
        english=int(input("enter the marks of english:"))
        physic=int(input("enter the marks of physics:"))
        chemistry=int(input("chemistry marks:"))
        hindi=int(input("hindi marks:"))

        total_marks=(maths+english+physic+chemistry+hindi)
        print("total marks ",total_marks)
        per_obtain(total_marks)

    def per_obtain(total_marks):
        per=(total_marks/500)*100
        print("total per:",per)
        decision(per)

    def decision(per):
        if per>90:
            print("Grade A")
        elif per>80 and per<90:
            print("grade B")
        elif per>70 and per<80:
            print("grade c")
        elif per>60 and per<70:
            print("grade d")
        elif per<60:
            print("Fail")
        else:
            print("Error")

    marks_obtain()
    i=input("enter yes or no:")
    if(i=="n"):
        break