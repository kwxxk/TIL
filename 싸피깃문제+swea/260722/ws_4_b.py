food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]
# get_food = input("음식 이름을 입력하세요: ")
# for food in food_list:
#     if food['이름'] == "자장면":
#         print("자장면엔 고춧가루지")
#     print(f"{food['이름']} 은/는 {food['종류']} (이)다")
# print(food_list)

i = 0
while i < len(food_list):
    food = food_list[i]
    if food['이름'] == '자장면':
        print("자장면엔 고춧가루지")

    print(f"{food['이름']} 은/는 {food['종류']} (이)다")
    i += 1

print(food_list)