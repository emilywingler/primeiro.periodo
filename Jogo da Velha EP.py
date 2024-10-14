######################################################
# Programação Funcional / Programção I (2022/2)
# EP2 - Jogo da Velha
# Nome: Emily Wingler Gonçalves 
# Matrícula: 2022100287
######################################################

import random
from os import system, name


def getMatricula():
    """
    Retorna a matricula do aluno como string
    """
    return "2022100287" 


def getNome():
    """
    Retorna o nome completo do aluno
    """
    return "Emily Wingler Gonçalves" 


def imprimeTabuleiro(L):
    """
    Recebe os valores das nove posições do tabuleiro e imprime o tabuleiro.
    - L : lista reponsável pelo tabuleiro.
    """
    print(f"\n {L[7]} | {L[8]} | {L[9]} \n---+---+---\n {L[4]} | {L[5]} | {L[6]} \n---+---+---\n {L[1]} | {L[2]} | {L[3]} \n")


def limpaTela():
    """
    Limpa o terminal.
    """
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def leValor(funcaoconversao, msg=" "):
    """
    É responsável por tentar converter o valor que o usuário
    digita, de acordo com  necessidade. Caso ela não consiga,
    irá retornar recursivamente o input, até o usuário digitar um valor que possa ser convertido.
    - funcaoconversao = tipo da conversão que será realizada. Ex.: int,float, etc.
    - msg = mensagem que virá no input inicial.
    """
    try:
        return funcaoconversao(input(msg))
    except:
        print(f"\nValor inválido. Você deve digitar um número inteiro entre 1 e 9.\n")
        return leValor(funcaoconversao, f"Em qual posição deseja jogar (1-9)?")


def jogador(L):
    """
    Recolhe a posição que o usuário quer jogar: se não for um número entre
    1-9 imprime uma mensagem de erro e retorna a própria função novamente.
    Caso a posição não esteja disponível, ela avisa o usuário e retorna a si mesma.
    Caso contrário retorna a posição escolhida.
    - L : lista responsável pelo tabuleiro;
    """
    jogada = leValor(int, "Em qual posição deseja jogar (1-9)? ")
    if jogada < 1 or jogada > 9:
        print(f"\nValor inválido. Você deve digitar um número inteiro entre 1 e 9.\n")
        return jogador(L)
    else:
        if L[jogada] != " ":
            print(f"\nJogada inválida. Você deve Jogar em um espaço vazio\n")
            return jogador(L)
        else:
            return jogada


def verificaSeGanhou(L, jog1, PCsimbolo):
    """
    Verifica a vitória (seja do computador, seja do usuário) em cada uma
    das posições possíveis. Não havendo vitória, irá verificar se há algum
    espaço vazio na lista excluindo a posição zero, se houver o jogo continua, senão
    ela imprime o tabuleiro, avisa que empatou e encerra o programa.
    - L : lista que representa o tabuleiro;
    - jog1 : simbolo do usuário;
    - PCsimbolo : simbolo do computador.
    """
    compara(L, jog1, PCsimbolo, 1, 2, 3)
    compara(L, jog1, PCsimbolo, 4, 5, 6)
    compara(L, jog1, PCsimbolo, 7, 8, 9)
    compara(L, jog1, PCsimbolo, 1, 4, 7)
    compara(L, jog1, PCsimbolo, 2, 8, 5)
    compara(L, jog1, PCsimbolo, 3, 6, 9)
    compara(L, jog1, PCsimbolo, 1, 5, 9)
    compara(L, jog1, PCsimbolo, 7, 5, 3)
    if " " not in L[1:]:
        imprimeTabuleiro(L)
        print(f"Deu velha !! \n")
        print(getNome()) # Emily W. Gonçalves
        print(getMatricula()) # 2022100287
        exit()


def compara(L, jog1, PCsimbolo, a, b, c):
    """
    É a função responsável por verificar se há uma vitória em uma determinada posição,
    seja do computador, ou do usuário. Havendo vitória, o usuário é informado por uma mensagem
    e o programa é encerrado.
    - L : lista que contém as posições do jogo;
    - jog1 : símbolo do usuário;
    - PCsimbolo : simbolo do computador;
    - a, b, c : posições a serem analisadas.
    """
    if L[a] == L[b] == L[c] == jog1:
        imprimeTabuleiro(L)
        print(f"Parabéns!!Você venceu o jogo!\n")
        print(getNome()) # Emily W. Gonçalves
        print(getMatricula()) # 2022100287
        exit()
    elif L[a] == L[b] == L[c] == PCsimbolo:
        imprimeTabuleiro(L)
        print(f"O computador venceu dessa vez!\n")
        print(getNome()) # Emily W. Gonçalves
        print(getMatricula()) # 2022100287
        exit()


def quemComeca(tabuleiro):
    """
    É responsável por decidir quem irá começar o jogo.
    Retorna 1 se for o usuário, ou 0 se for o computador.
    - tabuleiro: recebe a lista apenas com espaços, para imprimir o 
    tabuleiro caso, seja o usuário a começar.
    """
    x = int(random.choice([0, 1]))
    if x == 1:
        print(f"\nOk! Pode começar... ")
        imprimeTabuleiro(tabuleiro)
        return 1
    else:
        print(f"\nOk! O computador começa!")
        return 0


def bloqueiaOUganha(L, símbolo, a, b, c):
    """
    É responsável por analisar se há uma possibilidade de vitória
    ou de derrota, a partir de da função filter, e induzir a reação equivalente
    seja ganhar ou bloquear. Retorna uma posição da lista.
     - L : lista, geralmente o tabuleiro;
     - simbolo : os símbolos que representam cada jogador. Se for jog1
     está analisando as possibilidades de bloqueio, senão as de vitória;
     - a, b, c : posições da lista.
    """
    contasimbolo = [L[a]] + [L[b]] + [L[c]] # Forma uma lista de três elementos, com as posições indicadas
    condicao = list(filter(lambda x: x == símbolo, contasimbolo))
    if len(condicao) == 2 and " " in contasimbolo:
        return a if contasimbolo[0] == " " else b if contasimbolo[1] == " " else c
    else:
        return 0


def jogadaComputador(tabuleiro, simboloComputador):
    """
    Recebe o tabuleiro e o simbolo (X ou O) do computador e determina onde o computador deve jogar
    O tabuleiro pode estar vazio (caso o computador seja o primeiro a jogar) ou com algumas posições preenchidas, 
    sendo a posição 0 do tabuleiro descartada.

    Parâmetros:
    tabuleiro: lista de tamanho 10 representando o tabuleiro;
    simboloComputador: letra do computador.

    Retorno:
    Posição (entre 1 e 9) da jogada do computador.

    Estratégia adotada (resumidamente):
    - 1 Tentar ganhar do usuário;
    - 2 Bloquear o usuário caso ele esteja na iminência de ganhar;
    - 3 Tentando formar triângulos de quatro formas diferentes para ocasionar uma possível vitória;
    - 4 Impedir que o usuário forme as mesmas estratégias;
    - 5 Em último caso, sorteará uma posição aleatória para jogar
    """
    if simboloComputador == "X":
        jog1 = "O"
    else:
        jog1 = "X"
    if bloqueiaOUganha(tabuleiro, simboloComputador, 1, 2, 3) != 0:    # Verificando se ganha:
        return bloqueiaOUganha(tabuleiro, simboloComputador, 1, 2, 3)
    if bloqueiaOUganha(tabuleiro, simboloComputador, 4, 5, 6) != 0:
        return bloqueiaOUganha(tabuleiro, simboloComputador, 4, 5, 6)
    if bloqueiaOUganha(tabuleiro, simboloComputador, 7, 8, 9) != 0:
        return bloqueiaOUganha(tabuleiro, simboloComputador, 7, 8, 9)
    if bloqueiaOUganha(tabuleiro, simboloComputador, 1, 4, 7) != 0:
        return bloqueiaOUganha(tabuleiro, simboloComputador, 1, 4, 7)
    if bloqueiaOUganha(tabuleiro, simboloComputador, 2, 8, 5) != 0:
        return bloqueiaOUganha(tabuleiro, simboloComputador, 2, 8, 5)
    if bloqueiaOUganha(tabuleiro, simboloComputador, 3, 6, 9) != 0:
        return bloqueiaOUganha(tabuleiro, simboloComputador, 3, 6, 9)
    if bloqueiaOUganha(tabuleiro, simboloComputador, 1, 5, 9) != 0:
        return bloqueiaOUganha(tabuleiro, simboloComputador, 1, 5, 9)
    if bloqueiaOUganha(tabuleiro, simboloComputador, 7, 5, 3) != 0:
        return bloqueiaOUganha(tabuleiro, simboloComputador, 7, 5, 3)
    if bloqueiaOUganha(tabuleiro, jog1, 1, 2, 3) != 0:    # Verificando se bloqueia
        return bloqueiaOUganha(tabuleiro, jog1, 1, 2, 3)
    if bloqueiaOUganha(tabuleiro, jog1, 4, 5, 6) != 0:
        return bloqueiaOUganha(tabuleiro, jog1, 4, 5, 6)
    if bloqueiaOUganha(tabuleiro, jog1, 7, 8, 9) != 0:
        return bloqueiaOUganha(tabuleiro, jog1, 7, 8, 9)
    if bloqueiaOUganha(tabuleiro, jog1, 1, 4, 7) != 0:
        return bloqueiaOUganha(tabuleiro, jog1, 1, 4, 7)
    if bloqueiaOUganha(tabuleiro, jog1, 2, 8, 5) != 0:
        return bloqueiaOUganha(tabuleiro, jog1, 2, 8, 5)
    if bloqueiaOUganha(tabuleiro, jog1, 3, 6, 9) != 0:
        return bloqueiaOUganha(tabuleiro, jog1, 3, 6, 9)
    if bloqueiaOUganha(tabuleiro, jog1, 1, 5, 9) != 0:
        return bloqueiaOUganha(tabuleiro, jog1, 1, 5, 9)
    if bloqueiaOUganha(tabuleiro, jog1, 7, 5, 3) != 0:
        return bloqueiaOUganha(tabuleiro, jog1, 7, 5, 3)
    if tabuleiro[5] == " " and tabuleiro[1] != jog1 and tabuleiro[7] != jog1: # Aplicando a estratégia dos triângulos com o centro e o canto.
        return 5
    if tabuleiro[5] == simboloComputador and tabuleiro[1] == " " and tabuleiro[7] != jog1:
        return 1
    if tabuleiro[5] == simboloComputador and tabuleiro[1] == simboloComputador and tabuleiro[7] == " ":
        return 7
    if tabuleiro[5] == " " and tabuleiro[1] != jog1 and tabuleiro[3] != jog1:
        return 5
    if tabuleiro[5] == simboloComputador and tabuleiro[1] == " " and tabuleiro[3] != jog1:
        return 1
    if tabuleiro[5] == simboloComputador and tabuleiro[1] == simboloComputador and tabuleiro[3] == " ":
        return 3
    if tabuleiro[5] == " " and tabuleiro[9] != jog1 and tabuleiro[3] != jog1:
        return 5
    if tabuleiro[5] == simboloComputador and tabuleiro[9] == " " and tabuleiro[3] != jog1:
        return 9
    if tabuleiro[5] == simboloComputador and tabuleiro[9] == simboloComputador and tabuleiro[3] == " ":
        return 3
    if tabuleiro[5] == " " and tabuleiro[7] != jog1 and tabuleiro[9] != jog1:
        return 5
    if tabuleiro[5] == simboloComputador and tabuleiro[7] == " " and tabuleiro[9] != jog1:
        return 7 
    if tabuleiro[5] == simboloComputador and tabuleiro[7] == simboloComputador and tabuleiro[9] == " ":
        return 9
    if tabuleiro[5] == " " and tabuleiro[4] != jog1 and tabuleiro[2] != jog1: # Iniciano estratégia de formar um triângulo com o centro e as bordas
        return 5
    if tabuleiro[5] == simboloComputador and tabuleiro[4] == " " and tabuleiro[2] != jog1:
        return 4
    if tabuleiro[5] == simboloComputador and tabuleiro[4] == simboloComputador and tabuleiro[2] == " ":
        return 2
    if tabuleiro[5] == " " and tabuleiro[6] != jog1 and tabuleiro[8] != jog1:
        return 5
    if tabuleiro[5] == simboloComputador and tabuleiro[6] == " " and tabuleiro[8] != jog1:
        return 6
    if tabuleiro[5] == simboloComputador and tabuleiro[6] == simboloComputador and tabuleiro[8] == " ":
        return 8
    if tabuleiro[5] == " " and tabuleiro[2] != jog1 and tabuleiro[6] != jog1:
        return 5
    if tabuleiro[5] == simboloComputador and tabuleiro[2] == " " and tabuleiro[6] != jog1:
        return 2
    if tabuleiro[5] == simboloComputador and tabuleiro[2] == simboloComputador and tabuleiro[6] == " ":
        return 6
    if tabuleiro[5] == " " and tabuleiro[4] != jog1 and tabuleiro[8] != jog1:
        return 5
    if tabuleiro[5] == simboloComputador and tabuleiro[4] == " " and tabuleiro[8] != jog1:
        return 4
    if tabuleiro[5] == simboloComputador and tabuleiro[4] == simboloComputador and tabuleiro[8] == " ":
        return 8
    if tabuleiro[1] == " " and tabuleiro[7] != jog1 and tabuleiro[3] != jog1: # Aplicando a estratégia para formar um triângulo com os cantos
        return 1
    if tabuleiro[1] == simboloComputador and tabuleiro[7] == " " and tabuleiro[3] != jog1:
        return 7 
    if tabuleiro[1] == simboloComputador and tabuleiro[7] == simboloComputador and tabuleiro[3] == " ":
        return 3
    if tabuleiro[9] == " " and tabuleiro[7] != jog1 and tabuleiro[3] != jog1:
        return 9
    if tabuleiro[9] == simboloComputador and tabuleiro[7] == " " and tabuleiro[3] != jog1:
        return 7 
    if tabuleiro[9] == simboloComputador and tabuleiro[7] == simboloComputador and tabuleiro[3] == " ":
        return 3
    if tabuleiro[7] == " " and tabuleiro[1] != jog1 and tabuleiro[9] != jog1:
        return 7
    if tabuleiro[7] == simboloComputador and tabuleiro[1] == " " and tabuleiro[9] != jog1:
        return 1
    if tabuleiro[7] == simboloComputador and tabuleiro[1] == simboloComputador and tabuleiro[9] == " ":
        return 9
    if tabuleiro[3] == " " and tabuleiro[1] != jog1 and tabuleiro[9] != jog1:
        return 3
    if tabuleiro[3] == simboloComputador and tabuleiro[1] == " " and tabuleiro[9] != jog1:
        return 1 
    if tabuleiro[3] == simboloComputador and tabuleiro[1] == simboloComputador and tabuleiro[9] == " ":
        return 9
    if tabuleiro[4] == " " and tabuleiro[1] != jog1 and tabuleiro[2] != jog1: # Dando inicio a estratégia com um canto e duas bordas
        return 4
    if tabuleiro[4] == simboloComputador and tabuleiro[1] == " " and tabuleiro[2] != jog1:
        return 1
    if tabuleiro[4] == simboloComputador and tabuleiro[1] == simboloComputador and tabuleiro[2] == " ":
        return 2
    if tabuleiro[4] == " " and tabuleiro[7] != jog1 and tabuleiro[8] != jog1:
        return 4
    if tabuleiro[4] == simboloComputador and tabuleiro[7] == " " and tabuleiro[8] != jog1:
        return 7
    if tabuleiro[4] == simboloComputador and tabuleiro[7] == simboloComputador and tabuleiro[8] == " ":
        return 8
    if tabuleiro[6] == " " and tabuleiro[8] != jog1 and tabuleiro[9] != jog1:
        return 6
    if tabuleiro[6] == simboloComputador and tabuleiro[8] == " " and tabuleiro[9] != jog1:
        return 8
    if tabuleiro[6] == simboloComputador and tabuleiro[8] == simboloComputador and tabuleiro[9] == " ":
        return 9
    if tabuleiro[6] == " " and tabuleiro[2] != jog1 and tabuleiro[3] != jog1:
        return 6
    if tabuleiro[6] == simboloComputador and tabuleiro[2] == " " and tabuleiro[3] != jog1:
        return 2
    if tabuleiro[6] == simboloComputador and tabuleiro[2] == simboloComputador and tabuleiro[3] == " ":
        return 3
    if tabuleiro[5] == " " and tabuleiro[1] == jog1 and tabuleiro[7] == jog1: # Tentando evitar estratégias semelhantes por parte do usuário
        return 5
    if tabuleiro[5] == jog1 and tabuleiro[1] == " " and tabuleiro[7] == jog1:
        return 1
    if tabuleiro[5] == jog1 and tabuleiro[1] == jog1 and tabuleiro[7] == " ":
        return 7
    if tabuleiro[5] == " " and tabuleiro[1] == jog1 and tabuleiro[3] == jog1:
        return 5
    if tabuleiro[5] == jog1 and tabuleiro[1] == " " and tabuleiro[3] == jog1:
        return 1
    if tabuleiro[5] == jog1 and tabuleiro[1] == jog1 and tabuleiro[3] == " ":
        return 3
    if tabuleiro[5] == " " and tabuleiro[9] == jog1 and tabuleiro[3] == jog1:
        return 5
    if tabuleiro[5] == jog1 and tabuleiro[9] == " " and tabuleiro[3] == jog1:
        return 9
    if tabuleiro[5] == jog1 and tabuleiro[9] == jog1 and tabuleiro[3] == " ":
        return 3
    if tabuleiro[5] == " " and tabuleiro[7] == jog1 and tabuleiro[9] == jog1:
        return 5
    if tabuleiro[5] == jog1 and tabuleiro[7] == " " and tabuleiro[9] == jog1:
        return 7 
    if tabuleiro[5] == jog1 and tabuleiro[7] == jog1 and tabuleiro[9] == " ":
        return 9
    if tabuleiro[5] == " " and tabuleiro[4] == jog1 and tabuleiro[2] == jog1:
        return 5
    if tabuleiro[5] == jog1 and tabuleiro[4] == " " and tabuleiro[2] == jog1:
        return 4
    if tabuleiro[5] == jog1 and tabuleiro[4] == jog1 and tabuleiro[2] == " ":
        return 2
    if tabuleiro[5] == " " and tabuleiro[6] == jog1 and tabuleiro[8] == jog1:
        return 5
    if tabuleiro[5] == jog1 and tabuleiro[6] == " " and tabuleiro[8] == jog1:
        return 6
    if tabuleiro[5] == jog1 and tabuleiro[6] == jog1 and tabuleiro[8] == " ":
        return 8
    if tabuleiro[5] == " " and tabuleiro[2] == jog1 and tabuleiro[6] == jog1:
        return 5
    if tabuleiro[5] == jog1 and tabuleiro[2] == " " and tabuleiro[6] == jog1:
        return 2
    if tabuleiro[5] == jog1 and tabuleiro[2] == jog1 and tabuleiro[6] == " ":
        return 6
    if tabuleiro[5] == " " and tabuleiro[4] == jog1 and tabuleiro[8] == jog1:
        return 5
    if tabuleiro[5] == jog1 and tabuleiro[4] == " " and tabuleiro[8] == jog1:
        return 4
    if tabuleiro[5] == jog1 and tabuleiro[4] == jog1 and tabuleiro[8] == " ":
        return 8
    if tabuleiro[1] == " " and tabuleiro[7] == jog1 and tabuleiro[3] == jog1:
        return 1
    if tabuleiro[1] == jog1 and tabuleiro[7] == " " and tabuleiro[3] == jog1:
        return 7 
    if tabuleiro[1] == jog1 and tabuleiro[7] == jog1 and tabuleiro[3] == " ":
        return 3
    if tabuleiro[9] == " " and tabuleiro[7] == jog1 and tabuleiro[3] == jog1:
        return 9
    if tabuleiro[9] == jog1 and tabuleiro[7] == " " and tabuleiro[3] == jog1:
        return 7 
    if tabuleiro[9] == jog1 and tabuleiro[7] == jog1 and tabuleiro[3] == " ":
        return 3
    if tabuleiro[7] == " " and tabuleiro[1] == jog1 and tabuleiro[9] == jog1:
        return 7
    if tabuleiro[7] == jog1 and tabuleiro[1] == " " and tabuleiro[9] == jog1:
        return 1
    if tabuleiro[7] == jog1 and tabuleiro[1] == jog1 and tabuleiro[9] == " ":
        return 9
    if tabuleiro[3] == " " and tabuleiro[1] == jog1 and tabuleiro[9] == jog1:
        return 3
    if tabuleiro[3] == jog1 and tabuleiro[1] == " " and tabuleiro[9] == jog1:
        return 1 
    if tabuleiro[3] == jog1 and tabuleiro[1] == jog1 and tabuleiro[9] == " ":
        return 9
    if tabuleiro[4] == " " and tabuleiro[1] == jog1 and tabuleiro[2] == jog1:
        return 4
    if tabuleiro[4] == jog1 and tabuleiro[1] == " " and tabuleiro[2] == jog1:
        return 1
    if tabuleiro[4] == jog1 and tabuleiro[1] == jog1 and tabuleiro[2] == " ":
        return 2
    if tabuleiro[4] == " " and tabuleiro[7] == jog1 and tabuleiro[8] == jog1:
        return 4
    if tabuleiro[4] == jog1 and tabuleiro[7] == " " and tabuleiro[8] == jog1:
        return 7
    if tabuleiro[4] == jog1 and tabuleiro[7] == jog1 and tabuleiro[8] == " ":
        return 8
    if tabuleiro[6] == " " and tabuleiro[8] == jog1 and tabuleiro[9] == jog1:
        return 6
    if tabuleiro[6] == jog1 and tabuleiro[8] == " " and tabuleiro[9] == jog1:
        return 8
    if tabuleiro[6] == jog1 and tabuleiro[8] == jog1 and tabuleiro[9] == " ":
        return 9
    if tabuleiro[6] == " " and tabuleiro[2] == jog1 and tabuleiro[3] == jog1:
        return 6
    if tabuleiro[6] == jog1 and tabuleiro[2] == " " and tabuleiro[3] == jog1:
        return 2
    if tabuleiro[6] == jog1 and tabuleiro[2] == jog1 and tabuleiro[3] == " ":
        return 3
    x = range(10)
    return x if tabuleiro[x] == " " else jogadaComputador(tabuleiro, simboloComputador)


def escolheSimbolo():
    """
    É responsável coletar o simbolo que o usuário deseja ser.
    Retorna "X", se ele colocar x no input, e de modo análogo com o "O".

    Caso o jogador não colocar nenhum desses símbolos reconhecíveis,
    a função irá avisar o erro e retornar a si mesma.
    """
    E = input(f"Você deseja ser X ou O ? ")
    if E == "X" or E == "x":
        return "X"
    elif E == "O" or E == "o":
        return "O"
    else:
        print(f"\nSímbolo inválido!\n")
        return escolheSimbolo()


def jogo(jog1, start, tabuleiro):
    """
    É a função responsável por controlar o jogo, alternando entre jogadores
    recursivamente.

    - jog1 : é o símbolo que o usuário escolheu;
    - start : é o valor de partida que determina quem vai jogar;
    - tabuleiro : lista de tamanho 10 representando o tabuleiro.
    """
    PCsimbolo = "X" if jog1 == "O" else "O"
    verificaSeGanhou(tabuleiro, jog1, PCsimbolo)
    if start == 0:
        tabuleiro[jogadaComputador(tabuleiro, PCsimbolo)] = PCsimbolo
        imprimeTabuleiro(tabuleiro)
        verificaSeGanhou(tabuleiro, jog1, PCsimbolo)
        jogo(jog1, start+1, tabuleiro)
    elif start == 1:
        tabuleiro[jogador(tabuleiro)] = jog1
        verificaSeGanhou(tabuleiro, jog1, PCsimbolo)
        tabuleiro[jogadaComputador(tabuleiro, PCsimbolo)] = PCsimbolo
        verificaSeGanhou(tabuleiro, jog1, PCsimbolo)
        imprimeTabuleiro(tabuleiro)
        jogo(jog1, start, tabuleiro)


def main():
    """
    É uma função main genérica.
    """
    limpaTela()
    print(f"Olá seja Bem-vindo ao jogo da velha\n")
    tabuleiro = [" "]*10
    jog1 = escolheSimbolo()
    start = quemComeca(tabuleiro)
    jogo(jog1, start, tabuleiro[:])
    print(getNome()) # Emily W. Gonçalves
    print(getMatricula()) # 2022100287


################################
## NÃO ALTERE O CÓDIGO ABAIXO ##
################################
if __name__ == "__main__":
    main()
