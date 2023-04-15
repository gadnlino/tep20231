n = int(input())

fn = lambda x : (1 + 2**x + 3** x + 4 ** x) % 5

fn2 = lambda x: 4 if x%4 == 0 else 0

print(fn2(n))

#print(result)