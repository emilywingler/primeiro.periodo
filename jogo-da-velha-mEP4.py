######################################################
# Programção I / Programação Funcional (2022/1)
# miniEP4 - Jogo da Velha
# Nome: Emily Wingler Gonçalves
# Matrícula: 2022100287
######################################################

######################################################
# LEMBRE-SE:
# - Não é permitido usar estruturas de repetição,
#   funções impuras e operações que não sejam do 
#   Paradigma Funcional.
# - Você não pode usar variáveis globais;
# - Não use funções recursivas (não há necessidade);
# - Você deve seguir o código base disponibilizado, 
#   não sendo permitido a alteração do nome e/ou
#   lista de parâmetros das funções dadas;
# - Caso precise, você PODE criar outras funções;
# - Não é permitido a utilização de lista, tuplas 
#   ou qualquer outro tipo estruturado para 
#   “facilitar” a manipulação dos dados. Você deve 
#   sempre trabalhar com as 9 variáveis que 
#   representam as posições no tabuleiro;
#
# Dica: Leia o docstring de cada função para saber o
#       que cada uma deve fazer e retornar.
######################################################

def imprimeTabuleiro(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e imprime o tabuleiro
    """
    print(f" {p7} | {p8} | {p9} \n---+---+---\n {p4} | {p5} | {p6} \n---+---+---\n {p1} | {p2} | {p3} ")

def rec(r):
    if r == " " or r == "x" or r == "o":
        return True
    else:
        return False

def entradaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    verifica se os valores são válidos, ou seja, retorna True
    se cada variável possui " " ou "x" ou "o" e False, caso contrário.
    """
    if rec(p1) == rec(p2) == rec(p3) == rec(p4) == rec(p5) == rec(p6) == rec(p7) == rec(p8) == rec(p9):
        return True
    else:
        return False

def contasimbolo(p1, p2, p3, p4, p5, p6, p7, p8, p9, s):
    c = 0
    if p1 == s:
        c += 1
    if p2 == s:
        c += 1
    if p3 == s:
        c += 1
    if p4 == s:
        c += 1
    if p5 == s:
        c += 1
    if p6 == s:
        c += 1
    if p7 == s:
        c += 1
    if p8 == s:
        c += 1
    if p9 == s:
        c += 1
    return c
def jogadaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    verifica se os valores formam uma jogada válida.

    Retorna True se a jogada for válida e False, caso contrário
    """
    return True if abs(contasimbolo(p1,p2,p3,p4,p5,p6,p7,p8,p9,"x")- contasimbolo(p1,p2,p3,p4,p5,p6,p7,p8,p9,"o")) < 2 else False

def compara(a, b, c):
    if a == b == c== "x": 
        print("O jogador 'x' venceu!")
        return 0
    elif a == b == c == "o":
        print("O jogador 'o' venceu!")
        return 0
    else:
        return None

def contadora(x, y):
    if x == y:
        return 1
    else:
        return 0

def verificaJogada(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    imprime se um jogador ('x' ou 'o') venceu a jogada. 
    (Cada variável representa uma posição no tabuleiro)
    """
    A = compara(p1, p2, p3)
    B = compara(p4, p5, p6)
    C = compara(p7, p8, p9)
    D = compara(p1, p4, p7)
    E = compara(p2, p8, p5)
    F = compara(p3, p6, p9)
    G = compara(p1, p5, p9)
    H = compara(p7, p5, p3)
    if A == B == C == D == E == F == G == H == None:
        if contasimbolo(p1, p2, p3, p4, p5, p6, p7, p8, p9, " ") == 0:
            print("Empate!")
        else:
            print("O jogo nao terminou!")

def main():
    t1 = input()
    t2 = input()
    t3 = input()
    t4 = input()
    t5 = input()
    t6 = input()
    t7 = input()
    t8 = input()
    t9 = input()
    imprimeTabuleiro(t1, t2, t3, t4, t5, t6, t7, t8, t9)
    if entradaValida(t1, t2, t3, t4, t5, t6, t7, t8, t9) == False:
        print("Entrada invalida!")
    elif jogadaValida(t1, t2, t3, t4, t5, t6, t7, t8, t9) == False:
        print("Jogada invalida!")
    else:
        verificaJogada(t1, t2, t3, t4, t5, t6, t7, t8, t9)

main()

