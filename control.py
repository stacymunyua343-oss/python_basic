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
    print(f"{num3} is_largest")
if num4 >= num3 and num4 >= num5:
    print(f"{num4} is_largest")
if num5 >= num3 and num5 >= num4:
    print(f"{num5} is_largest")
#Create a program that performs addition, subtraction, multiplication and division of 2 numbers based on the users input.
#when declaring variable make sure you declare them as a float to handle decimal numbers and operator as a variable i.e operator = input("Enter the operator (+, -, *, /): ")
a=float(input("Enter first number."))
b=float(input("Enter second number."))
print("+ : Addition")
print("- : Subtraction")
print("* : Multiplication")
print("/ : Division")
operator=input("Enter your operator(+, -, *, /):")
if operator == '+':
   result= a + b
   print(f"The sum is {result}") 
elif operator == '-':
   result= a - b
   print(f"The difference is {result}")
elif operator == '/':
  if b == 0:
       print(f"Division by 0 is not allowed.")
  else:
       result= a / b
       print(f" Division is {result}")
elif operator == '*':
   result= a * b
   print(f"Multiplication is {result}")

#GRADE STUDENTS MARKS
#use the following grading system to grade students marks 70 and above = A, 60-69 = B, 50-59 = C, 40-49 = D, below 40 = Fail
num8= int(input("Enter your marks"))

if num8 >= 70 and num8<=100:
    print("A")
elif num8 >= 60 and num8 <= 69:
    print("B")
elif num8 >= 50 and num8 <= 59:
    print("C")
elif num8 >= 40 and num8 <= 49:
    print("D")
elif num8 >= 0 and num8 <= 39:
    print("Fail")
#electric bill calculator
#write a program that calculates te electricity bill based on the number of units consumed. the billing rates are as follows:
    # for the first 100 units(0-100): 25 per unit
    #for the next 100 units(101-200): 35 per unit
    #for the next 100 units(201-300): 45 per unit

un=int(input(f"Enter the number of units consumed"))
if un >= 0 and un <=100:
    price=25
    print(f"The charge is {price*un}")
elif un >= 101 and un <= 200:
    price=35
    print(f"The charge is {price*un}")
elif un >= 201 and un <= 300:
    price=45
    print(f"The charge is {price*un}")


