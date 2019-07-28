# Python program to check if the number is an Armstrong number or not

#What is Armstrong number e.g- 153= 1*1*1+5*5*5+3*3*3  =153
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
# display the result
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")