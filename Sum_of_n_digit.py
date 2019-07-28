n = int(input("Enter a number:"))
tot = 0
while(n > 0):
    dig = n % 10 #This means it will give the reminder or the last significant number of the digit
    tot = tot + dig
    n = n // 10
print("The total sum of digits is:",tot)