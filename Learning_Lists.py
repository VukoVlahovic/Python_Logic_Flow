fruits = ["apple", "banana", "pineapple", "orange"]

fruits.append("mushroom")
# print(dir(fruits))
fruits[0] = "Bacon"
for fruit in fruits:
    print(fruit)

fruits.remove("Bacon")
print("Now we removed Bacon ", fruits)

fruits.insert(1, "pear")
print("Now we inserted a pear at position 1 ", fruits)

fruits.sort()
print("Now we sorted the list in order", fruits)

fruits.reverse()
print("This will reverse the current list. Remember we previously sorted.", fruits)

print(fruits.index("mushroom"))
print("The number above refers to the position of mushroom in the array/list.")

print(fruit.count("apple"))
print("count returned 0 because there are no apples in the list. It was replaced earlier in the code.")
