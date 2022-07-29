total_years=0
list=[]
years=int(input("enter the number of years: "))
for i in range(years):
    print("the year which is runnnig:",i+1)
    months=12
    total_rainfall=0
    for j in range(months):
        
        print("enter the months ",j+1)
        rainfall_month=int(input("enter the months rainfall: "))
        total_rainfall+=rainfall_month
    list.append(total_rainfall)
    months+1
    
    print("the value of i is ",i)
    print("total months are",months)
    print(list)
    x=sum(list)
    
    sub_total=((j+1)*(i+1))
    print(sub_total)
    average=(x/(sub_total))
    print("average rainfall in the total years:",average)
            
        
            
        

