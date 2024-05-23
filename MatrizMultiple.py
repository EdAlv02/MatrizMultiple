import numpy as np

# Definición de las matrices múltiples A y B
A = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
B = [[[2, 0], [1, 2]], [[3, 1], [1, 1]]]

# Tamaño de las matrices múltiples
n = len(A)  #Número de submatrices
m = len(A[0]) # Número de filas en cada submatriz
p = len(B[0]) # Número de columnas en cada submatriz de B

# Inicializar la matriz resultado
C = [[[0 for _ in range(p)] for _ in range(n)] for _ in range(n)]
# Multiplicar matrices
for i in range(n):
  for j in range(n):
   for k in range(m):
     for ii in range(len(A[i][k])):
       for jj in range(len(B[k][j])):
         C[i][j][ii] += A[i][k][ii] * B[k][j][jj]

# Mostrar el resultado
for submatriz in C:
  print(submatriz)