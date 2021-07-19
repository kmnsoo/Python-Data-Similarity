# 다음과 같은 두 개의 문서가 있습니다.
# 두 문서 모두에서 등장한 단어는 apple과 banana 2개.
doc1 = "apple banana everyone like likey watch card holder"
doc2 = "apple banana coupon passport love you"

# 토큰화를 수행합니다.
tokenized_doc1 = doc1.split()
tokenized_doc2 = doc2.split()

# 토큰(Token)이란 문법적으로 더 이상 나눌 수 없는 언어요소를 뜻한다. 
# 텍스트 토큰화(Text Tokenization)란 말뭉치로부터 토큰을 분리하는 작업을 뜻한다.

# 토큰화 결과 출력
print(tokenized_doc1)
print(tokenized_doc2)

# 출력 결과 
# ['apple', 'banana', 'everyone', 'like', 'likey', 'watch', 'card', 'holder']  8개
# ['apple', 'banana', 'coupon', 'passport', 'love', 'you'] 6개

#문서1과 문서2의 합집합 구하기
union = set(tokenized_doc1).union(set(tokenized_doc2))
print("union -> ", union)

# 출력 결과 
# {'you', 'likey', 'banana', 'watch', 'holder', 'coupon', 'passport', 'love', 'card', 'like', 'apple', 'everyone'} 12개

# 문서1과 문서2의 교집합
intersection = set(tokenized_doc1).intersection(set(tokenized_doc2))
print("intersection -> ", intersection)

# 출력 결과 
# {'banana', 'apple'}

# 두 문서의 교집합(intersection)은 banana와 apple 총 2개이다. 
# 이제 교집합의 수를 합집합의 수로 나누면 자카드 유사도가 계산된다.

print("자카드 유사도->", len(intersection)/len(union)) # 2를 12로 나눔.
#출력결과 
# 0.16666666666666666(자카드 유사도)