strings = []

while True:
    try:
        st = str(input())

        strings.append(st)

        if(len(strings) == 2):

            chars = set(strings[0][:]).union(strings[1][:])

            table = {}

            for ch in chars:
                table[ch] = [strings[0].count(ch), strings[1].count(ch)]

            common_ch = []

            for k, v in table.items():
                if v[0] > 0 and v[1] > 0:
                    common_ch.append(k * min(v[0], v[1]))
            
            common_ch.sort()

            out = "".join(map(lambda x: str(x), common_ch))

            print(out)

            strings.clear()
    except EOFError:
        break