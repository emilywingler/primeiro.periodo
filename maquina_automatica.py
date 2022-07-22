from os import system, name
# Nome: Emily Wingler Gonçalves
# Matrícula: 2022100287

def limpaTela():
    """
    É a função responsável por limpar o terminal.
    """
    if name == 'nt':  # Windows
        system('cls')  
    else:  # Linux ou outro SO
        system('clear') 


def boas_vindas():
    """
    É a função que dará início à experiência do usuário ao exibir uma mensagem de boas-vindas  
    """
    amarelo ="\033[1;33m"      
    violeta ="\033[1;35m"     
    azul ="\033[1;36m"
    RST = "\033[0m"
    print(f"{violeta}Olá!\n\n{azul}Bem-vindo ao parque Magic Circus, onde o espetáculo é você!\n")
    print(f"{violeta}Para adicionar um toque de magia na sua jornada, adquira alguns dos nossos produtos!")
    enter = input(f"\n{amarelo}**Aperte Enter para continuar...{RST}")


def ehindisponível(P1, valor, num1):
    """
    É uma função para configurar a impressão da Tela de Entrada
    a partir do estoque. Caso o estoque seja igual à zero, a função irá retornar 'indisponível'
    no lugar do preço.
    - P1 = estoque analisado;
    - valor = preço do produto;
    - num1 = a quantidade de vezes que o espaço deve ser multiplicado
    para formar a imagem.
    """
    return " "*num1 + "R$ " + valor + " **" if P1 > 0 else " "*(num1-4) + "Indisponível **"


def Imprimemenu(P1, P2, P3, P4, P5):
    """
    É uma função responsável por imprimir a 
    tabela de valores para o usuário.
    - P1 = estoque do produto 'Cartas de Tarot';
    - P2 = estoque do produto 'Mini Bola de cristal';
    - P3 = estoque do produto 'incensos';
    - P4 = estoque do produto 'Pozinho mágico';
    - P5 = estoque do produto 'Varinha para iniciantes'.
    """
    violeta = "\033[1;35m"
    RST = "\033[0m"
    print(violeta)
    print("*"*62)
    print("*"*25 + " FAST MÁGIC " + "*"*25)
    print("*"*62)
    print("** 1. Cartas de Tarot" + ehindisponível(P1, "12,00", 30))
    print("** 2. Mini Bola de Cristal" + ehindisponível(P2, "30,00", 25))
    print("** 3. Incensos (3 unidades)" + ehindisponível(P3, "05,20", 24))
    print("** 4. Pozinho mágico instântaneo 5g" + ehindisponível(P4, "25,00", 16))
    print("** 5. Varinha para iniciantes Turbo 5k" + ehindisponível(P5, "50,00", 13))
    print("*"*62)
    print("*"*23 + " OUTRAS FUNÇÕES " + "*"*23)
    print("*"*62)
    print("** 6. Informações Internas" + " "*34 + "**")
    print("** 7. Finalizar" + " "*45 + "**")
    print("*"*62)
    print("*"*62)
    print(RST)


def leValor(funcaoconversao, msg=" "):
    """
    É responsável por tentar converter o valor que o usuário
    digita, de acordo com  necessidade. Caso ela não consiga,
    irá retornar recursivamente o input, até o usuário digitar um valor que possa ser convertido.
    - funcaoconversao = tipo da conversão que será realizada. Ex.: int,float, etc.
    - msg = mensagem que virá no input inicial.
    """
    vermelho = "\033[1;31m"   
    azul ="\033[1;36m"
    try:
        return funcaoconversao(input(msg))
    except:
        print(f"\n{vermelho}ERRO: A máquina não reconhece este comando:\n")
        return leValor(funcaoconversao, f"{azul}** Por favor, tente novamente:")


def confirmacoes(i=0):
    """
    - i = parâmetro indicador, irá determinar que ação a função realizará
    Se i = 0 será uma função que irá retornar 'False', caso o usuário não queira realizar 
    uma nova compra, e digite 'n' ou 'N'. Retornará 'True', caso o usuário 
    queira comprar novamente e digite 's' ou 'S'.
    Se i != 0 será uma função que irá retornar 'False', caso o usuário não queira realizar 
    a compra do produto, e digite 'n' ou 'N'. Retornará 'True', caso o usuário 
    confirme a compra e digite 's' ou 'S'
    """
    vermelho = "\033[1;31m" 
    azul = "\033[1;36m"
    RST = "\033[0m"
    if i == 0:
        _=input(f"{azul}\n** Deseja aumentar ainda mais o seu arsenal mágico? (S,N): ")
        if _ != "s" and _ != "S" and _ != "N" and _ != "n":
            print(f"\n{vermelho}ERRO: A máquina não reconhece este comando{RST}")
            confirmacoes()
        return False if _ == "n" or _ == "N" else True
    if i != 0:
        _=input(f"{azul}\n** Tem certeza que quer realizar essa compra? (S,N): ")
        if _ != "s" and _ != "S" and _ != "N" and _ != "n":
            print(f"\n{vermelho}ERRO: A máquina não reconhece este comando{RST}")
            confirmacoes(i)
        return False if _ == "n" or _ == "N" else True


def pagar(valor):
    """
    É uma função que irá pedir que o usuário pague pelo produto, de forma que: 
    o valor precisa ser igual ou maior do que o preço do produto. Caso essa
    condição não seja atendida, a função continuará retornando o input para que o
    usuário continue digitando. Quando a condição ser atendida, ele irá retornar o
    valor total que o usuário depositou na máquina.
    - valor = preço do produto em questão
    """
    azul = "\033[1;36m"
    d = leValor(float, f"{azul}**Insira o dinheiro na máquina: ")
    if valor == d:  
        return round(d, 2)
    elif d < 0:
        pagar(valor)
    elif d < valor:
        return d + pagar(round(valor - d,2))
    else:
        return round(d, 2)


def imprimeTroco(v, m):
    """
    É uma função que atua em conjunto com a geratroco. Ela é responsável 
    por imprimir a maior quantidadede notas possíveis (recursivamente), 
    de um valor específico, a partir de um troco pré- determinado. Quando
    isso não é mais uma possibilidade (o valor do troco é menor que o valor da nota)
    a função retorna o resto do troco.
    - v = troco
    - m = valor da nota que será impressa
    """   
    violeta = "\033[1;35m"     
    v = round(v, 2)
    if v >= 1:
        if v >= m:
            print(f"{violeta}R$ {m},00")
            return imprimeTroco(v-m, m)
        else:
            return v 
    else:
        if v >= m:
            print(f"{violeta}R$ 0,{round(int(m * 100), 2):02d}")
            return imprimeTroco(v-m, m)
        else:
            return v


def geraTroco(troco, total):
    """
    É uma função que é construída a partir da imprimeTroco. Ela é 
    responsável por três fucnionalidades: imprimir o valor que o usuário 
    depositou, quanto que ele precisa receber de troco, e as notas referentes a
    esse valor, da maior nota possível até a menor. Assim, começando
    com o valor original do troco, e as notas de 100, depois com o resto disso
    em notas de 50, e do mesmo modo sucesivamente com os outros valores de notas
    (e moedas), até todo o dinheiro ser devolvido ao cliente.
    - total = valor total que o usuário depositou na máquina
    - troco = total - valor do produto
    """
    amarelo = "\033[1;33m"      
    troco = round(troco, 2)
    print(f"\n{amarelo}Valor pago R$ {total:.2f}")
    print(f"O seu troco é de R$ {troco:.2f}\n")
    v = imprimeTroco(troco, 100)
    v = imprimeTroco(v, 50)
    v = imprimeTroco(v, 20)
    v = imprimeTroco(v, 10)
    v = imprimeTroco(v, 5)
    v = imprimeTroco(v, 2)
    v = imprimeTroco(v, 1)
    v = round(imprimeTroco(v, 0.50), 2)
    v = round(imprimeTroco(v, 0.25), 2)
    v = round(imprimeTroco(v, 0.10), 2)
    v = round(imprimeTroco(v, 0.05), 2)
    v = round(imprimeTroco(v, 0.01), 2)


def Imprime_info(P1, P2, P3, P4, P5, F, i=0):
    """
    É a função responsável por imprimir as informações internas da máquina.
    - P1 = estoque do produto 'Cartas de Tarot';
    - P2 = estoque do produto 'Mini Bola de cristal';
    - P3 = estoque do produto 'incensos';
    - P4 = estoque do produto 'Pozinho mágico';
    - P5 = estoque do produto 'Varinha para iniciantes'.
    - F = faturamento da máquina (valor total arrecadado pela venda dos produtos)
    - i = parâmetro criado para exibir, ou não, a mensagem final para o usuário (indicador)
    """
    violeta = "\033[1;35m"
    azul ="\033[1;36m"
    RST = "\033[0m"
    print(violeta)
    print("*"*62)
    print("*"*19 + " INFORMAÇÕES  INTERNAS " + "*"*20)
    print("*"*26 + " estoque " + "*"*27)
    print("*"*62) 
    print(f"** Cartas de Tarot: {P1} " + (f"unidades"+" "*30 if P1 != 1 else "unidade"+" "*31) + "**") 
    print(f"** Mini Bola de Cristal: {P2} " + (f"unidades"+" "*25 if P2 != 1 else "unidade"+" "*26) + "**") 
    print(f"** Incensos (3 unidades): {P3} " + (f"unidades"+" "*24 if P3 != 1 else "unidade"+" "*25) + "**") 
    print(f"** Pozinho mágico instântaneo 5g: {P4} " + (f"unidades"+" "*16 if P4 != 1 else "unidade"+" "*17) + "**") 
    print(f"** Varinha para iniciantes Turbo 5k: {P5} "+ (f"unidades"+" "*13 if P5 != 1 else "unidade"+" "*14) + "**")
    print("*"*62)  # Logo acima,temos a formatação para alterar 'unidade' para plural ou singular 
    print("*"*62)  # dependendo da quantidade de estoque. Além de organizar a parte estética da tabela
    print(f"** Atualmente o faturamento desta máquina é de: " + f"R$ {F:.2f}" + (" "*3 if F>=100 else " "*4 if F >= 10 else " "*5) + "**" )
    print("*"*62)
    print("*"*62)
    print(RST)
    if i == 0:
        print(f"\n{azul}Que você nunca perca o seu pozinho mágico!\nBons Feitiços e até a próxima!{RST}\n")


def maquina(P1, P2, P3, P4, P5, F):
    """
    É a função responsável por controlar as funcionalidades da máquina
    - P1 = estoque do produto 'Cartas de Tarot';
    - P2 = estoque do produto 'Mini Bola de cristal';
    - P3 = estoque do produto 'incensos';
    - P4 = estoque do produto 'Pozinho mágico';
    - P5 = estoque do produto 'Varinha para iniciantes'.
    - F = faturamento da máquina (valor total arrecadado pela venda dos produtos)
    """
    vermelho = "\033[1;31m"
    amarelo ="\033[1;33m"      
    violeta ="\033[1;35m"     
    azul ="\033[1;36m"
    RST = "\033[0m"
    limpaTela()
    Imprimemenu(P1, P2, P3, P4, P5)  # Imprime a tabela de preços para o usuário
    opcao = leValor(int, f"{azul}** Escolha uma opção: ")  # Escolha da funcionalidade
    print(RST)
    if P1 + P2 + P3 + P4 + P5 == 0:  # Para otimizar o tempo do usuário caso os estoques estejam vazios.
        print(f"\n{vermelho}Infelizmente essa máquina não possui estoque!\nProcure a máquina mais próxima para abastecer seu arsenal mágico{RST}")
        Imprime_info(P1, P2, P3, P4, P5, F)
        exit()
    if opcao == 1:
        print(f"{amarelo}Hmmmm...Você escolheu a opção 'Cartas de Tarot'.\n\n{violeta}Significa que busca por respostas!")
        print(f"\n{amarelo}Valor do produto: R$12,00\n")
        valor = 12  # Preço do produto
        if P1 <= 0:  # Caso o estoque do produto tenha acabado, o programa avisa o usuário e impede a compra
            print(f"{vermelho}Desculpa, mas esse produto está indisponível{azul}") 
            enter = input(f"\n{amarelo}**Aperte Enter para continuar...{RST}")
            maquina(P1, P2, P3, P4, P5, F)
        elif confirmacoes(1) == False:
            maquina(P1, P2, P3, P4, P5, F)
        else:
            print(f"{violeta}\n**Hora de Pagar**\n{RST}")
            total = pagar(valor)
            troco = total - valor
            if troco >= 99000:  # Caso os pagamentos sejam em valores muito altos (além da capacidade de troco)
                print(f"{vermelho}Desculpa, mas a máquina não tem capacidade de fornecer esse troco.{RST}\n")
                enter = input(f"{amarelo}Escolha novamente!\nAperte Enter para continuar...")
                maquina(P1, P2, P3, P4, P5, F)
            F += valor  # Quando a compra é possível, o valor é adicionado ao faturamento geral da máquina
            P1 -= 1  # Diminui o estoque do produto após a compra 
            geraTroco(troco, total)
            if confirmacoes() == False:
                Imprime_info(P1, P2, P3, P4, P5, F)
                exit()
            else:
                maquina(P1, P2, P3, P4, P5, F)
    elif opcao == 2:
        print(f"{amarelo}Você escolheu a opção 'Mini Bola de Cristal'.\n\n{violeta}O que será que te aguarda no futuro?")
        print(f"\n{amarelo}Valor do produto: R$30,00{RST}\n")
        valor = 30  # Preço do produto
        if P2 <= 0:
            print(f"{vermelho}Desculpa, mas esse produto está indisponível{RST}")
            enter = input(f"\n{amarelo}**Aperte Enter para continuar...{RST}")
            maquina(P1, P2, P3, P4, P5, F)
        elif confirmacoes(1) == False:
            maquina(P1, P2, P3, P4, P5, F)
        else:
            print(f"{violeta}\n**Hora de Pagar**\n{RST}")
            total = pagar(valor)
            troco = total - valor
            if troco >= 99000:
                print(f"{vermelho}Desculpa, mas a máquina não tem capacidade de fornecer esse troco.{RST}\n")
                enter = input(f"{amarelo}Escolha novamente!\nAperte Enter para continuar...")
                maquina(P1, P2, P3, P4, P5, F)
            F += valor
            P2 -= 1
            geraTroco(troco, total)
            if confirmacoes() == False:
                Imprime_info(P1, P2, P3, P4, P5, F)
                exit()
            else:
                maquina(P1, P2, P3, P4, P5, F)
    elif opcao == 3:
        print(f"{amarelo}Você escolheu a opção 'Incensos (3 unidades)'.\n\n{violeta}Para limpar a energia qualquer ambiente...")
        print(f"\n{amarelo}Valor do produto: R$05,20\n")
        valor = 5.20  # Preço do produto
        if P3 <= 0:
            print(f"{vermelho}Desculpa, mas esse produto está indisponível{RST}")
            enter = input(f"\n{amarelo}**Aperte Enter para continuar...{RST}")
            maquina(P1, P2, P3, P4, P5, F)
        elif confirmacoes(1) == False:
            maquina(P1, P2, P3, P4, P5, F)
        else:
            print(f"{violeta}\n**Hora de Pagar**\n{RST}")
            total = pagar(valor)
            troco = total - valor
            if troco >= 99000:
                print(f"{vermelho}Desculpa, mas a máquina não tem capacidade de fornecer esse troco.{RST}\n")
                enter = input(f"{amarelo}Escolha novamente!\nAperte Enter para continuar...")
                maquina(P1, P2, P3, P4, P5, F)
            F += valor
            P3 -= 1
            geraTroco(troco, total)
            if confirmacoes() == False:
                Imprime_info(P1, P2, P3, P4, P5, F)
                exit()
            else:
                maquina(P1, P2, P3, P4, P5, F)
    elif opcao == 4:
        print(f"{amarelo}Você escolheu a opção 'Pozinho mágico instântaneo 5g'.\n\n{violeta}Use mas não abuse!!")
        print(f"\n{amarelo}Valor do produto: R$25,00{RST}\n")
        valor = 25  # Preço do produto
        if P4 <= 0:
            print(f"{vermelho}Desculpa, mas esse produto está indisponível{RST}")
            enter = input(f"\n{amarelo}**Aperte Enter para continuar...{RST}")
            maquina(P1, P2, P3, P4, P5, F)
        elif confirmacoes(1) == False:
            maquina(P1, P2, P3, P4, P5, F)
        else:
            print(f"{violeta}\n**Hora de Pagar**\n{RST}")
            total = pagar(valor)
            troco = total - valor
            if troco >= 99000:
                print(f"{vermelho}Desculpa, mas a máquina não tem capacidade de fornecer esse troco.{RST}\n")
                enter = input(f"{amarelo}Escolha novamente!\nAperte Enter para continuar...")
                maquina(P1, P2, P3, P4, P5, F)
            F += valor
            P4 -= 1
            geraTroco(troco, total)
            if confirmacoes() == False:
                Imprime_info(P1, P2, P3, P4, P5, F)
                exit()
            else:
                maquina(P1, P2, P3, P4, P5, F)
    elif opcao == 5:
        print(f"{amarelo}Você escolheu a opção 'Varinha para iniciantes Turbo 5k'.\n\n{violeta}Irá tornar a sua experiência mais interativa aqui no parque")
        print(f"\n{amarelo}Valor do produto: R$50,00{RST}\n")
        valor = 50 # Preço do produto
        if P5 <= 0: # Condicional para produto sem estpque
            print(f"{vermelho}Desculpa, mas esse produto está indisponível{RST}")
            enter = input(f"\n{amarelo}**Aperte Enter para continuar...{RST}")
            maquina(P1, P2, P3, P4, P5, F)
        elif confirmacoes(1) == False:
            maquina(P1, P2, P3, P4, P5, F)
        else:
            print(f"{violeta}\n**Hora de Pagar**\n{RST}")
            total = pagar(valor)
            troco = total - valor
            if troco >= 99000:
                print(f"{vermelho}Desculpa, mas a máquina não tem capacidade de fornecer esse troco.{RST}\n")
                enter = input(f"{amarelo}Escolha novamente!\nAperte Enter para continuar...")
                maquina(P1, P2, P3, P4, P5, F)
            F += valor
            P5 -= 1
            geraTroco(troco, total)
            if confirmacoes() == False:
                Imprime_info(P1, P2, P3, P4, P5, F)
                exit()
            else:
                maquina(P1, P2, P3, P4, P5, F)
    elif opcao == 6:
        Imprime_info(P1, P2, P3, P4, P5, F, 1)  # Aqui a mensagem final não pode ser exibida, portanto o parâmetro i != 0;
        enter = input(f"\n{amarelo}**Aperte Enter para continuar...{RST}")
        maquina(P1, P2, P3, P4, P5, F)  
    elif opcao == 7:
        Imprime_info(P1, P2, P3, P4, P5, F)
        exit()
    else:
        print(f"{vermelho}Opção inválida") # Caso o usuário digite um valor acima ou abaixo, do esperado
        enter = input(f"\n{amarelo}**Aperte Enter para continuar...{RST}")
        maquina(P1, P2, P3, P4, P5, F)


def main():
    """
    É uma função main tradicional, reponsável por todo o sistema
    """
    limpaTela()
    boas_vindas()
    limpaTela()
    maquina(5, 5, 5, 5, 5, 0)
    limpaTela()

main()

