"""
##############################################
Vinicius Miranda de Pinho

Comprehensions in Pytohn

Class mosh

23 - 03 -2020
################################################
"""

items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 11),

]


prices2 = list(map(lambda item: item[1], items))
print(prices2)

# list comprehensions
prices = [item[1] for item in items]
print(prices)

