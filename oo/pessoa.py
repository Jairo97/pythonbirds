class Pessoa:
    def comprimentar(self,nome):
        return f'Olá {nome} seu id é: {id(self)}'

if __name__ == '__main__':
    pessoa = Pessoa()
    print(pessoa.comprimentar('Dell'))

