class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá{id(self)}'

if __name__ == '__main__':
    thaila = Pessoa(nome='Thaila')
    junior = Pessoa(thaila, nome='Junior')
    print(Pessoa.cumprimentar(junior))
    print(id(junior))
    print(junior.cumprimentar())
    print(junior.nome)
    print(junior.idade)
    for filho in junior.filhos:
        print(filho.nome)
    junior.sobrenome = 'Reis'
    del junior.filhos
    print(junior.__dict__)
    print(thaila.__dict__)

