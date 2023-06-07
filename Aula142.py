class A:
    ... #ou Pass

    def quem_sou(self):
        print("A")

class B (A):
    ... #ou Pass

    def quem_sou(self):
        print("B")
        
class C (A):
    ... #ou Pass

    def quem_sou(self):
        print("C")

class D (B,C): #A ordem importa !! -> Muda o algoritmo
    ... #ou Pass

    def quem_sou(self):
        print("D")


d = D()
d.quem_sou()
print(D.__mro__)
print(D.mro())