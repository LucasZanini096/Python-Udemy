class Pessoa:
    def __init__(self, nome, sobrenome): #Sempre o primeiro parâmetro dessa função será "Self"
        #Essa função recebe parâmetros
        #A instância da classe é referênciada pelo "Self"

        self.nome = nome #Dentro da instância dessa classe eu estou criando um atributo chamado nome,
        #na qual recebe como parâmetro "nome"

        self.sobrenome = sobrenome


#p1 = Pessoa() #Inicializando um objeto, porém sem inicializar os seus atributos
#p1.nome = "Luiz"  #Criação de uma instância 
#p1.sobrenome =  "Otávio"

p2 = Pessoa("Maria", "Joana") #Cria um novo objeto e coloca dentro dessa varável 
#p2.nome = "Maria"
#p2.sobrenome = "Joana"

#print(p1.nome)
#print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)


#O "self" referência o objeto que está sendo criado -> me permite ter dados diferentes em cada instância 
#Quando eu crio uma classe, eu crio um molde 
#Este molde vai gerar novos objeto, em que cada objeto via ter seu próprio self dentro da classe
#O método __init__ permite a inicialiação dos atributos de uma classe 

