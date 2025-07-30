fruits = ["apple", "banana", "cherry"]
nested = ["fruit", fruits]

print("Length:", len(fruits))
print("Concatenation:", fruits + ["orange", "grape"])
print("'banana' in list?", "banana" in fruits)

print("Iterating:")
for f in fruits:
    print(f)

print("Indexing:", fruits[0], fruits[-1])
print("Slicing:", fruits[1:])
print("Nested access:", nested[1][1])
