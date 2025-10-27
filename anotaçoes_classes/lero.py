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
#########1

class Pessoa:
    def __init__(self, nome):
        self.nome=nome
        
p1=Pessoa('Ana') #o self q é o p1 da classe pessoa atribui o nome dos parentesis para si
p2=Pessoa('Sofia')

print (p1.nome)
print (p2.nome)


########2
class Animal:
    def __init__(self, tipo):
        self.tipo=tipo
        
bicho1=Animal('gato')
bicho2=Animal('cachorro')

print (bicho1.tipo, bicho2.tipo)

########3
class Carro(object):
    estado='novo'
    
fusca=Carro()
fusca.estado='novo'

ferrari=Carro()
ferrari.estado='usado'

print (fusca.estado)
print (ferrari.estado)
print(type(fusca))
print(type(ferrari))
'''
##########4
class Carro(object):
    def __init__(self, estado, cor):
        self.estado=estado
        self.cor=cor
    
    
fusca=Carro('novo', 'azul')
#fusca.estado='novo'
ferrari=Carro('usado', 'vermelho')
#ferrari.estado='usado'

print ((type(fusca)),fusca.cor)
print((type(ferrari)),ferrari.cor)
                                                                                                  





    












