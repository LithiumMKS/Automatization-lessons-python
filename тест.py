for e in range(1, 151):
    for b in range(1, 151):
        if b > e:
            break
        for c in range(1, 151):
            if c > e:
                break
            for d in range(1, 151):
                if d > e:
                    break
                for a in range(1, 151):
                    if a > e and (a + b + c + d) > e:
                        break
                    if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                        print(f'a ={a} , b = {b}, c = {c}, d = {d}, e = {e}')
                        break

