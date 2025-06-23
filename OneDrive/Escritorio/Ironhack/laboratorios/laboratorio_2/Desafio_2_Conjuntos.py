import random

sample_list = random.sample(range(0,101),80)

set1 = set(sample_list)

sample_list2 = random.choices(range(0,101),k=80)
set2 = set(sample_list2)



set3 = [n for n in set1 if n not in set2]
set3 = set(set3)

set4 =[n for n in set2 if n not in set1]
set4 = set(set4)

set5 = [n for n in set1 if n in set2]
set5 = set(set5)

print(f"{len(set1)}: A (80 valores unicos aleatorios)")
print(f"{len(set2)}: B (80 valores aleatorios que se pueden repetir)")
print(f"{len(set3)}: numeros em A mas nao em B")
print(f"{len(set4)}: numeros em B mas nao em A")
print(f"{len(set5)}: numeros em A e em B")

set6 = set()
set6.update(set3,set5)

print(set1 == set6)

print(set1.issubset(set2))
print(set1.issubset(set3))

conjunto_unido1 = set3.union(set4,set5)
conjunto_final = conjunto_unido1.union(set1,set2)



list_to_remove = [1, 9, 11, 19, 21, 29, 31, 39, 41, 49, 51, 59, 61, 69, 71, 79, 81, 89, 91, 99]
set1 -= set(list_to_remove)
print(set1)
"""
set10 = set1 - set(list_to_remove)
removed=[]
for n in set1:
    if n not in set10:
        removed.append(n)
print(removed)
"""