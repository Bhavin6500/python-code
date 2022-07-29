#BMI calculator

Feet=0.0
Inches=0.0
weight=0.0
feet_cm = 30.48
inch_cm = 2.54
total_height_cm = 0.0
BMI = 0.0
convert_cm_m = 0.0
convert_cm_m2 = 0.0

weight = float(input("Enter your total weight in Kilogram: "))
Feet = int(input("Enter your height in feet:"))
Inches = int(input("Enter inches in your height:"))

total_height_cm = (Feet*feet_cm)+(Inches*inch_cm)
print("total height of the person in centimeter:",total_height_cm ,"cm")
convert_cm_m=total_height_cm/100
convert_cm_m2 = convert_cm_m * convert_cm_m


BMI = weight/convert_cm_m2
print("BMI of the person is :",format(BMI,'.2f') )
if(BMI < 19):
    print("person is Underweight")
elif(BMI>19 and BMI<25):
    print("Person is healthy")
elif(BMI >= 25):
    print("Person is overweighted")
