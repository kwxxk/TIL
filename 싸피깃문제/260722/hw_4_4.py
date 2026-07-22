list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

rental_book = [
    '장생전',
    '위대한 개츠비',
    '원생몽유록',
    '이생규장전',
    '데미안',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]
# check_book = ['위대한 개츠비', '데미안', '난중일기']
# if rental_book == None:
#     print("모든 도서가 대여 가능한 상태입니다.")
# else:
#     for b in check_book:
#         if b not in list_of_book:
#             print(f"{check_book} 을/를 보충하여야 합니다.")
#             if b in rental_book:
#                 print(f"'{check_book}' 은/는 현재 대여 중입니다.")
#             else:
#                 print(f"'{check_book}' 이/가 대여 가능한 상태입니다.")
#             break


check_books = ['위대한 개츠비', '데미안', '난중일기']

if rental_book is None:
    print("모든 도서가 대여 가능한 상태입니다.")
else:
    # 1. 검사할 책 목록에서 책을 한 권씩 꺼냄
    for book in check_books:
        # 2. 보유 도서 목록에 없는 경우
        if book not in list_of_book:
            print(f"'{book}' 을/를 보충하여야 합니다.")
        # 3. 보유 중인데 대여 목록에 있는 경우
        elif book in rental_book:
            print(f"'{book}' 은/는 현재 대여 중입니다.")
        # 4. 보유 중이고 대여 목록에도 없는 경우
        else:
            print(f"'{book}' 이/가 대여 가능한 상태입니다.")