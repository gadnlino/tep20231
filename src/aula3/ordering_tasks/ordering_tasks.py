adlist = {}
degrees = {}

def top_sort(vert):

    sorting = []

    while (len(vert) > 0):
        for v in adlist[vert[0]]:
            degrees[v] = degrees[v] - 1

            if(degrees[v] == 0):
                vert.append(v)
        
        sorting.append(vert.pop(0))
    
    return sorting

while True:

    numbers = list(map(lambda x : int(x), str(input()).split(" ")))

    n = numbers[0]
    m = numbers[1]
    
    if(n == 0 and m == n):
        break

    for i in range(n):
        adlist[i] = []
        degrees[i] = 0

    for __ in range(m):
        edge = list(map(lambda x : int(x), str(input()).split(" ")))

        vi = edge[0]-1
        vj = edge[1]-1

        adlist[vi].append(vj)
        adlist[vj].append(vi)

        degrees[vj] = degrees[vj] + 1
        
    initial = []

    for k, v in degrees.items():
        if(v == 0):
            initial.append(k)
    
    sorting = top_sort(initial)

    out = " ".join(map(lambda x : str(x+1), sorting))

    print(out)