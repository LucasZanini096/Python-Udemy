import json
#from Exercicio_8 import Pessoa

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 

    def get_ano_nacimento(self):
        return Pessoa.ano_atual - self.idade 




with open("arquivo_Json.json", "r", encoding="utf8") as arquivo:
    p2 = Pessoa(**json.load(arquivo))
    
print(p2.nome)
print(p2.idade)

print(__name__)
