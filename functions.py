def greet():
    print("This is my first function")

#function with parameters
def student(name,age,course):
    print(f"Student name is {name}")
    print(f"Student age is {age}")
    print(f"Student course is {course}")
student("Stacy", 21, "Economics and Statistics")
student("Lydia", 22, "Data Science")
student("Mark", 23, "Arts")
student("Nick", 22, "Cyber Security")

#function with return keyword
def add_number(a,b):
    return a+b
result=add_number(6,26)
print(f"Sum : {result}")

#function to return product
def multiply_number(a,b):
    return a*b
result=multiply_number(6,26)
print(f"product : {result}")