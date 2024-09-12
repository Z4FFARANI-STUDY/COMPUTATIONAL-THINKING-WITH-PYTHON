l = [1,10,20,45]

def soma(*params):
    res = 0
    for i in params:
        res += i
    return res

print(soma(*l))
