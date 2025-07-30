rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

print("Enter elements for Matrix A:")
A = []
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"Enter A[{i}][{j}]: "))
        row.append(val)
    A.append(row)

print("Enter elements for Matrix B:")
B = []
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"Enter B[{i}][{j}]: "))
        row.append(val)
    B.append(row)
C = []
for i in range(rows):
    row = []
    for j in range(cols):
        sum_val = A[i][j] + B[i][j]
        row.append(sum_val)
    C.append(row)

print("Resulting Matrix C (A + B):")
for row in C:
    print(row)


