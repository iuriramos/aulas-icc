import csv
filename = "DM_ALUNO.CSV"

f = open(filename, "r", encoding="latin_1", newline="")
reader = csv.reader(f, delimiter="|")

tabela = {}
menor_ano = 9999
maior_ano = 0000

ja_achei = False

for i, row in enumerate(reader):
    print(i)
    
    if row[0] == "2" and row[6] == "127": #Código da IES e Curso
        ja_achei = True

        if (int(row[118]),int(row[55])) in tabela:
            tabela[(int(row[118]),int(row[55]))] += 1
        else:
            tabela[(int(row[118]),int(row[55]))] = 0
        
        if menor_ano > int(row[118]):
            menor_ano = int(row[118])

        if maior_ano < int(row[118]):
            maior_ano = int(row[118])
    else:
        if ja_achei:
            break
    
#imprime tabela formatada
print("------------------------------------------------------------------------------------- ")
print("|\t|\t|\t|\t|Transfer.\t|\t|\t|".expandtabs(12))
print("|\t|\t|Matricula\t|Desvinc.\t|para outro\t|\t|\t|".expandtabs(12))
print("|\t|Cursando\t|Trancada\t|do Curso\t|curso UnB\t|Formado\t|Falecido\t|".expandtabs(12))

for i in range(menor_ano, maior_ano+1):
    print("------------------------------------------------------------------------------------- ")
    print("|", i, end="")
    anterior = i
    for j in range(2, 7+1):
        print("\t|".expandtabs(12-len(str(anterior))-2), tabela.get((i,j), 0), end="")
        anterior = tabela.get((i,j), 0)
    print("\t|".expandtabs(12-len(str(anterior))-2))
print("------------------------------------------------------------------------------------- ")
