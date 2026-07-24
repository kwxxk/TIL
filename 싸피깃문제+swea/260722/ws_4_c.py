matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]
matrix_len = 0
for element in matrix:
    matrix_len += 1
print(matrix_len)

temporary_len = 0
for i in matrix:
    temporary_len = len(i)
    if temporary_len <= 4:
        print(f"{i} 리스트는 {temporary_len}개 만큼 요소를 가지고 있습니다.")

x=0
for outer in matrix:
    y= 0
    for inner in outer:
        print(f"matrix의{x},{y} 번째 요소의 값은 {inner} 이다")
        y+=1
    x +=1

#   for row_idx, outer in enumerate(matrix):
#     # col_idx: 열 인덱스 (0, 1, 2, ...), inner: 실제 값
#     for col_idx, inner in enumerate(outer):
#         print(f"matrix의 {row_idx},{col_idx}번째 요소값은 {inner} 입니다")