
def sum_diagonals(matrix):
    sum_of_d1=0
    sum_of_d2=0
    n=len(matrix)
    mid_lm=0
    if n%2 !=0:
            mid=n//2
            mid_lm=matrix[mid][mid]
    else:
         mid_lm=0
    for i in range(n):
        sum_of_d1+=matrix[i][i] 
        # sum_of_d1=sum_of_d1
        sum_of_d2+=matrix[i][-i-1]
        # sum_of_d2=sum_of_d2

    return sum_of_d1+sum_of_d2-mid_lm    # for each_item in i:
        #     if each_item==inner_index:
            #    inner_index+=1


matrix_3x3 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 5, 9]
]
print(sum_diagonals(matrix_3x3))

matrix_4x4 = [
	[ 1,  2,  3,  4],
	[ 5,  6,  7,  8],
	[ 9, 10, 11, 12],
	[13, 14, 15, 16]
]
print(sum_diagonals(matrix_4x4))