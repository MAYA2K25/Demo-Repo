name=input("Enter your name:")
age=int(input("Enter your age:"))
gpa=float(input("Enter your gpa:"))
enrolled=input("Enter whether you have enrolled Yes/No:")

print(f"my name is {name}")
print(f"my age is {age}")
print(f"My gpa for finals is {gpa}")

if enrolled.lower() == "yes":
    print(f"{enrolled}, I am Enrolled")
elif enrolled.lower() == "no":
    print(f"{enrolled}, I am not Enrolled")
else:
    print(f"No input from customer")

print(type(name,age,gpa,enrolled))