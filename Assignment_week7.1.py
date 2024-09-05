# ^^^^^^^^^^^^^^Solving Assignment from(47:55)^^^^^^^^^^^^^^^

print('--------------Assignment 1 --------------------')

number = int(input('Enter a number: '))
num_list = []
if number > 5:

	while number > 1:
		number -= 1
		if number == 6:
			continue
		print(number)
		num_list.append(number)
	else:
		print('All numbers was printed ')
	print(f'{len(num_list)} Numbers Printed Successfully.')
else:
	print('number must be greater than 5')
#------------------------------------------------

print('--------------Assignment 2 --------------------')
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
x = 0
list_ = []
while x < len(friends):
	if str(friends[x][0]).isupper():
		print(friends[x])
		list_.append(friends[x])
	x += 1
print(f'Friends Printed And Ignored Names Count Is: {len(friends)-len(list_)}')
#------------------------------------------------

# print('--------------Assignment 3 --------------------')

skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills:
	print(skills.pop(0))
	#print(skills[0]);del(skills[0])  # del function delet(what is here)
#------------------------------------------------

# print('--------------Assignment 4--------------------')

my_friends = []
list_max = 4

while len(my_friends) < list_max:
	name = input('Enter name of your friend: ').strip()

	if name.isupper():
		print('Name not valid, should not be in all uppercase.')
		continue

	elif name.istitle():
		my_friends.append(name)
		print(f'Friend {name} added. Names left in the list: {list_max - len(my_friends)}')

	elif name.islower():
		my_friends.append(name.capitalize())
		print(f'Friend {name} => 1st Letter Become Capital \
						\nNames left in the list: {list_max - len(my_friends)}')
	else:
		print('Invalid name')

print("Final list of friends:", my_friends)

