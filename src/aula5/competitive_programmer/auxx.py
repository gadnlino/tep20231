import json

alll = list()

for i in range(30):
    m = i * 60
    print(m)
    nstr = str(m)
    s = set()
    
    for c in nstr:
        s.add(c)

    ls = list(s)

    if(ls not in alll):
        alll.append(ls)

print(json.dumps(alll))
    