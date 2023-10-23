import sys
from sympy import symbols, sympify, diff

e = 0.00001

def bissecao(expressao, a, b, fA, fB):
    if fA*fB > 0:
        print("Intervalo inválido")
        sys.exit()

    fX = 1
    i=0

    while abs(fX) > e:
        x = (a + b) / 2
        fX = eval(expressao.replace('x', str(x)))

        if fX * fA < 0:
            b = x
        elif fX * fB < 0:
            a = x

        i += 1
    print(f"\nRaiz Bissecao em {i} iteracoes: ", x)

def falsa_posicao(expressao, a, b, fA, fB):
    if fA * fB > 0:
        print("Intervalo inválido")
        sys.exit()

    fX = 1
    i = 0

    while abs(fX) > e and abs(b - a) > e:
        x = ((a * fB) - (b * fA)) / (fB - fA)
        fX = eval(expressao.replace('x', str(x)))

        if fX * fA < 0:
            b = x
            fB = fX
        elif fX * fB < 0:
            a = x
            fA = fX

        i += 1
    print(f"Raiz Falsa-Posicao em {i} iteracoes: ", x)


def newton_raphson(expressao, xk):
    x = symbols('x')
    expressao = sympify(expressao)
    derivada = diff(expressao, x)

    i = 0
    while i < 100:
        fXk = expressao.subs(x, xk)
        fXkl = derivada.subs(x, xk)
        xk1 = xk - (fXk / fXkl)

        if abs(xk1 - xk) < e:
            break

        xk = xk1
        i += 1

    print(f"Raiz Newton-Raphson em {i} iteracoes: ", xk)

def main():
    expressaoString = input("Digite a expressão matemática seguindo o exemplo abaixo:\n\n x^3 - 9*x + 5 \n\n     sera\n\n x**3 - 9*x + 5\n\n")
    a = float(input("\nDigite o valor de 'a' para o intervalo [a, b]: "))
    b = float(input("Digite o valor de 'b' para o intervalo [a, b]   (o metodo de newton utiliza a media aritmética do intervlao como chute inicial)  : "))

    fA = eval(expressaoString.replace('x', str(a)))
    fB = eval(expressaoString.replace('x', str(b)))
    xk = a/b

    bissecao(expressaoString, a, b, fA, fB)
    falsa_posicao(expressaoString, a, b, fA, fB)
    newton_raphson(expressaoString, xk)

if __name__ == "__main__":
    main()
