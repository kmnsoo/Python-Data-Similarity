import numpy as np

# 유클리드 거리(euclidean distance)는 문서의 유사도를 구할 때 자카드 유사도나 코사인 유사도만큼, 유용한 방법은 아니다.
#  하지만 여러 가지 방법을 이해하고, 시도해보는 것 자체만으로 다른 개념들을 이해할 때 도움이 되므로 의미가 있다.

def dist(x,y):   
    return np.sqrt(np.sum((x-y)**2))

# 문서들을 4차원 공간에 배치시키고 문서 Q또한 4차원의 공간에 배치시킨 후 유클리드 거리를 구한다.

doc1 = np.array((2,3,0,1))
doc2 = np.array((1,2,3,1))
doc3 = np.array((2,1,2,2))
docQ = np.array((1,1,0,1))



print(dist(doc1,docQ))
print(dist(doc2,docQ))
print(dist(doc3,docQ))

#출력 결과:
#2.23606797749979
#3.1622776601683795
#2.449489742783178

#유클리드 거리의 값이 가장 작다는 것은, 문서 간의 거리가 가장 가깝다는 것을 의미한다.
#  즉, 문서1이 문서Q와 가장 유사하다고 볼 수 있다.