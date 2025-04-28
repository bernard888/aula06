notas = [0.0,0.0,0.0,0.0,0.0,]
soma = 0
conta = 0
for i in range(len(notas)):
    notas[i] = float(input(f"digite a nota do {i+1}° aluno: "))
for x in range (len(notas)):
    soma = soma + notas[x]
media = soma/len(notas)
for y in range(len(notas)):
    if notas[y] > media:
        conta+=1
print(f"a media da turma é {media:.1f} e o número de alunos acima da média é {conta}")
