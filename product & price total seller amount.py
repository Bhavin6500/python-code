
list_product=[]
list_price=[]
items=int(input("Enter the total items: "))

for i in range(items):
    print("enter the product number:",i+1)
    while True:
        try:
            product_name=input("Enter the name of the product:")
            if(product_name.isalpha()):
                break
            else:
                raise TypeError
        except TypeError:
            print("Enter any Alphabetic value")
            continue
    while True:
        try:
            product_price=int(input("Enter the price of the product:"))
            break
        except:
            print("please enter the numberic value")   
            continue
        
       
    list_product.append(product_name)
    list_price.append(product_price)
            # print(product_name)
    # print(product_price)
    # print(list_product)
    # print(list_price)
    
dictionary=dict(zip(list_product,list_price))
print(dictionary)
total=sum(list_price)
print("Total amount customer has to pay is :",total)















# a=["apple","banana","cherry"]
# b=[25,32,12]
# c=dict(zip(a,b))
# print(c)



#  while True:
#         try: 
#             product_name=input("Enter the name of the product:")
#             product_price=int(input("Enter the price of the product:"))
#         except NameError:
#             print("enter string input")
#         except ValueError:
#             print("Enter anything")