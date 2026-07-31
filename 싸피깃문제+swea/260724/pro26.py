# scores = {
#     'bogeom' : 89,
#     'sangho' : 100,
#     'IU' : 78,
#     'sori' : 76,
#     'hejun' : 85,
# }
# max_score=0
# top_person = ""
# for name, score in scores.items():
#     if score > max_score:
#         max_score = score
#         top_person=name
# print(top_person)

scores = {
    'bogeom' : 89,
    'sangho' : 100,
    'IU' : 78,
    'sori' : 76,
    'hejun' : 85,
}
max_v = 0
best_student = ""
for name, score in scores.items():
    if score > max_v:
        max_v = score #갱신
        best_student=name #갱신 될 때의 학생
print(best_student)

# ★★★★★최대, 최솟값 코드 구현 월말평가에 무조건 나옴 ★★★★★