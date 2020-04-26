import random
import string


print(random.random())

print(random.randint(1, 1000))

print(random.choice([1, 2, 3, 4, 5, 6]))

# this one can create a password random
print("".join(random.choices("assksdksajdasjdkajdkad", k=4)))


print(string.digits)

print(string.ascii_letters)


print("".join(random.choices(string.ascii_letters + string.digits, k=10)))


# this is random change
numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)
