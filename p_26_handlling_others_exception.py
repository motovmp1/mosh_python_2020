import sys

try:
    file_text = open("/home/elsys/PycharmProjects/mosh_python_2020/txt_files/text.txt", "w")
    n = file_text.write('hello world......')
    age = (int(input("Age: ")))
    print("Your age is: ", age, "years old")
    x_factor = 10 / age
except (ValueError, ZeroDivisionError) as message:
    print("Your value is wrong")
    print(type(message))
finally:
    print(file_text.closed)
    file_text.close()
    print(file_text.closed)
