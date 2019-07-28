# Python program to check if the input number is prime or not and find square root of that number

num = int(input('Enter a number to be checked:'))

# prime numbers are greater than 1
if num > 1:

    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")
        num_sqrt = num ** 0.5
        print("The squre root of prime number is",num_sqrt)
# if input number is less than
# or equal to 1, it is not prime
else:
    print(num, "is not a prime number")
