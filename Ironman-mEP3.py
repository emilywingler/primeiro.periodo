######################################################
# Programção I / Programação Funcional (2022/1)
# miniEP3 - Ironman
# Nome: Emily Wingler Gonçalves
# Matrícula: 2022100287
######################################################

######################################################
# LEMBRE-SE:
# - Não é permitido usar estruturas de repetição,
#   funções impuras e operações que não sejam do
#   Paradigma Funcional.
# - Você NÃO pode usar variáveis globais;
# - Não use funções recursivas (não há necessidade);
# - Caso precise, você PODE criar outras funções;
# - Evite ao máximo a replicação de código. 
#   Códigos que não atendam a esse requisito 
#   valerão 50% da pontuação;
######################################################

############
# Tasks iniciais:
# 1.Criar uma função com os valores de entrada: sexo e idade
# 2.Criar uma função com os valores de entrada: Tempos
# 3.Criar uma função para somar todos os tempos -- RETORNA TEMPO DE ATLETA EM MINUTOS
# 4.Criar uma função converte tempo, entregando horas e minutos(ver exercícios anteriores)
#  -obs.: colocar para retornar horas e minutos, mas que entrega
#  os valores dos segundos (à cargo de organização(OU NÃO)) -- RETORNA TEMPO DE ATLETA EM HORAS
# 5.Criar uma função que relacione idade e sexo de forma que
# comece com a condicional relacionada ao sexo, e depois vá 
# para as idades e tempos -- RETORNA TEMPO NECESSÁRIO EM HORAS
# 6. Criar a função subtraitempos: ela subtrai o tempo necessário em horas e o tempo de atleta
# e entrega o valor em módulo
# 7. Criar função "Conseguiu índice?": compara o tempo de atleta >= ao tempo
# necessário em sua categoria (retorna se ficou acima ou abaixo do índice)
# Problema de subtração: print(f"0{8}")
# Problema nos inputs = foi resolvido ao colocar tudo na main
# Para fazer as outras funções funcionarem, utilizei parâmetros
########################################

def restriçãopelosexomaiúscula(s):
    """
    Irá impedir a repetição de código na parte de 
    impressão por causa do usos dos artigos
    """
    if s == "F" or s == "f":
        A = "A"
        return A
    else:
        OO = "O"
        return OO


def restriçãopelosexominúscula(s):
    """
    Irá impedir a repetição de código na parte de 
    impressão por causa do usos dos artigos
    """
    if s == "F" or s == "f":
        a = "a"
        return a
    else:
        o = "o"
        return o


def somatempo(H20, T1, bike, T2, run):
    """
    Soma todos os tempos realizados pelo esportista.
    """
    return H20 + T1 + bike + T2 + run


def converte(H20, T1, bike, T2, run):
    """
    converte o tempo em minutos, entregando - o em horas e minutos
    (retornará o "tempo do atleta" em horas).
    """
    H = somatempo(H20, T1, bike, T2, run) // 60
    M = somatempo(H20, T1, bike, T2, run) % 60
    return H, M


def restringir(s, i):
    """
    Utilizada para restringir os valores digitados de
    acordo com a tabela especificada no trabalho,
    relacionando sexo, idade e tempo.
    """
    h = int
    m = int
    if s == "F" or s == "f":
        if i >= 18 and i <= 29:
            h = 8
            m = 10
            return h, m
        elif i >= 30 and i <= 34:
            h = 8
            m = 20
            return h, m
        elif i >= 35 and i <= 39:
            h = 8
            m = 40
            return h, m
        elif i >= 40 and i <= 44:
            h = 9
            m = 00
            return h, m
        elif i >= 45 and i <= 49:
            h = 9
            m = 20
            return h, m
        elif i >= 50 and i <= 54:
            h = 9
            m = 40
            return h, m
        elif i >= 55 and i <= 59:
            h = 10
            m = 00
            return h, m
        elif i >= 60 and i <= 64:
            h = 10
            m = 30
            return h, m
        elif i >= 65 and i <= 69:
            h = 11
            m = 00
            return h, m
        elif i >= 70 and i <= 74:
            h = 11
            m = 45
            return h, m
        elif i >= 75 and i <= 79:
            h = 12
            m = 30
            return h, m
        else:
            h = 13
            m = 30
            return h, m
    if s == "M" or s == "m":
        if i >= 18 and i <= 29:
            h = 8
            m = 00
            return h, m
        elif i >= 30 and i <= 34:
            h = 8
            m = 10
            return h, m
        elif i >= 35 and i <= 39:
            h = 8
            m = 25
            return h, m
        elif i >= 40 and i <= 44:
            h = 8
            m = 35
            return h, m
        elif i >= 45 and i <= 49:
            h = 8
            m = 50
            return h, m
        elif i >= 50 and i <= 54:
            h = 9
            m = 00
            return h, m
        elif i >= 55 and i <= 59:
            h = 9
            m = 15
            return h, m
        elif i >= 60 and i <= 64:
            h = 9
            m = 30
            return h, m
        elif i >= 65 and i <= 69:
            h = 9
            m = 50
            return h, m
        elif i >= 70 and i <= 74:
            h = 10
            m = 20
            return h, m
        elif i >= 75 and i <= 79:
            h = 11
            m = 00
            return h, m
        else:
            h = 12
            m = 00
            return h, m


def converte2(s, i,):
    """
    tranforma horas e minutos, em apenas minutos novamente (para 
    o "tempo necessário")
    """
    h, m = restringir(s, i)
    return h*60 + m


def subtraitempos(s, i, H2O, T1, bike, T2, run):
    """
    Verifica se há alguma diferença entre o Tempo do atleta e o
    Tempo necessario
    """
    if converte2(s, i) == somatempo(H2O, T1, bike, T2, run) :
        return 0
    else:
        return converte2(s, i)- somatempo(H2O, T1, bike, T2, run)


def tempodeatleta(s, H2O, T1, bike, T2, run):
    """
    Imprimirá os valores de saída quanto ao "tempo de atleta",
    relacionando os indíces.
    """
    H, M = converte(H2O, T1, bike, T2, run)
    if H < 10 and M < 10:
        print(f"Tempo d{restriçãopelosexominúscula(s)} atleta: 0{H}h 0{M}min")
    elif H < 10 and M >= 10:
        print(f"Tempo d{restriçãopelosexominúscula(s)} atleta: 0{H}h {M}min")
    elif H >= 10 and M < 10:
        print(f"Tempo d{restriçãopelosexominúscula(s)} atleta: {H}h 0{M}min")
    else:
        print(f"Tempo d{restriçãopelosexominúscula(s)} atleta: {H}h {M}min")

def temponecessario(s, i):
    """
    Imprimirá os valores calculdos anteriormente quanto
    ao "Tempo necessário"
    """
    h, m = restringir(s, i)
    if h < 10 and m < 10:
        print(f"Tempo necessario: 0{h}h 0{m}min")
    elif h < 10 and m >= 10:
        print(f"Tempo necessario: 0{h}h {m}min")
    elif h >= 10 and m < 10:
        print(f"Tempo necessario: {h}h 0{m}min")
    else:
        print(f"Tempo necessario: {h}h {m}min")
   
def indiceetempo(s, i, H2O, T1, bike, T2, run):
    """
    Imprimirá se o atleta conseguiu o indíce, e o tempo
    de realização da prova
    """
    if subtraitempos(s, i, H2O, T1, bike, T2, run) > 0: 
        print("Conseguiu indice? SIM")
        H2 = subtraitempos() // 60
        M2 = subtraitempos() % 60
        if H2 < 10 and M2 < 10:
            print(f"{restriçãopelosexomaiúscula(s)} atleta terminou a prova 0{H2}h 0{M2}min acima do indice")
        elif H2 < 10 and M2 >= 10:
            print(f"{restriçãopelosexomaiúscula(s)} atleta terminou a prova 0{H2}h {M2}min acima do indice")
        elif H2 >= 10 and M2 < 10:
            print(f"{restriçãopelosexomaiúscula(s)} atleta terminou a prova {H2}h 0{M2}min acima do indice")
        else:
            print(f"{restriçãopelosexomaiúscula(s)} atleta terminou a prova {H2}h {M2}min acima do indice")
    elif subtraitempos(s, i, H2O, T1, bike, T2, run) < 0:
        print("Conseguiu indice? NAO")
        y = abs(subtraitempos())
        H2 = y // 60
        M2 = y % 60
        if H2 < 10 and M2 < 10:
            print(f"{restriçãopelosexomaiúscula(s)} atleta terminou a prova 0{H2}h 0{M2}min abaixo do indice")
        elif H2 < 10 and M2 >= 10:
            print(f"{restriçãopelosexomaiúscula(s)} atleta terminou a prova 0{H2}h {M2}min abaixo do indice")
        elif H2 >= 10 and M2 < 10:
            print(f"{restriçãopelosexomaiúscula(s)} atleta terminou a prova {H2}h 0{M2}min abaixo do indice")
        else:
            print(f"{restriçãopelosexomaiúscula(s)} atleta terminou a prova {H2}h {M2}min abaixo do indice")
    
    else:
        print("Conseguiu indice? SIM")
        if s == "F" or s == "f":
            print(f"A atleta terminou a prova 00h 00min abaixo do indice")
        else:
            print(f"O atleta terminou a prova 00h 00min abaixo do indice")


def main():
    s = input() 
    i = int(input())
    H2O = int(input())
    T1 = int(input())
    bike = int(input())
    T2 = int(input())
    run = int(input())
    restriçãopelosexomaiúscula(s)
    restriçãopelosexominúscula(s)
    somatempo(H2O, T1, bike, T2, run)
    converte(H2O, T1, bike, T2, run)
    restringir(s, i)
    converte2(s, i)
    subtraitempos(s, i, H2O, T1, bike, T2, run)
    tempodeatleta(s,H2O, T1, bike, T2, run)
    temponecessario(s, i)
    indiceetempo(s, i, H2O, T1, bike, T2, run)




main()
