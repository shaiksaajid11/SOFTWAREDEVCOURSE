p = ["aaaa","saajid","bbb"]
d=1
for i in range(len(p)):
    if i==0:
        d=p[i][0]
    elif i>0:
        d=d+p[i][0]
print(d)