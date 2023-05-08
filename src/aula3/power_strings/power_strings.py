while True:

    line = str(input()).strip()

    if(line == '.'):
        break

    substrs = set()

    sz = len(line)

    for tam in range(1, sz+1):
        for j in range(tam, sz+1):
            sub = line[j-tam: j]
            substrs.add(sub)
    
    values = list(map(lambda x: (x, line.count(x)), substrs))

    print(values)

    maxx = max(map(lambda x: x[1], values))

    print(maxx)
