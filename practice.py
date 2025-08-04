num1= int(input("enter the first number: "))
num2= int(input("enter the second number: "))
operator=input("enter an operator:(+, *, /, -): ")

if operator =="+" :
    print("results: ",num1+num2)
elif operator =="*" :
    print("results: ",num1*num2)
elif operator =="/" :
    print("results: ",num1/num2)
elif operator =="-" :
    print("results: ",num1-num2)
else :
    print("invalid operator")