scores = {
    'bogeom' : 89,
    'sangho' : 100,
    'IU' : 78,
    'sori' : 76,
    'hejun' : 85,
}
max_score=0
top_person = ""
for name, score in scores.items():
    if score > max_score:
        max_score = score
        top_person=name
print(top_person)