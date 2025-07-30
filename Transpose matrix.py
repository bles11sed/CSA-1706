rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter the elements row by row (space-separated):")
matrix = []
for i in range(rows):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    while len(row) != cols:
        print("Please enter exactly", cols, "values.")
        row = list(map(int, input(f"Row {i+1} again: ").split()))
    matrix.append(row)

transpose = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

print("\nOriginal Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transpose:
    print(row)
