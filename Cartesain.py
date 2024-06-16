from itertools import product
list1 = [1, 2]
list2 = ['a', 'b', 'c']
# Find Cartesian product
cartesian_product = list(product(list1, list2))
print(cartesian_product)

#second method
cartesian_product= []

for elem1 in list1:
    for elem2 in list2:
        cartesian_product.append((elem1, elem2))

print(cartesian_product)

#time complexcity
cartesian_product= [(x, y) for x in list1 for y in list2]
print(cartesian_product)