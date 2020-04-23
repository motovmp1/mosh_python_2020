from timeit import timeit

code1 = """
def calculate_x_factor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_x_factor(-1)
except ValueError as error:
    pass
"""

code2 = """
def calculate_x_factor(age):
    if age <= 0:
        return None
    return 10 / age



x_factor = calculate_x_factor(-1)
assert x_factor == None
 """

print("The time is:", timeit(code1, number=10000))
print("The time is:", timeit(code2, number=10000))
