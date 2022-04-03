class Pessoa:
    olhos = 2 #Atributo default (Atributo de Classe)
    def __init__(self,*filhos,nome=None,idade=37):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def comprimentar(self):
        return f'Olá {self.nome} sua idade  é: {self.idade}'
    @staticmethod
    def metodo_estatico():
        return 43
    @classmethod
    def metodo_de_classe(cls):
        return f'{cls} - {cls.olhos}'

if __name__ == '__main__':
    filho = Pessoa(nome= 'San',idade=17)
    pessoa = Pessoa(filho,nome='Din')
    print(pessoa.comprimentar())
    for filho in pessoa.filhos:
        print(f'{pessoa.nome} é pai de {filho.nome}')
    pessoa.sobrenome = 'Ramalho'
    print(f'{pessoa.nome} {pessoa.sobrenome}')
    del pessoa.filhos
    print(pessoa.__dict__)
    print(filho.__dict__)
    pessoa.olhos = 1
    print(id(pessoa.olhos))
    del pessoa.olhos
    Pessoa.olhos = 3
    print(Pessoa.olhos, pessoa.olhos, filho.olhos)
    print(id(Pessoa.olhos),id(pessoa.olhos), id(filho.olhos))
    print(Pessoa.metodo_estatico(), pessoa.metodo_estatico())
    print(Pessoa.metodo_de_classe(), pessoa.metodo_de_classe())
