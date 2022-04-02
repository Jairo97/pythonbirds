class Pessoa:
    def __init__(self,*filhos,nome=None,idade=37):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def comprimentar(self):
        return f'Olá {self.nome} sua idade  é: {self.idade}'

if __name__ == '__main__':
    filho = Pessoa(nome= 'San')
    pessoa = Pessoa(filho,nome='Fulano')
    print(pessoa.comprimentar())
    print(pessoa.filhos)
    for filho in pessoa.filhos:
        print(filho.nome)
