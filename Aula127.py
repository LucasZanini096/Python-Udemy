#__dict__ e vars para atributos de instância (ambos funcionam em conjunto)
#Eles mantém um objeto do tipo mapping, que pode ser relacionado a um dicionário
# Ele é um dicionário que está dentro do meu objeto, dentro das minhas instâncias da minha classe 
#Resumindo, __dict__  e vars() salvam os objetos instanciados de uma classe (molde) 
# na forma de um dicionário 
#Assim como um dicionário tradicional, ele pode ser editável 



class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 

    def get_ano_nacimento(self):
        return Pessoa.ano_atual - self.idade 


p1 = Pessoa("João", 35)
p1.nome  = "Eita"
print(p1.idade)
print(p1.__dict__)
print(vars(p1))
p1.__dict__["outra"] = "coisa"  #Não é muito comum   
print(p1.__dict__) 

#Posso utilizar esse método para salvar minhas instâncias num arquivo Json 
#Já que o arquivo do tipo Json naão suporta Classes 

dados = {'nome': 'Eita', 'idade': 35}
p2 = Pessoa(**dados) #Desempacotando um dicionário 
print(p2.nome)
print(p2.idade)








