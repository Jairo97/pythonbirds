class Pessoa:
    def __init__(self,nome=None,idade=37):
        self.nome = nome
        self.idade = idade

    def comprimentar(self):
        return f'Olá {self.nome} sua idade  é: {self.idade}'

if __name__ == '__main__':
    pessoa = Pessoa('Fulano',38)
    print(pessoa.comprimentar())

