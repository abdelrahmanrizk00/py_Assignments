# ^^^^^^^^^^^^^^Solving Assignment from(38:40)^^^^^^^^^^^^^^^

print('--------------Assignment 1 --------------------')

name = input('Enter your name : ').strip().capitalize()
print(f'Hello {name}, Happy To See You Here.')

age = int(input('Enter your age : '))
if age < 16:
	print('Hello Your Age Is Under 16, Some Articles Is Not Suitable For You')
elif age > 16:
	print(f'Hello Your Age Is {age}, All Articles Is Suitable For You')

#------------------------------------------------
print('--------------Assignment 2 --------------------')

first_name = input('Enter Your first name : ').strip().capitalize()
second_name = input('Enter Your second name : ').strip().capitalize()
print(f'Hello {first_name} {second_name:.1}.')

#------------------------------------------------
print('--------------Assignment 3 --------------------')

email = str(input('Enter your personal mail : ')).strip().lower()
user_name = email[:email.index('@')]
site = email[email.index('@') + 1: email.index(".c")]
# how to get top domain
second_part = email[email.index('@') + 1:]
domain = second_part[second_part.index('.') + 1:]

print(f"Hello {user_name.capitalize()} in my program")
print(f"Email Service Provider Is >> {site}")
print(f'Top Level Domain Is >> {domain}')