#Tasks:
#1. Fazer as variáveis, dentro das restrições (input vazio)
#2. Imprimir as informações dos usuários
#3. Imprimir os impedimentos
p = float(input())
i = int(input())
doc = str()
if i == 17 or i == 16: #Pode ocasionar um erro, mas parece certo
    doc = input()
bs = input()
drog = input()
doa1 = input()
Mdoa1 = int()
doa12 = int()
if doa1 == "N":
    Mdoa1 = int(input())
    doa12 = int(input())
sex = input()
grav = str()
ama = str()
baby = int()
if sex == "F":
    grav = input()
    ama = input()
    if ama == "S":
        baby = int(input())
print(f"Peso: {p}")
print(f"Idade: {i}")
if i == 17 or i == 16:
    print(f"Documento de autorizacao: {doc}")
print(f"Boa saude: {bs}")
print(f"Uso drogas injetaveis: {drog}")
print(f"Primeira doacao: {doa1}")
if doa1 == "N":
    print(f"Meses desde ultima doacao: {Mdoa1}")
    print(f"Doacoes nos ultimos 12 meses: {doa12}")
print(f"Sexo biologico: {sex}")
if sex == "F":
    print(f"Gravidez: {grav}")
    print(f"Amamentando: {ama}")
    if ama == "S":
        print(f"Meses bebe: {baby}")
Impe = False
if p < 50: #Pode ser o erro = "Peso mínimo: 50 kg" = CORIGIDO
    print("Impedimento: abaixo do peso minimo.")
    Impe = True
if i < 16:
    print("Impedimento: menor de 16 anos.")
    Impe = True
if i >= 16 and i < 18 and doc == "N":
    print("Impedimento: menor de 18 anos, sem consentimento dos responsaveis.")
    Impe = True
if i > 60 and doa1 == "S": #tinha erro aqui = RESOLVIDO
    print("Impedimento: maior de 60 anos, primeira doacao.")
    Impe = True
if i > 69: #Pode ser um ero (menos provável), PELA LÓGICA NÃO É UM ERRO
    print("Impedimento: maior de 69 anos.")
    Impe = True
if bs == "N":
    print("Impedimento: nao esta em boa saude.")
    Impe = True
if drog == "S":
    print("Impedimento: uso de drogas injetaveis.")
    Impe = True
if sex == "M":
    if doa1 == "N" and Mdoa1 < 2: #Pode ser esse o erro. Foi aparentemente corrigido
        print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
        Impe = True
    if doa1 == "N" and doa12 >= 4: #Erro? Aqui, talvez não faça sentido colocar maior que 4
        print("Impedimento: numero maximo de doacoes anuais foi atingido.")
        Impe = True
if sex == "F":
    if doa1 == "N" and Mdoa1 < 3: #Se esse for o erro, então a linha 66 está certa
        print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
        Impe = True
    if doa1 == "N" and doa12 >= 3:
        print("Impedimento: numero maximo de doacoes anuais foi atingido.")
        Impe = True
    if grav == "S":
        print("Impedimento: gravidez.")
        Impe = True
    if ama == "S" and baby < 12: #tinha erro aqui : resolvido
        print("Impedimento: amamentacao.")
        Impe = True
if not Impe:
    print("Procure um hemocentro.")
