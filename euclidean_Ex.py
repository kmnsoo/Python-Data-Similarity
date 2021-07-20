from numpy.linalg import norm
import numpy as np

def euclidean_distance(A, B):
    return np.linalg.norm(A - B)


document_1 = np.array([1, 1, 0])
document_2 = np.array([3, 3, 0])
document_3 = np.array([1, 0, 1])

# 문서 1과 문서 2의 유클리드 거리 출력
print(euclidean_distance(document_1, document_2))
# 문서 1과 문서 3의 유클리드 출력
print(euclidean_distance(document_1, document_3))