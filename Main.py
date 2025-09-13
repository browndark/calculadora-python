class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Não é possível dividir por zero")
        return a / b


if __name__ == "__main__":
    calc = Calculadora()

    # Solicita entradas do usuário
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /): ")

    if operacao == "+":
        print("Resultado:", calc.somar(a, b))
    elif operacao == "-":
        print("Resultado:", calc.subtrair(a, b))
    elif operacao == "*":
        print("Resultado:", calc.multiplicar(a, b))
    elif operacao == "/":
        try:
            print("Resultado:", calc.dividir(a, b))
        except ZeroDivisionError as e:
            print("Erro:", e)
    else:
        print("Operação inválida!")

import unittest
from Main import Calculadora

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_soma(self):
        self.assertEqual(self.calc.somar(2, 3), 5)

    def test_subtracao(self):
        self.assertEqual(self.calc.subtrair(10, 4), 6)

    def test_multiplicacao(self):
        self.assertEqual(self.calc.multiplicar(3, 7), 21)

    def test_divisao(self):
        self.assertEqual(self.calc.dividir(8, 2), 4)

    def test_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.dividir(5, 0)

if __name__ == "__main__":
    unittest.main()

import timeit
from Main import Calculadora

calc = Calculadora()
tempo = timeit.timeit(lambda: calc.somar(100, 200), number=1000000)
print("Tempo:", tempo, "segundos")
