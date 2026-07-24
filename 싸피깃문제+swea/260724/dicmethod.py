dic = {"apple": 2, "banana": 5}

# print(dic['kiwi'])

# error를 일으키지 않기 위해서
# 메서드 get
print(dic.get('kiwi'))

# get요청 get
# requests.get(url)

# 딕셔너리를 iterator 방식으로 순회
# key가 나온다
for key in dic:
    print(key)