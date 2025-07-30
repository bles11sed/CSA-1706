fruits = input("Enter some fruits (separated by spaces): ").split()

fruits.append(input("Enter one fruit to append: "))
fruits.extend(input("Enter more fruits to extend (separated by spaces): ").split())
fruits.remove(input("Enter a fruit to remove: "))
fruits.pop(int(input("Enter index to pop: ")))

print("Final list:", fruits)

