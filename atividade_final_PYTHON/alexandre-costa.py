"""
1:Alisson:GOLEIRO
2:Danilo:DEFESA
3:Thiago Silva:DEFESA
4:Marquinhos:DEFESA
5:Casemiro:MEIO-CAMPO
6:Alex Sandro:DEFESA
7:Lucas Paquetá:MEIO-CAMPO
8:Fred:MEIO-CAMPO
9:Richarlison:ATACANTE
10:Neymar:ATACANTE
11:Raphinha:ATACANTE
12:Weverton:GOLEIRO
13:Dani Alves:DEFESA
14:Éder Millitão:DEFESA
15:Fabinho:MEIO-CAMPO
16:Alex Telle:DEFESA
17:Bruno Guimarães:MEIO-CAMPO
18:Gabriel Jesus:ATACANTE
19:Antony:ATACANTE
20:Vinicius Junior:ATACANTE
21:Rodrygo:ATACANTE
22:Éverton Ribeiro:MEIO-CAMPO
23:Ederson:GOLEIRO
24:Bremer:DEFESA
25:Pedro:ATACANTE
26:Gabriel Martinelli:ATACANTE
"""

atk_reserva = []
dfs_reserva = []
meio_reserva = []
gol_reserva = []
lst_reserva = [atk_reserva,dfs_reserva,meio_reserva,gol_reserva]
lst_jogadores = []
lst_ataque = []
lst_meio = []
lst_defesa = []
lst_goleiro = []
lst_escalados = [lst_defesa,lst_goleiro,lst_ataque, lst_meio]

class Jogador:
    def __init__(self, nome, numero, posicao):
        self.__numero = numero
        self.__nome_jogador = nome
        self.__posicao = posicao # GOLEIRO ou DEFESA ou MEIO-CAMPO ou ATECANTE
        self.__situacao = "NORMAL"  # ou "EXPULSO"
        self.__participou_partida = False # ou True
        
    def __str__(self) :
        return f"{self.__nome_jogador} : {self.__numero} : {self.__posicao}"

    def __repr__(self):
        return f"{self.__nome_jogador} : {self.__numero} : {self.__posicao}"

    def getNum(self):
        return f"{self.__numero}"
    
    def getPos(self):
        return f"{self.__posicao}"
    
    def getName(self):
        return f"{self.__nome_jogador}"
    
    def getpart(self, x):
        self.__participou_partida = x
    
    def getStatus(self, y):
        self.__situacao = y
    
    def setStatus(self):
        return f"{self.__situacao}"
    
    


# Opção 1: Ler de um arquivo texto todos os jogadores
#         escalados para a copa e armazenar em uma
#         lista (lst_jogadores)
#         Cada Elemento da lista será uma instância
#             da classe Jogador.
def acesso():   
    arquivo = open("convocados.txt", "r")
    for i in arquivo:
        if i == '26:Gabriel Martinelli:ATACANTE':
            numero, nome, posicao = i[:].split(':')
            jogador = (Jogador(nome,numero,posicao))
            lst_jogadores.append(jogador)
        else:
            numero, nome, posicao = i[:].split(':')
            posicao = posicao[:-1]
            jogador = (Jogador(nome,numero,posicao))
            lst_jogadores.append(jogador)
    for i in (lst_jogadores):
        print(i)
        

# Opção 2: Você deverá escalar 11 dos jogadores para
#         iniciar a partida.
#         Os Jogadores escalados para a partida ficam
#             em uma lista (lst_escalados)
#             Alterar o atributo 'participou_partida'
#                 para True
#         Os jogadores que não forem escalados para
#             iniciar a partida ficam em uma outra
#             lista (lst_reserva)
def escalacao():
    while True:
        num = input("Digite o número da camisa do jogador => ")
        if not num:
            for i in lst_jogadores:
                if (i.getPos() == 'ATACANTE'):
                    if i not in lst_ataque:
                        atk_reserva.append(i)
                        
                if (i.getPos() == 'DEFESA'):
                    if i not in lst_defesa:
                        dfs_reserva.append(i)
                        
                if (i.getPos() == 'MEIO-CAMPO'): 
                    if i not in lst_meio:
                        meio_reserva.append(i)
                        
                if (i.getPos() == 'GOLEIRO'):
                    if i not in lst_goleiro:
                        gol_reserva.append(i)
            break
                        
        for jogador in lst_jogadores:
            j = 0
            if jogador.getNum() == num:
                if jogador not in lst_escalados:
                    
                    if jogador.getPos() == 'GOLEIRO':
                        if jogador in lst_goleiro:
                            print("Jogador já está na lista\n")
                        
                        else:
                            if len(lst_goleiro) == 1:
                                print("Máximo de goleiros atingido\n")
                            else:
                                jogador.getpart(True)
                                print(f'GOLEIRO {jogador.getName()} ADICIONADO\n')
                                lst_goleiro.append(jogador)

                    if jogador.getPos() == 'ATACANTE':
                        if jogador in lst_ataque:
                            print("Jogador já está na lista\n")        
                        else:
                            if len(lst_ataque) == 4:
                                print("Máximo de atacantes atingido\n")
                            else:
                                jogador.getpart(True)
                                print(f'ATACANTE {jogador.getName()} ADICIONADO\n')
                                lst_ataque.append(jogador)
                    
                    if jogador.getPos() == 'DEFESA':
                        if jogador in lst_defesa:
                            print("Jogador já está na lista\n")
                        
                        else:    
                            if len(lst_defesa) == 3:
                                print("Máximo de DEFESA atingido\n")
                            else:                    
                                jogador.getpart(True)
                                print(f'DEFESA {jogador.getName()} ADICIONADO\n')
                                lst_defesa.append(jogador)
                        
                    if jogador.getPos() == 'MEIO-CAMPO':
                        if jogador in lst_meio:
                            print("Jogador já está na lista\n")
                        else:
                            if len(lst_meio) == 3:
                                print("Máximo de MEIO-CAMPOS atingido\n")
                            else:
                                jogador.getpart(True)
                                print(f'MEIO-CAMPO {jogador.getName()} ADICIONADO\n')   
                                lst_meio.append(jogador)
 
#Opção 3: Você poderá realizar a substituição de um
 #       jogador por outro.
  #      Quando isso acontecer o jogador vai para
   #         a lista de Reserva e o outro para a
    #        lista Escalados.                                                             
def pega_lista(lista, lista_reserva):
    while True:
        camisa_num = input("Digite o número da camisa do jogador a ser substituido => ")
        if not camisa_num:
            break
        for i, v in enumerate(lista):
            if v.getNum() == camisa_num:
                print(f'JOGADOR {v.getName()} REMOVIDO\n')
                v.getpart(False)
                del lista[i]
                lista_reserva.append(v)
            if camisa_num != v.getNum():
                print('Jogador não está na lista\n')
                break
            novo_num = input("Digite o número da camisa do novo jogador => ")
            for i, n in enumerate(lista_reserva):
                try:
                    if n.getNum() == novo_num:
                        n.getpart(True)
                        print(f'JOGADOR {n.getName()} ADICIONADO\n')
                        lista.append(n)
                        del lista_reserva[i]
                except:
                    pass
          
def substituicao():
    posit = input(
    """Qual a posição do jogador que você deseja substituir
        1 - GOLEIRO
        2 - ATACANTE
        3 - DEFESA
        4 - MEIO-CAMPO
        => """)
    if posit == '1':
        pega_lista(lst_goleiro, gol_reserva)
    if posit == '2':
        pega_lista(lst_ataque,atk_reserva)
    if posit == '3':
        pega_lista(lst_defesa,dfs_reserva)
    if posit == '4':
        pega_lista(lst_meio,meio_reserva)
        
        
#Opção 4: Caso haja alguma expulsão, o jogador sai
 #       da lista de Escalados e vai para a lista
  #      Reserva.
def expulsa():
    posit = input(
    """Qual a posição do jogador que você deseja expulsar:
        1 - GOLEIRO
        2 - ATACANTE
        3 - DEFESA
        4 - MEIO-CAMPO
        => """)
    if posit == '1':
        expulsao(lst_goleiro)
    if posit == '2':
        expulsao(lst_ataque)
    if posit == '3':
        expulsao(lst_defesa)
    if posit == '4':
        expulsao(lst_meio)
        
def expulsao(lista):
    camisa_num = input("Digite o número da camisa do jogador a ser substituido => ")
    if not camisa_num:
        pass
    else:
        for i, v in enumerate(lista):
            if v.getNum() == camisa_num:
                print(f'JOGADOR {v.getName()} EXPULSO\n')
                v.getStatus('EXPULSO')
                del lista[i]
            if camisa_num != v.getNum():
                print('Jogador não está na lista\n')
                break
            
#Opção 5: Mostrar a escalação de todos jogadores que
 #       participaram do jogo, inclusive as substituições
  #      e expulsões.
   #     Salve esses dados em um arquivo (todosjogadores.txt)
def printa():
    arquivo = open("todosjogadores.txt", "a")
    for i in lst_escalados:
        if type (i) == list:
            for j in i: 
                print([j])               
                arquivo.write(f"{j.getNum()} : {j.getName()} : {j.getPos()}\n")                       
while  True:
    print("""
    MENU
    ======
    1- Ler arquivo de jogadores
    2- Escalar time
    3- Realizar Substiuição
    4- Expulsão
    5- Imprimir escalação
    Escolha:
    """)   
    escolha = input("Digite sua escolha => ")
    if escolha == '1':
        acesso()
    if escolha == '2':    
        escalacao()
    if escolha == '3':
        substituicao()
    if escolha == '4':
        expulsa()
    if escolha == '5':
        printa()
    if not escolha:
        print('Saindo...')
        exit()