tup = ("I",)
print(type(tup))

tup = tup + ("r","o","n","h","a","c","k",)
print(tup)

tup1 = tup[:4]
tup2 = tup[-4:]
print(tup1)
print(tup2)

tup3 = tup1 + tup2
print(tup3)
print(tup == tup3)

print(len(tup1),len(tup2),len(tup3))
e = len(tup1) + len(tup2)
print(e == len(tup3))

if "h" in tup3:
    print(tup3.index("h"))

letters = ["a","b","c","d","e"]

for k in letters:
    if k in tup3:
        print(True)
    else:
        print(False)

for k in letters:
    if k in tup3:
        c = tup3.count(k)
        print(f"{k} = {c}")

