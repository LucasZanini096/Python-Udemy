#Atributos de classe
#Maneira de como evitar o HardCode


class Pessoa:

    ano_atual = 2022 #Estou criando um atributo da classe em si 
    #Vai ter o mesmo valor em tdoas as instâncias dessa classe 
    #Está atrelado ao molde da classe
    
    
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 

    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade #Chamo o atributo da Classe dessa maneira : Pessoa.(nome_do_atributo)


p1 = Pessoa ('João', 35)
p2 = Pessoa ('Helena', 12)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

