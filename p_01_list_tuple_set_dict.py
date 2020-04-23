# LIST - SQUARE BRACES []
# TUPLE - ROUNDED BRACES ()
# SET - the set keywords
# DIC - {} curly braces made up of key-values pairs


list1 = ["computer", "printer", "tv", "camera", 89, 30.8]
list1[0] = "pc"
print(list1)

# tuple is immutable (never change)
tuple1 = ("computer", "printer", "tv", "camera", 89, 30.8)
# tuple1[0] = "pc"
print(tuple1)

# set
set1 = set(["computer", "printer", "tv", "camera", 89, 30.8])
print(set1)

# not two keys, and cannot chage keys
dict1 = {
    1: "Monday",
    2: "Tuesday",
    "A": 23
}
print(dict1)
