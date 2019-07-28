# Python program to convert decimal number into binary, octal and hexadecimal number system
#A number with the prefix '0b' is considered binary, '0o' is considered octal and '0x' as hexadecimal.bin
# Change this line for a different result
dec = int(input("Enter the decimal number ::"))

print("The decimal value of",dec,"is:")
print(bin(dec),"in binary.")
print(oct(dec),"in octal.")
print(hex(dec),"in hexadecimal.")