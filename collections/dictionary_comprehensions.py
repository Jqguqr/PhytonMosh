# Expresion normal
values1 = []

for x in range(5):
    values1.append(x * 2)

# List + Comprehensions
values2 = [x * 2 for x in range(5)]
print(values2)

# Set + Comprehensions
values3 = {x * 2 for x in range(5)}
print(values3)

# Dictinary + Comprehensions
values4 = {x: x * 2 for x in range(5)}
print(values4)

# Tuple + Comprehensions
values5 = (x * 2 for x in range(5))
print(values5)
