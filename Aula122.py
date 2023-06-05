#Métodos em instâncias de classes Python

#Classes são moldes que geram novas instâncias ou novos objetos. Objetos e instâncias referem-se a mesma coisa.
#Desejo criar um comportamento (ações) para a minha instância 

#Self -> refere-se a própria instância da classe 
#Hard Coded -> Algo fixo, ou seja, seu valor não muda, independentemente do molde aplicado. É um código escrito!! 


class Carro: #Cada carro tem seus atributos (cor, modelo, tipo) e suas ações (andar, frear e etc)
    def __init__(self, nome) : #O método __init__, por padrão empre retorna None
         self.nome = nome 
        
    def acelerar(self): #Os métodos são funções criadas dentro de classes 
        print(f"{self.nome} está acelerando")   #Me permite criar ações específicas 



fusca = Carro()
print(fusca.nome)
fusca.acelerar() 
print(fusca.acelerar()) #Vai retornar None Também !!!!
#Pois "self" retorna none por padrão 


celta = Carro(nome="Celta") #Parâmetro nomeado 
print(celta.nome)
celta.acelerar()





