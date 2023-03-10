# Program: Matrix Multiplication
# Function to multiply two matrices
def multiply_matrices(mat1, mat2):
    result = [[0 for j in range(len(mat2[0]))] for i in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result


# Input two matrices from the user
matrix1 = []
matrix2 = []

rows1 = int(input("Enter the number of rows of matrix 1: "))
columns1 = int(input("Enter the number of columns of matrix 1: "))

for i in range(rows1):
    row = list(
        map(int, input(f"Enter row {i+1} of matrix 1 separated by space: ").split())
    )
matrix1.append(row)

rows2 = int(input("Enter the number of rows of matrix 2: "))
columns2 = int(input("Enter the number of columns of matrix 2: "))

for i in range(rows2):
    row = list(
        map(int, input(f"Enter row {i+1} of matrix 2 separated by space: ").split())
    )
matrix2.append(row)

# Call the function to multiply the matrices
print("Resultant matrix:")
resultant_matrix = multiply_matrices(matrix1, matrix2)
for row in resultant_matrix:
    print(row)
