#PROGRAMAÇAO ORIENTADA A OBJETOS (POO)

#########LINGUAGENS
#baixo nivel é linguagem decimal (010111010) de maquina
#linear é a linguagem q n pode ser modificada (ainda na linguagem de máquina)
#estrutural usa algoritmos e linguagem humana mas n era interativa (entre coisas)
#programação orientada a objeto é transformar algo físico em computacional (lógico)



# classes sao estruturas de dados q possuem atributos e metodos (representaçao computacional)----- OBJETOS
#atributo sao caracteristicas do objeto trabalhado em questao q sao especificados posteriormente ----- VARIAVEIS
#metodo sao as funçoes q ele vai executar/já executa ----- FUNÇOES
#classes podem ser iguais mas com variaveis e metodos diferentes
#classe tem q ta com primeira letra maiuscula (ex.:CarroDrive) pascal case
#instancias


#carro (classe)

# ATRIBUTO -> VARIAVEL
# modelo -> ferrari
# ano -> 2020
# estado -> seminovo
# ^^^^^^Variaveis^^^^^^

# acelerar, frear, buzinar
# ^^^^^^Metodos^^^^^^
 
#------------------------------------------
#def é para definir funçoes
#__init__ 'dois underlines' inicializa
#self faz referencia ao proprio objeto em questao
#def _init_(self, cor, marca, volume)
'''
class ControleRemoto:    #AQUI ESTÁ FAZENDO AS DECLARAÇÕES
    def __init__(self, cor, marca, volume):
        self.cor=cor
        self.marca=marca
        self.volume=volume
        
controle_remoto = ControleRemoto('preto','LG', 10)
print(controle_remoto.cor)
        
#
#
#

class Carro(object):
    estado='novo'
    
fusca=Carro()
fusca.estado='novo'

ferrari=Carro()
ferrari.estado='usado'

print (fusca.estado)
print (ferrari.estado)
print(type(fusca)) diz se é string, int..
print(type(ferrari))
-----------------------------------  QUESTOES PARA PRATICAR
'''
########1
class Pessoa:             #classe
    def __init__(self, nome):
        self.nome=nome
        
p1=Pessoa('Ana') #o self q é o p1 da classe pessoa atribui o nome dos parentesis para si
p2=Pessoa('Sofia')  #objetos

print (p1.nome, p2.nome)

########2
class Animal:
    def __init__(self, tipo):
        self.tipo=tipo
        
bicho1=Animal('gato')
bicho2=Animal('cachorro')

print (bicho1.tipo, bicho2.tipo)

########3,4
class Carro:
     def __init__(self, cor, estado='novo'): #vem pré definido tds q tiverem 'estado'
        self.estado=estado #(atributo) com variavel que vai ser definida
        self.cor=cor
    
fusca=Carro()
fusca.estado='novo'
fusca.cor='azul'

ferrari=Carro()
ferrari.estado='usado'
ferrari.cor='vermelha'

print (fusca.estado, ferrari.estado)
print(type(fusca))
print(type(ferrari))
print(fusca.cor, ferrari.cor)

##########5
class Aluno:
    def __init__(self, nome, nota):
        self.nome=nome   #definiçao de atributo nome com a variavel vazia
        self.nota=nota
    
nome=Aluno
nota=Aluno
nome=input('Digite seu nome: ')
nota=input(float('Digite sua nota: ')) #coerçao
aluno1=Aluno(nome, nota)

print(aluno1.nome, aluno1.nota)

########6
'''
class ContaBancaria:
    def __init__ (self, saldo=0): #definiçao do metodo construtor
        self.saldo=saldo
        
conta1=ContaBancaria(100)
conta2=ContaBancaria(1000)

print(conta1.saldo, conta2.saldo)

#########7
                                                                                                  





    













