
num1=input("enter num1 value :")
num2=input("enter num2 value :")

print("Value of num1 before swaping :",num1)
print("Value of num2 before swaping :",num2)

#Approach 1: using a temporary variable
# temp=num1
# num1=num2
# num2=temp

#Approach 2:

num1,num2=num2,num1

print("Value of num1 after swaping :",num1)
print("Value of num2 after swaping :",num2)

