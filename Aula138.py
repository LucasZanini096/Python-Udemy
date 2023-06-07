#Herança simples - Relações entre classes 
# Associação - usa, Agregação - tem 
#Composição - É dono de, Herança - É um
#
# Herança vs Composição (e Agregação e Associação)
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class (Vai herdar outras classes (classes filhas))
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

#Classes criam tipos (types, como int, float, boolean e entre outros)
#Relação de herança -> uma classe extende outra classe (uma é mais generalizada em relação à outra)

#Todas as Classes criadas já herdam de um built-in do próprio Python (str)
#Ela herda da super-classe Object

class Pessoa: #Classe genérica
    def __init__(self, nome, sobrenome):
        self.nome = nome 
        self.sobrenome = sobrenome 
    
    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__) 
        #self.__class__.__name__ -> permite eu saber o nome da classe

class Cliente(Pessoa): #Estou herdando a classe Pessoa para dentro de Cliente 
    #Todo o código escrito dentro de pessoa vai ser herdado para Cliente 
    ...

class Aluno(Pessoa):
    ...

c1 = Cliente("Luiz", "Antonio")
c1.falar_nome_classe()
c2 = Aluno("Maria", "Helena")
c2.falar_nome_classe()

#MRO -> Method Resolution Order 
#Primeiro ele resolve dentro da própria classe (sub-classe).
#Se não encontrar nada vai em direção à classe mais hierarquizada 
#Se não encontrar também, vai em direção a classe Objects 
# A herança pode deixar muito complexo o código para debugar
# Utilize 3 níveis no máximo !!!
