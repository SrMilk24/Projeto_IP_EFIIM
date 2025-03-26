class Calopsita:
    def __init__(self, nome, aveia, velocidade, golpe):
        self.nome = nome
        self.aveia = aveia
        self.velocidade = velocidade
        self.golpe =golpe

        return None
    
    def __str__(self):
        return "member of Test"
    # Todas as funções no use_case
    def set_nome(self, nome):
        self.nome = nome

juliano = Calopsita("Juliano", 10, 10, ["bicada atomica super poderosa"])
marcelo = Calopsita("Marcelo", 10, 10, ["Bundada de tanajura"])

print(juliano.golpe)
print(marcelo.golpe)