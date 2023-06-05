#@staticmethod (métodos estáticos) são inúteis no Python =)
#Métodos estáticos são métodos que estão dentro da 
#classe, mas não em acesso ao self nem ao cls
#Em resumo, são funções que existem dentro da sua classe



class Classe:
    @staticmethod #Não possui acesso ao cls e ao self 
    #Uma função jogada no meio da classe, na qual não pode ser utilizada como um método 
    def funcao_que_esta_na_classe(*args, **kwargs):
        print("OI", args, kwargs)

def funcao(*args, **kwargs):
        print("OI", args, kwargs)


c1 = Classe()
c1.funcao_que_esta_na_classe(1,2,3)
funcao(1,2,3)
Classe.funcao_que_esta_na_classe(nomeado=1)
funcao(nomeado=1)

