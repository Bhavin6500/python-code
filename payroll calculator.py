
week=int(input("Enter the number of weeks: "))
alist=[]
list=[]
list_for_week=[]

for a in range(week):
    print("the running week:",a+1)
    total_days=0

    days=int(input("enter the number of days:"))
    print("Runnung days is:",)
   
    total_hour=0
    alist.append(days)

    for b in range(days):
        if (days>7):
            print("there are seven days in a week")
        else:
            print("the running day:",b+1)
            
            hour=int(input("enter the number of hours:"))
            total_hour+=hour
            
            print(total_hour)
            total_days+=1
    list.append(total_hour)    
# print(list)
# print("total days are:",total_days)
# print(alist)
sum_of_hours=sum(list)
sum_of_days=sum(alist) 
print("The total hours are:",sum_of_hours)
print("The total days are:",sum_of_days) 
 
print("In",week,"weeks the total",sum_of_days,"days worker works:",sum_of_hours,"hours")  

if(sum_of_hours<=40):
    x=int(input("Enter the pay rate of user:"))
    user=sum_of_hours*x
    print("the total pay worker get is:",user,"$")
else:
    x=int(input("Enter the pay rate of user:"))
    greater_than_40=sum_of_hours-40
    user=40*x
    extra_work=greater_than_40*(x*1.5)
    total_work_include_extra=user+extra_work
    print("the total pay worker get is:",total_work_include_extra,"$")