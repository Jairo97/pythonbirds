import unittest
from unittest import TestCase

from oo.carro import Motor, Direcao, Carro
#TESTE UTILIZANDO O UNITTEST
#TESTE UNITARIO É QUANDO VOCE QUER TESTAR UMA CLASSE EM ISOLAMENTO, IDEPENDENTE DE  QUAIS QUER CLASSES QUE ELA DEPENDA.
class CarroTeste(TestCase):
    def teste_motor_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0,motor.velocidade)
    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1,motor.velocidade)
    def teste_frear(self):
        motor = Motor()
        motor.frear()
        self.assertEqual(0,motor.velocidade)
    def teste_direcao(self):
        direcao = Direcao()
        self.assertEqual('Norte', direcao.valor)
    def teste_carro_acelerar(self):
        motor = Motor()
        direcao = Direcao()
        carro = Carro(direcao,motor)
        carro.motor.acelerar()
        self.assertEqual(1,carro.motor.velocidade)
    def teste_carro_direcao(self):
        motor = Motor()
        direcao = Direcao()
        carro = Carro(direcao, motor)
        carro.direcao.girar_a_direita()
        self.assertEqual('Leste', carro.direcao.valor)
        carro.direcao.girar_a_direita()
        carro.direcao.girar_a_direita()
        self.assertEqual('Oeste', carro.direcao.valor)
        carro.direcao.girar_a_esquerda()
        self.assertEqual('Sul', carro.direcao.valor)