class Pessoa:
    olhos = 2 #Atributo default (Atributo de Classe)
    def __init__(self,*filhos,nome=None,idade=37):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def comprimentar(self):
        return f'Olá, meu nome é {self.nome}, Tudo bem?'
    @staticmethod
    def metodo_estatico():
        return 43
    @classmethod
    def metodo_de_classe(cls):
        return f'{cls} - {cls.olhos}'
#A herança serve para a reutilização de codigo. (atributos,metodos)
class Homem(Pessoa):
    def comprimentar(self):
        comprimentar_classe_pai = super().comprimentar()
        return f'{comprimentar_classe_pai}, Aperto de mão.'
class Mutante(Pessoa):
    olhos = 3 #Subscrita de dados

if __name__ == '__main__':
    filho = Homem(nome= 'San',idade=17)
    pessoa = Pessoa(filho,nome='Din')
    fulano = Mutante(nome='Fulano',idade=36)
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
    Pessoa.olhos = 2
    print(Pessoa.olhos, pessoa.olhos, filho.olhos)
    print(id(Pessoa.olhos),id(pessoa.olhos), id(filho.olhos))
    print(Pessoa.metodo_estatico(), pessoa.metodo_estatico())
    print(Pessoa.metodo_de_classe(), pessoa.metodo_de_classe())
    print(isinstance(pessoa, Pessoa))#Verifica se o objeto pessoa é da classe Pessoa
    print(isinstance(pessoa, Homem))  # Verifica se o objeto pessoa é da classe Homem
    print(isinstance(filho,Pessoa)) #Verifica se o objeto filho é da classe Pessoa
    print(isinstance(filho, Homem))  # Verifica se o objeto filho é da classe Homem
    print(isinstance(fulano, Homem))  # Verifica se o objeto fulano é da classe Homem
    print(fulano.olhos) #Subscrita de atributos
    print(filho.comprimentar())
    print(fulano.comprimentar())



