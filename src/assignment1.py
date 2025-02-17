def add_matrices(A, B):
    rows = len(A)
    cols = len(A[0])
    
    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Perform addition
    for i in range(rows):
        for j in range(cols):
            result[i][j] = A[i][j] + B[i][j]
    
    return result
