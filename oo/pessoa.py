class Pessoa:
    def __init__(self,*filhos,nome=None,idade=37):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def comprimentar(self):
        return f'Olá {self.nome} sua idade  é: {self.idade}'

if __name__ == '__main__':
    filho = Pessoa(nome= 'San')
    pessoa = Pessoa(filho,nome='Din')
    print(pessoa.comprimentar())
    for filho in pessoa.filhos:
        print(f'{pessoa.nome} é pai de {filho.nome}')
    pessoa.sobrenome = 'Ramalho'
    print(f'{pessoa.nome} {pessoa.sobrenome}')
    del pessoa.filhos
    print(pessoa.__dict__)
    print(filho.__dict__)