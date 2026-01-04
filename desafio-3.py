class Heroi:
    
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        ataque = ""

        # decisão
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        else:
            ataque = "um ataque desconhecido"

        #  f-strings
        print(f"o {self.tipo} atacou usando {ataque}")

# objetos 
meu_mago = Heroi("Gandalf", 100, "mago")
meu_ninja = Heroi("Hanzo", 25, "ninja")

meu_mago.atacar()
meu_ninja.atacar()