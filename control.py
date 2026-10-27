#a python program that checks if someone is eligible to vote or no

age=int(input("Enter your age"))
if age>=18:
    print("You are eligible")
else:
    print("You cannot vote...underage")
#Create a program that checks if a number is odd or even
num=int(input("Enter your number"))
if num % 2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

#Create a program that checks between 3 numbers which one is the biggest
num3=int(input("Enter first number"))
num4=int(input("Enter second number"))
num5=int(input("Enter third number"))
if num3 >= num4 and num3 >= num5:
    print("{num3} is_largest")
if num4 >= num3 and num4 >= num5:
    print("{num4} is_largest")
if num5 >= num3 and num5 >= num4:
    print("{num5} is_largest")
