# In the loop, when the item value is "banana", jump directly to the next item.


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
