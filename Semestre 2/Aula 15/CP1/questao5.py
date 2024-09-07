def transposta(A):
    trans = []
    for j in range(len(A[0])):
        linha = []
        for i in range(len(A)):
            linha.append(A[i][j])
        trans.append(linha)
    return trans
