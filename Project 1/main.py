outcomes = 0
indexy = 0


for i in range(0,8):
    for j in range(0,8):
        if i < j:
            for k in range(0,8):
                if k > i and k > j:
                    for l in range(0,8):
                        if l > i and l > j and l > k:
                            for h in range(0,8):
                                if h > i and h > j and h > k and h > l:
                                    for q in range(1,8):
                                        for w in range(1,8):
                                            if q != w:
                                                for e in range(1,8):
                                                    if e != q and e != w:
                                                        for r in range(1,8):
                                                            if r != e and r != q and r != w:
                                                                for t in range(1,8):
                                                                    if t != e and t != r and t != w and t != q:
                                                                        password = [0,0,0,0,0,0,0,0]
                                                                        password[i] = q
                                                                        password[j] = w
                                                                        password[k] = e
                                                                        password[l] = r
                                                                        password[h] = t
                                                                        outcomes += 1
                                                                        if(outcomes <= 100):
                                                                            print(str(password[0]) + str(password[1]) + str(password[2]) + str(password[3]) + str(password[4])  + str(password[5]) + str(password[6]) + str(password[7]))

print(outcomes)