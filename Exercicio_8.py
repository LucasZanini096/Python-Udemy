import json

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 

    def get_ano_nacimento(self):
        return Pessoa.ano_atual - self.idade 



p1 = Pessoa("Lucas", 19)
print(p1.__dict__)



#Colocando num arquivo Json 

with open("arquivo_Json.json", "w+", encoding="utf8") as arquivo:
    
    json.dump(
        p1.__dict__,
        arquivo,
        indent=2,
        ensure_ascii=False
        )

print(__name__)

