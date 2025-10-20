#PROGRAMAÇAO ORIENTADA A OBJETOS (POO)
# 
# classes sao estruturas de dados q possuem atributos e metodos ----- OBJETOS
#atributo é caracteristicas gerais do objeto trabalhado em questao q sao especificados posteriormente ----- VARIAVEIS
#metodo é as funçoes q ele vai executar/já executa ----- FUNÇOES
#classes podem ser iguais mas com variaveis e metodos diferentes

#carro (classe)
# modelo -> ferrari
# ano -> 2020
# estado -> seminovo
# ^^^^^^Variaveis^^^^^^

# acelerar, frear, buzinar
# ^^^^^^Metodos^^^^^^
#
#classe tem q ta com primeira letra maiuscula
# ------------------------------------------
#def define funçao
#__init__ 'dois underlines'
#self referencia ao proprio objeto em questao
#def _init_(self, cor, marca, volume)
'''
class ControleRemoto:
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
print(type(fusca))
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






    









