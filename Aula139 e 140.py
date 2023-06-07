# super() é super lasse na sub classe
# Classe principal (Pessoa)
# -> super class, base class, parent class
# Classes filhas (Cliente)
# -> sub class, child class, derived class

class MinhaString(str):
    def upper(self): #Realizei a sobreposição do método upper original de STR
        print('CHAMOU UPPER') #Mas ainda eu desejo utilizar o método original da classe 
        #Solução
        retorno = super().upper() 
        print('DEPOIS DO UPPER')
        return retorno 

        #O super() recebe automaticamente a classe de referência e o seu self em seu parâmetro
        #Não havendo a necessidade de declará-los 
        #Ele chama um método específico(declarado) da classe gernérica correspondente 
        #Na qual será executado 

string = MinhaString('Luiz')
print(string.upper())



class A:

    atributo_a = "valor"


    def __init__(self,atributo):
        self.atributo_ = atributo

    def metodo(self):
        print("A")

class B(A):

    atributo_b = "valor"

    def __init__(self, atributo, outra_coisa): #Caso eu queira declarar um __init__ em B
        super().__init__(atributo) #Eu tenho que declarar um super() com o método 
        #De init para A
        self.outra_coisa = outra_coisa

    def metodo(self):
        print("b")

class C(B):

    atributo_c = "valor"

    def __init__(self, *args, **kwargs):
        print("EI, burlei o sistema. ")
        super().__init__(*args, **kwargs)


    def metodo(self):
        super(C, self).metodo() #Busca em B o nome do método
        super(B, self).metodo() #Busca em A o nome do método 
        #OU
        #A.metodo(self) -> Essa estrutura funciona como um super().metodo()
        #B.metodo(self)
        print("C")

c = C('atributo', "Qualquer") #Vou ter que instânciar c com um atributo, pois realizei o init em A
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
print(c.outra_coisa)
c.metodo()
print(C.mro()) #Retorna o Method Resolution Order no Terminal 

