try:
    age = (int(input("Age: ")))
    print("Your age is: ", age, "years old")
except ValueError as message:
    print("Your value is wrong")
    print(type(message))
else:
    print("No any error pass to except")
print("End of the program")
