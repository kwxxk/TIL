import numpy as np
A = np.array([[1, 2], [2, 4]]) # 랭크 1인 행렬
rank = np.linalg.matrix_rank(A)
print(rank)