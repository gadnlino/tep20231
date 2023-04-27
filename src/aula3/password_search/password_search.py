while True:
    try:
        line = str(input()).strip()

        if(len(line) == 0):
            break

        args = line.split(" ")

        passwd_size = int(args[0])
        msg = str(args[1])

        substrs = {}

        for i in range(passwd_size, len(msg)+1):
            sub = msg[i-passwd_size : i]
            
            if(sub not in substrs):
                substrs[sub] = 1
            else:
                substrs[sub] += 1
        
        #print(substrs)

        maxx = -1
        passwd = None

        for k, v in substrs.items():
            if v > maxx:
                maxx = v
                passwd = k

        print(passwd)        
    except EOFError:
        break