# Python Program to find the area of triangle

a = int(input("Enter value of side A::"))
b = int(input("Enter value of side B::"))
c = int(input("Enter value of side C::"))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)