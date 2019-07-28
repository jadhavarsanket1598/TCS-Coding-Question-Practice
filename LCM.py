a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if(a>b):
    greater=a
else:
    greater=b
while(1):
    if(greater%a==0 and greater%b==0):
        print("LCM of two numbers is:",greater)
        break
    greater=greater+1