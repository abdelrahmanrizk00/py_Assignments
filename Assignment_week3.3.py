# ^^^^^^^^^^^^^^Solving Assignment from(24:25)^^^^^^^^^^^^^^^

# --------------Assignment 1 ------------------
name = "Abdulrahamn.Rezk",
print(name)
print(type(name))
print(len(name))
#----------------------------------------------

# --------------Assignment 2 ------------------
friends=("Osama", "Abdo","Hamam")
n_friends=list(friends)
n_friends[0]="Elzero"
friends=tuple(n_friends)
print(friends)
print(type(friends))
print(len(friends), 'Elemnts')
# ---------------------------------------------

# --------------Assignment 3 ------------------
Num = 1, 2, 3
Alpha = "A", "B", "c"
alphnum = Num+Alpha
print(alphnum)
print(f"{len(alphnum)} Elements")
print(alphnum[3])
# ---------------------------------------------
print('='*50)
# --------------Assignment 4 ------------------
new = (101, "Abdo", "ALi", True, .08206)
a, b, c, _, e = new
print(f'''a= {a} 
b= {b} 
c= {c}
e= {e}''')
# ----------------END---------------------------