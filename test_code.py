from src.assignment1 import test_add_matrices


# Example Usage
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = test_add_matrices(A, B)

# Print the result
for row in result:
    print(row)
