import json

QuantidadeAlunos = int(input("Digite a quantidade de alunos:"))
NomesAlunos = [0] * QuantidadeAlunos
Media = [0] * QuantidadeAlunos
alunos = {"alunos": []}

for i in range(QuantidadeAlunos):
    NomesAlunos[i] = input("Digite o nome do aluno de numero: ")
    Media[i] = float(input("Digite a media do respectivo aluno: "))

for j in range(QuantidadeAlunos):
    alunos["alunos"].append(
        {
            "Nome": NomesAlunos[j],
            "Media": Media[j]
        }
    )

with open("Alunos.json", "w") as arquivo:
    json.dump(alunos, arquivo, indent=4)
