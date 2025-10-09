n = int(input("Enter the size of matrix: ")) 
matrix = [list(map(int, input().split())) for _ in range(n)]

primary_diagonal = 0
secondary_diagonal = 0

for i in range(n):
    primary_diagonal += matrix[i][i]             
    secondary_diagonal += matrix[i][n - 1 - i]    

print(abs(primary_diagonal - secondary_diagonal))