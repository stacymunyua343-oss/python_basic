#for loop

for i in range (1,11):
    print(f"Welcome to my shop!Customer {i}")

customers=["Stacy","Brian", "Sylvia", "Joel", "Lydia"]

for c in customers:
    print(f"Welcome to todays class! {c}")
#calculate expense that you bought
#bread ksh 90
#milk ksh120
#sugar ksh160

my_shopping=[90,120,160]
total=0
for m in my_shopping:
    total=total+m
    print(f"My total shopping cost is{total}")
#imagine you have 5 customers and each pay you 100 create a script to the total.
total=0
for num in range (1,6):
    total=total+100
print(f"The total money collected : Ksh{total}")

#while loop
x=0
while x<=10:
    print(f"Loops{x}")
    x+=1
#imagine you want to save starting at 0 balance and save 100 daily until you have 1000.
x=0
while x < 1000:
    x=x+100
    print(f"money saved : {x}")
print("Congratulations! you have reached your target")
