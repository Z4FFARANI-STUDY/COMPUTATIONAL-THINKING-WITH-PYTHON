m = [
    [0,0],
    [3,0]
]

def esparsa(m):
    qtde = 0
    for i in m:
        for j in i:
            if j == 0:
                qtde += 1
                if qtde > len(m) * len(m[0]) / 2
                    return True
    return False
print(esparsa(m))