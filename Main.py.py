lass Calculadora:
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
