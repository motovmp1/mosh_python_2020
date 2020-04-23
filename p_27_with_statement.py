import sys
# with support more than one file to open as , comma and second file name

try:
    with open("/home/elsys/PycharmProjects/mosh_python_2020/txt_files/text.txt", "w") as files:
        print("File opened")
        files.write("Test this lines")
        age = (int(input("Age: ")))
        print("Your age is: ", age, "years old")
        x_factor = 10 / age
except (ValueError, ZeroDivisionError) as message:
    print("Your value is wrong")
    print(type(message))
finally:
    print("test")
