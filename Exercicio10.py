    
#Criar classe Motor

class Motor:
    def __init__(self,nome_motor):
        self.nome_motor = nome_motor

#Criar Fabricante

class Fabricante:
    def __init__(self, nome_fabricante):
        self.nome_motor = nome_fabricante


#Criar classe Carro 
class Carro:
   
    def __init__(self, nome):
        self.carro = []
        self.carro.append(nome)
        
    
    def carro_especificacoes(self,nome_motor,nome_fabricante):
        self.carro.append(Motor(nome_motor))
        self.carro.append(Fabricante(nome_fabricante))

        return f'Carro: {self.carro[0]} | Motor: {self.carro[1]} | Fabricante: {self.carro[2]}'
    

carro = Carro("Uno")
motor = Motor('1.5')
fabricante = Fabricante("Fiat")
print(carro.carro_especificacoes(motor, fabricante))

#Resolução 

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor (self,valor):
        self._motor = valor 

    @property
    def fabricante(self):
        return self._fabricante

    @motor.setter
    def fabricante(self,valor):
        self._motor = fabricante 

class Motor:
    def __init__(self, nome):
        self.nome = nome 

class Fabricante:
    def __init__(self, nome):
        self.nome = nome 

fusca = Carro("Fusca")
volkswagen = Fabricante("Volkswagen")
motor_1_0 = Motor("1.0")
fusca_fabricante = volkswagen
fusca.motor = motor_1_0
print(fusca.nome, fusca.fabricante, fusca.motor.nome)


    
