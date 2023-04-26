strings = []

while True:
    try:
        string = str(input()).strip()

        if(len(string) == 0):
            break

        if(string.strip() == '#'):
            order = []

            maxlen = max(list(map(lambda s : len(s), strings)))

            for i in range(maxlen):
                for si in range(1, len(strings)):
                    if(i < len(strings[si-1]) and i < len(strings[si])):
                        chsi1 = strings[si-1][i]
                        chsi = strings[si][i]
                        
                        if(chsi1 in order):
                            pos = order.index(chsi1)

                            if(chsi not in order):
                                order.insert(pos+1, chsi)
                        else:
                            if(chsi1 not in order):
                                order.append(chsi1)
                            
                            if(chsi not in order):
                                order.append(chsi)
                    elif(i < len(strings[si])):
                        if(strings[si][i] not in order):
                            order.append(strings[si][i])
                # for s in strings:
                #     if(i < len(s) and s[i] not in order):
                #         order.append(s[i])

            out = "".join(map(lambda x: str(x), order))

            print(out)
            strings.clear()
        else:
            strings.append(string)
    except EOFError:
        break