open = True

def calculadora(operacao):
    if operacao == 1:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        return num1 + num2
    elif operacao == 2:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        return num1 - num2
    elif operacao == 3:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        return num1 * num2
    elif operacao == 4:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num2 == 0:
            print("Erro: Divisão por zero não é permitida.")
            return None
        else:
            return num1 / num2

while open == True:
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Calculadora Simples")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Escolha uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

    operacao = int(input("Digite o número da operação desejada: "))

    if operacao  <= 0 or operacao > 5:
        print("Operação inválida. Tente novamente.")
        continue

    if operacao == 5:
        print("Saindo da calculadora...")
        open = False
        break

    elif operacao == 1:
        resultado = calculadora(1)
        print(f"O resultado da adição é: {resultado}")

    elif operacao == 2:
        resultado = calculadora(2)
        print(f"O resultado da subtração é: {resultado}")

    elif operacao == 3:
        resultado = calculadora(3)
        print(f"O resultado da multiplicação é: {resultado}")

    elif operacao == 4:
        resultado = calculadora(4)
        if resultado is not None:
            print(f"O resultado da divisão é: {resultado}")