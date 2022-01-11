def diagonalSum(mat):
    
    rows_length,diag_sum = len(mat),0

    for i in range(rows_length):
        diag_sum += mat[i][i] + mat[i][rows_length-i-1]

    if rows_length %2==1:
        diag_sum -=mat[rows_length//2][rows_length//2]


    return diag_sum

