def sort_leaderboard(leaderboard):
    sorted_list=[]
    unique_list=[]
    for name, score in leaderboard:
            unique_list.append((name, score))
    unique_list.sort()

    for name, neg_score in unique_list:
          sorted_list.append((-neg_score, name))
    sorted_list.sort()
    final_list=[]
    for neg_score, name in sorted_list:
          final_list.append((name, -neg_score))

    return final_list

leaderboard = [
	('Alice', 88),
	('Bob', 92),
	('Charlie', 92),
	('David', 85)
]
print(sort_leaderboard(leaderboard))
        
scores = [('Zelda', 100), ('Mario', 120), ('Link', 100), ('Sonic', 100)]
print(sort_leaderboard(scores))

    