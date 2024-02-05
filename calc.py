a = int(input("Enter your choice 1.Add, 2. Sub, 3. Mul  \n"))
if a==1:
    k= int(input("Enter first Number  "))
    x= int(input("Enter second Number  "))
    y= k+x
    print("Your answer is " , y)
           
elif a==2:
    k= int(input("Enter first Number "))
    x= int(input("Enter second Number "))
    y= k-x
    print("Your answer is " , y)

elif a==3:
    k= int(input("Enter first Number "))
    x= int(input("Enter second Number "))
    y= k*x
    print("Your answer is " , y)


else:
    print("Invalid sellection ")