
options=int(input("Enter 1.Money Withdraw 2.Money depoit: "))
total_amount=0
while options==1:
    pin=int(input("please enter the pin number: "))
    if pin==1234:
        amount=int(input("enter the amount you want to deposit: "))
        total_amount+=amount
        print(total_amount)
    elif(pin==123):
        amount=int(input("Enter the amonut you want to withdraw: "))
        total_amount-=amount
        print(total_amount)


