from numpy import dot
from numpy.linalg import norm
import numpy as np

def cosine_similarity(A, B):
    return dot(A, B) / (norm(A) * norm(B))

document_1 = np.array([1, 1, 0])
document_2 = np.array([3, 3, 0])
document_3 = np.array([1, 0, 1])

# 문서 1과 문서 2의 코사인 유사도 출력
print(cosine_similarity(document_1, document_2))
# 문서 1과 문서 3의 코사인 유사도 출력
print(cosine_similarity(document_1, document_3))

# 결과 값: 문서 1과 문서 2의 유사도: 1
# 문서 1과 문서 3의 유사도: 0.5

