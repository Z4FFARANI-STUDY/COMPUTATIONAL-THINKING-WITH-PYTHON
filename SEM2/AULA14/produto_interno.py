def prodint(v, w):
    if len(v) != len(w):
        return None
    soma = 0
    for i in range(len(v)):
        termo = v[i]*w[i]
        print(f"i={i} - v[{i}]={v[i]} - w[{i}]={w[i]} - {termo}")
        soma += termo
    return soma

v = [2,2,3,4,5,6,7,8,9]
w = [2,2,3,4,5,6,7,8,9]
print(prodint(v,w))