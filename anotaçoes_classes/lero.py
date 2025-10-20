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
'''
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











