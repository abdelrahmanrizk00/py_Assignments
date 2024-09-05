# ^^^^^^^^^^^^^^Solving Assignment from(21:23)^^^^^^^^^^^^^^^

# --------------Assignment 1 ------------------

friends=["saad", "Zizo", "Kholio", "Desha", "Farghaly", "Bebo"]
print(friends[0])
print(friends.pop(0))
print(friends[-1])
print(friends.pop(-1))
#----------------------------------------------
print('=' * 50)
# --------------Assignment 2 ------------------

old_friends=["sobhy", "khaled", "Abdo", "ELDOh","Adel"]
print(old_friends[::2])
print(old_friends[1::2])
# ---------------------------------------------

# --------------Assignment 3 ------------------

old_friends=["sobhy", "khaled", "Abdo", "ELDOh","Adel"]
print(old_friends[1], old_friends[2], old_friends[3])
print(old_friends[-1], old_friends[-2])
# ---------------------------------------------
print('=' * 50)
# --------------Assignment 4 ------------------

old_friends=["sobhy", "khaled", "Abdo", "ELDOh","Adel"]
old_friends[-2] = "Elzero"
old_friends[-1] = "Elzero"
# ---------------------------------------------
print('=' * 50)
# --------------Assignment 5 ------------------
print(old_friends)
old_friends.insert(0,"Ahmed")
print(old_friends)
old_friends.append("Boody")
print(old_friends)
# ---------------------------------------------
print('=' * 50)
# --------------Assignment 6 ------------------

# print(old_friends.pop(-1))
old_friends.remove("Ahmed")
old_friends.remove("sobhy")
old_friends.remove("Boody")
print(old_friends)
# ---------------------------------------------
print('=' * 50)
# --------------Assignment 7 ------------------
school_frieds = ["fathy", "khalifa", "gooda", "amir"]
c = school_frieds.copy()
uni_friends = ["Abdo", "Ahmed", "Hamam", "Nasr"]
school_frieds.extend(uni_friends)
print(school_frieds)
# ---------------------------------------------
print('=' * 50)
# --------------Assignment 8 ------------------
c.sort()
print(c)
c.sort(reverse=True)
print(c)
print(len(school_frieds))
#-----------------------------------------------
print('=' * 50)
# --------------Assignment 9 -------------------

prog_lang =["py", "Jv", "C", "C++", "Kotlin", ['web', 'Embededd', 'cyber', 'Ai']]
print(prog_lang[-1][-1])
print(prog_lang[-1][0])
# ----------------END---------------------------
