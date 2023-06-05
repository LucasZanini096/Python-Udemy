# O nome Self é dado por convenção -> posso colocar em seu lugar qualquer outro nome 
#Desde que ele seja o primeiro parâmetro do método __init__ vai funcionar normalmente

#Lembre-se: a palavra Self é utilizada para referenciar a própria instância 
#Classe - Molde (gerlamente sem dados)
#Instância da class (objeto) - Tem os dados 
#Uma clsse pode gerar várias instâncias 
#Na classe o self é a própria instância 



class Carro: #Criação do molde
    def __init__(abc, nome) : #Inicializando uma instância 
         abc.nome = nome #Criação de um atributo 
        
    def acelerar(efg): 
        print(f"{efg.nome} está acelerando")  #Criação de um método



fusca = Carro()
print(fusca.nome)
fusca.acelerar() 
print(fusca.acelerar()) 
Carro.acelerar(fusca) #Vai dar erro !!! -> Pois eu estou chamando uma classe que não foi inicializada 
#Porém para eu corrigir este problema é so colocar o self dentro do parâmetro do método

celta = Carro(nome="Celta") 
print(celta.nome)
celta.acelerar()