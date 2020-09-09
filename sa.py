p = ["aaaa,aa, bbb"]
d=1
for i in range(len(p)):
    if p[i][0] == '"' or p[i][-1] == '"':
        d=p[i]
print(d)