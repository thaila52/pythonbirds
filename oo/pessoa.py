class Pessoa:
    olhos = 2
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
    junior.olhos = 1
    print(junior.__dict__)
    print(thaila.__dict__)
    print(Pessoa.olhos)
    print(thaila.olhos)
    print(junior.olhos)
    print(id(Pessoa.olhos), id(thaila.olhos), id(junior.olhos))

