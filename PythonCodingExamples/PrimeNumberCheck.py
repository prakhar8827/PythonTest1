# Program to check whether a number is prime or not ?
# Prime number means it has only 2 factors i.e. 1 and the number itself.

num=19
count=0

if num>1:
    for i in range(1,num+1):
        if num%i==0:
            count=count+1

    if count==2:
        print("number is prime")
    else:
        print("number is not prime")