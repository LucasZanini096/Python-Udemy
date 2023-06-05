#Escopo da função e de métodos da classe
#A classe possui seu NameSpace (seu próprio escopo)
class Animal:
    #nome = "Leão"

    def __init__(self,nome):
        self.nome = nome


        variavel = "nome" #Eu não consigo acessar a variável "variavel" fora do escopo da função __init__
        print(variavel)
    

    #def acao(self):
    #    print(variavel) #Vai gerar um erro, pois "variavel" está dentro de um escopo de uma função 

    def comendo(self,alimento):
        return f'{self.nome} está comendo {alimento}'
    
    def executar(self, *args, **kwargs):
        return self.comendo(*args,**kwargs)


#print(Animal.nome) #Posso pegar a própria variável nome dentro da 
#própria classe sem instânciar essa classe.



leao = Animal(nome = "Leão")
print(leao.nome)
print(leao.executar("maçã"))



  