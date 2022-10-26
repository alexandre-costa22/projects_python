#
# Tarefa 1
# Competências avaliadas:
# - Saber interpretar o que foi solicitado
# - Desenvolver uma solução viável para o problema
# - Saber utilizar classes e objetos

lista_visitante=[]
lista_profissionais=[]
lista_visitas = []
lista_erro_prof = []
lista_erro_vis = []

class Profissional:
    def __init__(self, nome, especialidade, sala):
        self.__nome = nome
        self.__especialidade = especialidade
        self.__sala = sala 

    def getNome_prof(self):
        return f"{self.__nome}"
    
    def __str__(self):
        return f"Nome: {self.__nome}  Especialidade: {self.__especialidade}  Sala: {self.__sala}"
    
    def __repr__(self):
        return f"Nome: {self.__nome}  Especialidade: {self.__especialidade}  Sala: {self.__sala}"


class Visitante:
    def __init__(self, nome, documento):
        self.__nome = nome
        self.__documento = documento
    
    def getNome_vis(self):
        return f"{self.__nome}"

    def __str__(self):
        return f"Nome: {self.__nome}  Documento: {self.__documento}"
    
    def __repr__(self):
        return f"Nome: {self.__nome}  Documento: {self.__documento}"

class Visita:
    def __init__(self, visitante, profissional, data_visita):
        self.visitante = visitante
        self.profissional = profissional
        self.data_visita = data_visita

    def __str__(self):
        return f"Visitante: {self.visitante} Profissional: {self.profissional} Data: {self.data_visita}"

def profissa():
    doc_profissa = input("Digite o nome do profissional => ")
    for profissa in lista_profissionais:
        if  doc_profissa == profissa.getNome_prof():
            return profissa
    return f"Profissional não encontrado"

def visitante_cadastro():
    nome = input("Digite o nome do visitante => ")
    while True:
        try:
            documento = int(input("Digite o número do documento => "))
            break
        except:
            print("Insira um valor válido")
    visitante = Visitante(nome,documento)
    lista_visitante.append(visitante)
    
def cadastro_profissa():
    nome = (input("Digite o nome do profissional => "))
    especialidade = input("Digite sua especialidade => ")
    while True:
        try:
            sala = int(input("Digite sua sala => "))
            break
        except:
            print("Digite um valor válido")
    profissional = Profissional(nome,especialidade,sala)
    lista_profissionais.append(profissional)
    print(lista_profissionais)
    

def cadastro_visita():
    for v in lista_visitante:
        print(v)
    visita = input("Digite o nome do visitante cadastrado => ")
    for i in lista_visitante:
        if visita == i.getNome_vis():
            lista_erro_vis.append(i)
    if len(lista_erro_vis) != 0:
        for f in lista_profissionais:
            print(f)   
        prof = input("Digite o nome do profissional => ")
        for p in lista_profissionais:
            if p.getNome_prof() == prof:
                lista_erro_prof.append(p)
        if len(lista_erro_prof) != 0:
            data = input("Data da visita => ")
            visita = Visita(visita,prof,data)
            lista_visitas.append(visita)
            print("Cadastro realizado")
            del lista_erro_prof[:]
            del lista_erro_vis [:]
        else:
            print("Profissional não encontrado")          
    else:
        print("Visitante não encontrado")

while True:
    print("""
    ======================
    MENU
    ======================
    1- Cadastrar Profissional
    2- Localizar Profissional
    3- Cadastrar Visitante
    4- Registrar Visita
    5- Relatório de Conferência"""
    )
    escolha = input("Escolha =>" )

    if escolha == '1':
        cadastro_profissa()
                    
    if escolha == '2':
        print(profissa())

    if escolha == '3':
        visitante_cadastro()

    if escolha == '4':
        cadastro_visita()

    if escolha == '5':
        for i in lista_visitas:
            print(i)
        




