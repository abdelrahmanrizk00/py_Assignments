# ^^^^^^^^^^^^^^Solving Assignment from(38:40)^^^^^^^^^^^^^^^

print('----- ----Assignment 1 --------------------')
num_1 = int(input('Enter first number : ').strip())
num_2 = int(input('Enter second number : ').strip())

operator = input("choose operation ('+', '-', '*', '/', '%') ? ").strip()

if operator == '+':
	print(f'Result of >> {num_1}+{num_2}= {num_1 + num_2}')
elif operator == '-':
	print(f'Result of >> {num_1}-{num_2}= {num_1 - num_2}')
elif operator == '*':
	print(f'Result of >> {num_1}*{num_2}= {num_1 * num_2}')
elif operator == '/':
	print(f'Result of >> {num_1}/{num_2}= {num_1 / num_2}')
elif operator == '%':
	print(f'Result of >> {num_1}%{num_2}= {num_1 % num_2}')
else:
	print('please check your inputs.')
#------------------------------------------------

print('--------------Assignment 2 --------------------')

age = 16
print('App Is Suitable For You' if age > 16 else 'App Is Not Suitable For You')
#------------------------------------------------

print('--------------Assignment 3 --------------------')

age = int(input('Enter your age her : ').strip())

m = age * 12
w = m * 4
d = w * 7
h = d * 24
mi = h * 60
se = mi * 60
if age > 10 & age < 100 :
	print(f"Your Age In Months Is {m} Months")
	print(f"Your Age In weeks  Is {w:,} weeks ")
	print(f"Your Age In Days   Is {d:,} Days  ")
	print(f"Your Age In Hours  Is {h:,} Hours ")
	print(f"Your Age In minutes Is {mi:,} minutes ")
	print(f"Your Age In seconds Is {se:,} seconds")

else:
	print("please check your age ")
#------------------------------------------------

print('--------------Assignment 4 --------------------')

country = input("Input Your Country : ").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

if country in countries:
	print(f'Your Country Eligible For Discount And The Price After Discount Is ${price - discount}')
else:
	print(f'Your Country Not Eligible For Discount And The Price Is ${price}')