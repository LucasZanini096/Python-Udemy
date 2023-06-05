#Métodos de classe + factories(fábricas)
#São Mmétodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro 
# parâmetro, recebrermos a própria classe.


class Pessoa:
    ano = 2023 #atributo de classe > fora do escopo de um método da classe 

    def __init__(self, nome, idade):       
        self.nome = nome
        self.idade  = idade 
    
    def metodo_de_classe(self):
        print("Hey")

p1 = Pessoa('João', 34)
p1.metodo_de_classe()

#Pessoa.metodo_de_classe() # Vai dar erro, tenho que passar o self dentro do argumento

#Solução (@classmethod)

class Pessoa:
    ano = 2023 #atributo de classe > fora do escopo de um método da classe 

    def __init__(self, nome, idade):       
        self.nome = nome
        self.idade  = idade 
    

    @classmethod #Função decoradora que permite eu chamar minha classe sem self
    def metodo_de_classe(cls): #Essa função recebe a própria classe, denominada de "cls"
        print("Hey")

    @classmethod
    def criar_com_50_anos(cls,nome):
        return cls(nome,50) #Vai retornar a própria classe, que dentro dela vai instanciar nome e idade

    @classmethod
    def criar_sem_nome(cls,nome):
        return cls(nome,50) #Isso é uma fábrica de métodos, ou seja, estou criando métodos que acessam a própria classe(molde)


p1 = Pessoa('João', 34)
p1.metodo_de_classe()
p2 = Pessoa.criar_com_50_anos("Helena")
p3 = Pessoa("Anônima", 23)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)


