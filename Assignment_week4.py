# ^^^^^^^^^^^^^^Solving Assignment from(26:32)^^^^^^^^^^^^^^^

print('--------------Assignment 1 --------------------')
num = [1, 2, 3, 4, 5, 1]
uniq_list = set(num)
uniq_list = list(uniq_list)
#uniq_list = list(set(num))
print(uniq_list)
print(type(uniq_list))
uniq_list.remove(5)
print(uniq_list)
print("*" * 50)
#------------------------------------------------

print('--------------Assignment 2 --------------------')
num = {1, 2, 3}
alpha = {"a", "B", "c"}
print(num | alpha)
print(num.union(alpha))
num.update(alpha)
print(num)
print("*" * 50)
# -----------------------------------------------

print('--------------Assignment 3 --------------------')
set1 = {1, 2, 3}
print(set1)
set1.clear()
print(set1)
alpha = {"a", "b", "c"}
alpha.discard("d")
alpha.remove("a")
print(alpha)
print("*" * 50)
# -----------------------------------------------

print('--------------Assignment 4 --------------------')
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5, 6}
print(s1.issubset(s2))    # The small set . isSubset(large set)
print(s2.issuperset(s1))  # The large set . isSuperset(small set)
print("*" * 50)
# -----------------------------------------------

print('--------------Assignment 5 --------------------')
dct1 = {"01": {
    "lang": "HTML",
    "progress": "10%"
    },
    "02": {
    "lang": "css",
    "progress": "1.5%"
    },
    "03": {
    "lang": "python",
    "progress": "30%"
    }
}
print(f"lang is {dct1['01']['lang']} and the progress is {dct1['01']['progress']}")
print(f"lang is {dct1['02']['lang']} and the progress is {dct1['02']['progress']}")
print(f"lang is {dct1['03']['lang']} and the progress is {dct1['03']['progress']}")
dct1['04'] = {'lang': 'Java', 'progress': '0%'}
print(dct1.keys())
print(dct1.values())
print(f"lang is {dct1['04']['lang']} and the progress is {dct1['04']['progress']}")
# ----------------END-----------------------------