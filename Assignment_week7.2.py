# # ^^^^^^^^^^^^^^Solving Assignment from(51:55)^^^^^^^^^^^^^^^
#
# print('--------------Assignment 1 --------------------')

# nums = [15, 81, 5, 17, 20, 21, 13]
# index = 1
# nums.sort(reverse=True)
# for i in nums:
# 	if i % 5 == 0:
# 		print(f'{index}=> {i}')
# 		index += 1
# print('All numbers are printed')
# #------------------------------------------------
#
# # print('--------------Assignment 2 --------------------')
#
# for num in range(1, 21):
# 	if num in [6, 8, 12]:
# 		continue
# 	print(f'{str(num).zfill(2)}')
# print("All Numbers Printed")
# #------------------------------------------------
#
# # print('--------------Assignment 3 --------------------')
#
# my_ranks = {
# 	'Math': 'A',
# 	"Science": 'B',
# 	'Drawing': 'A',
# 	'Sports': 'C'}
# points = {
# 	'A': 100,
# 	'B': 80,
# 	'C': 40
#
# }
# summ = 0
# for mat in my_ranks:
# 	print(f'My Rank in {mat} Is {my_ranks[mat]} And This Equal {points[my_ranks[mat]]} Points')
# 	summ += points[my_ranks[mat]]
# print(f'Total Points Is {summ}')
# #------------------------------------------------
#
# # print('--------------Assignment 4 --------------------')
#
students = {
	"Ahmed": {
		"Math": "A",
		"Science": "D",
		"Draw": "B",
		"Sports": "C",
		"Thinking": "A"
	},
	"Sayed": {
		"Math": "B",
		"Science": "B",
		"Draw": "B",
		"Sports": "D",
		"Thinking": "A"
	},
	"Mahmoud": {
		"Math": "D",
		"Science": "A",
		"Draw": "A",
		"Sports": "B",
		"Thinking": "B"
	}
}
rank = {
	'A': 100,
	'B': 80,
	'C': 40,
	'D': 20
}

for name, values in students.items():
	print('*' * 50)
	print(f'Student Name => {name}'.center(50, '*'))
	print('*' * 80)
	total = 0
	for mat, degree in values.items():
		print(f'- {mat} ==> {rank[degree]}')
		total += rank[degree]
	print(f'Total  Points For {name} Is {total}')