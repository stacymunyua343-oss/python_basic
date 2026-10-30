#list data structure- uses box brackets
 #changable
#ordered indices
myproducts=["bread", "milk", "sugar","blueband"]
print(myproducts)
myproducts.pop()
myproducts[1]="honey"
print(f"I like drinking tea that has {myproducts[1]}")

#tuple data structure-does not support changing of items- uses normal bracket
countries=("Kenya", "Tanzania", "Burundi", "Somalia","Rwanda")
#countries[0]="usa"
print(countries)

#set data structures-does not support duplication- uses curly brackets
computers={"hp", "dell", "macbook", "lenovo"}
print(computers)


#dictionary data structure
customer={
    "name" : "stacy",
    "age"  :  21,
    "city" : "nairobi",
    "salary" : 500000,
    "profession" : "economist and statistician"
}
print(f"Customer Name :{customer['name']}")

myfruits=["mangoes", "bananas", "apples","pineapples"]
for m in myfruits:
    print(f"I have {m}")
#imagine you are building a school system that calculates the average marks.

marks=[65,89,64,89,90]
total=0
for x in marks:
    total+=x
average=total/len(marks)
print(f"Total marks: {total}")
print(f"Average marks: {average}")

#create a complex calculator using inputoutput and controlflows.
print("Operations: +, -, *, /, %, **")

# loop to keep calculator running
while True:
    
    operator = input("Enter operator (+,-,*,/,%,**) or 'q' to quit: ").lower()

    if operator == "q":
        print("Calc terminated")
        break

    # --- TWO NUMBER OPERATIONS ---
    if operator in ["+", "-", "*", "/", "%", "**"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operator == "+":
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif operator == "-":
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif operator == "*":
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif operator == "/":
                if num2 != 0:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
                else:
                    print("Error: Cannot divide by zero!")
            elif operator == "%":
                print(f"Result: {num1} % {num2} = {num1 % num2}")
            elif operator == "**":
                print(f"Result: {num1} ** {num2} = {num1 ** num2}")

        except ValueError:
            print("Invalid input! Please enter numbers only.")


    else:
        print("Invalid operator! Try again.")