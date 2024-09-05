# ^^^^^^^^^^^^^^Solving Assignment from(11:18)^^^^^^^^^^^^^^^

# --------------Assignment 1 -------------------
# "Hello 'Osama', How You Doing \ """ Your Age Is "38"" + And Your Country Is: Egypt
name = 'Abdul-rahman'
age = 20
gpa = 3.29
my_country = "Egypt"
print('''"Hello '%s', How you Doing \\"""your Age Is "%d"" + And Your Country Is: %s and my GpA:%.2f''' %(name,age,my_country,gpa))
# ----------------------------------------------

# --------------Assignment 2 ------------------
# "Hello 'Osama', How You Doing \
# """ Your Age Is "38"" +
# And Your Country Is: Egypt

print('''"Hello '{:s}', How You Doing \\
"""Your Age Is "{:d}" + 
And Your Country Is: {:s} '''.format(name,age,my_country))
# ===> or that
print(f'''"hello '{name}', how you doing \\
"""your age is "{age}" + 
and your country is: {my_country} '''.capitalize())
# ----------------------------------------------
print('=' * 50)
# --------------Assignment 3 -------------------
Name = "Elzero"
print(Name[2:])
print(Name[1]+'\n'+Name[2]+'\n'+Name[5])
# ----------------------------------------------

# --------------Assignment 4 -------------------
# Needed Output
# "lze"
# "Ezr"
# "rzE"
print(Name[1:4] + '\n' + Name[::2] )
print(Name[-2::-2])
# ----------------------------------------------
print('=' * 50)
# --------------Assignment 5 -------------------
Name="@#@#Abdul-Rahman@#@#"
print(Name.strip("@#"))
# ----------------------------------------------
print('=' * 50)
# --------------Assignment 6 -------------------
n1, n2, n3, n4, n5 = "9", '15', '150', '950', '1500'
print(n1.zfill(4))
print(n2.zfill(4))
print(n3.zfill(4))
print(n4.zfill(4))
print(n5.zfill(4))
# ---------------------------------------------
print('=' * 50)
# --------------Assignment 7 ------------------
name1="Abdo"
name2='Abdulrahman_Rezk'
print(name1.rjust(20, '@'))
print(len(name2))
print(name2.rjust(20,'@'))
# ---------------------------------------------
print('=' * 50)
# --------------Assignment 8 ------------------
name='aBDOrEZK'
print(name.swapcase())
# ---------------------------------------------
print('=' * 50)
# --------------Assignment 9 ------------------
msg = "I love python And Although love Elzero Web School, and I love you"
print(msg.count("love"))
# ---------------------------------------------
print('=' * 50)
# --------------Assignment 10 ------------------
name='Abdo-Rezk'
print(name.index("-"))
# ---------------------------------------------
print('=' * 50)
# --------------Assignment 11 ------------------
msg = "I >3 anything And Although >3 Elzero Web School"
print(msg.replace(">3", "love",1))
# ---------------------------------------------
print('=' * 50)
# --------------Assignment 12 ------------------
msg = "I >3 anything And Although >3 Elzero Web School"
print(msg.replace(">3", "love"))
# ---------------------------------------------
print('=' * 50)
# --------------Assignment 13 ------------------
name='Abdulraham_Rezk'
age= 20
gpa= 3.29
print(f'HI I am: {name}\nMy Age: {age:d}\nMyGpa: {gpa:.3f} ')
# ----------------END-----------------------------