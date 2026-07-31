import json

a= dict()
a['name'] = 'sanghi'
a['price'] = 4900
a['brand'] = 'mcdonald'

# 딕셔너리를 json으로 바꾼다 == 인코딩 encoding
# 메서드 dumps
# indent = 들여쓰기
b = json.dumps(a, indent = 4)

# json을 딕셔너리로 바꾼다 == 디코딩 decoding
# 메서드 loads

c= json.loads(b)
print(a)
print(b)
print(c)