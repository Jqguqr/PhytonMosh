items = [
    ("product1", 10),
    ("product2", 7),
    ("product3", 16)
]

# how to get the list with the prices
prices = []
for item in items:
    prices.append(item[1])
# print(prices)

# with map fucntion and Lamdas
prices_items = list(map(lambda item: item[1], items))
print(prices_items)

# COMPREHENSIONS
price_items = [item[1] for item in items]
print(price_items)
