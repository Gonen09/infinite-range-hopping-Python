import math
import matplotlib.pyplot as plt


def generador_v(vector_n, constante):

    """ Genera un vector de V's a partir de un vector de N's y una constante"""

    v = []

    for x in range(len(vector_n)):
        nv = vector_n[x] // constante  # // = Division entera
        v.append(nv)

    # print("valores n: ", vector_n)
    # print("valores v: ", v)

    return v


def generador_n(vector_v, constante):

    """ Genera un vector de N's a partir de un vector de V's y una constante"""

    n = []

    for x in range(len(vector_v)):
        nn = vector_v[x] * constante
        n.append(nn)

    # print("valores v: ", vector_v)
    # print("valores n: ", n)

    return n


def f1(b, u, lam, gam, v, N):
    sumatoria = 0

    for n in range(1, N):
        try:
            sumatoria += n * math.exp(b * ((-lam + u + (gam / v)) * n - (gam / v) * math.pow(n, 2)))
        except OverflowError:
            print("Desbordamiento")
            break

    return sumatoria


def f2(b, u, lam, gam, v, N):
    sumatoria = 0

    for n in range(N):
        try:
            sumatoria += math.exp(b * ((-lam + u + (gam / v)) * n - (gam / v) * math.pow(n, 2)))
        except OverflowError:
            print("Desbordamiento")
            break

    return sumatoria


def calculo_ro(b, u, lam, gam, v, n):
    try:
        numerador = f1(b, u, lam, gam, v, n)
        denominador = f2(b, u, lam, gam, v, n)
        fraccion1 = 1 / v
        fraccion2 = numerador / denominador
        ro = fraccion1 * fraccion2

        # print("Numerador: ", numerador)
        # print("Denominador: ", denominador)
        # print("fraccion 1: ", fraccion1)
        # print("fraccion 2: ", fraccion2)
        # print("Ro: ", ro)

    except ZeroDivisionError:
        print('Division por cero')
        ro = 0

    print("Valor ro: ", ro)
    return ro


def calculo_validador(u, lam, gam):
    try:
        resultado = (u - lam) / (2 * gam)
    except ZeroDivisionError:
        print('Division por cero')
        resultado = 0

    print("Valor validador: ", resultado)
    return resultado


def graficador(datos_x, datos_y, titulo, titulo_x, titulo_y, ajuste_ejes=False):
    if len(datos_x) != 0 or len(datos_y) != 0:

        # Informacion grafico
        plt.title(titulo)
        plt.xlabel(titulo_x)
        plt.ylabel(titulo_y)

        if ajuste_ejes:
            # Limites grafico
            minimo_x = min(datos_x) - 1
            maximo_x = max(datos_x) + 1
            minimo_y = min(datos_y) - 1
            maximo_y = max(datos_y) + 1
            plt.xlim(minimo_x, maximo_x)
            plt.ylim(minimo_y, maximo_y)

        # Mostrar datos
        plt.plot(datos_x, datos_y, 'ro')
        plt.show()
    else:
        print("Vector vacio")


def metodo1(b, u, lam, gam, v, n):

    """ Calcular el valor real y el esperado """

    ro = calculo_ro(b, u, lam, gam, v, n)
    vro = calculo_validador(u, lam, gam)

    return ro, vro


def metodo2(valores, vector_v, vector_n):
    """ Grupo fijo de valores e iterar con un N y un V, Valores: +β,-µ,-λ,+γ """

    salida_resultado = []

    for x in range(len(vector_n)):
        ro = calculo_ro(valores[0], valores[1], valores[2], valores[3], vector_v[x], vector_n[x])
        salida_resultado.append(ro)

    salida_esperado = calculo_validador(valores[1], valores[2], valores[3])
    return salida_resultado, salida_esperado


def metodo3_beta(vector_b, u, lam, gam, v, n):
    """ Grupo fijo de valores con un vector iterable, Valores: +β,-µ,-λ,+γ,V,N """

    salida_resultado = []
    salida_esperado = []

    for x in range(len(vector_b)):
        print("Beta: ", vector_b[x], " Mu:", u, " Lambda: ", lam, " Gamma: ", gam, " Volumen: ", v, " Particulas: ", n)

        ro, rvo = metodo1(vector_b[x], u, lam, gam, v, n)
        salida_resultado.append(ro)
        salida_esperado.append(rvo)

        print(" ")
        print(" ")

    return salida_resultado, salida_esperado


def metodo3_mu(b, vector_u, lam, gam, v, n):
    """ Grupo fijo de valores con un vector iterable, Valores: +β,-µ,-λ,+γ,V,N """

    salida_resultado = []
    salida_esperado = []

    for x in range(len(vector_u)):
        print("Beta: ", b, " Mu:", vector_u[x], " Lambda: ", lam, " Gamma: ", gam, " Volumen: ", v, " Particulas: ", n)

        ro, rvo = metodo1(b, vector_u[x], lam, gam, v, n)
        salida_resultado.append(ro)
        salida_esperado.append(rvo)

        print(" ")
        print(" ")

    return salida_resultado, salida_esperado


def metodo3_lambda(b, u, vector_lam, gam, v, n):
    """ Grupo fijo de valores con un vector iterable, Valores: +β,-µ,-λ,+γ,V,N """

    salida_resultado = []
    salida_esperado = []

    for x in range(len(vector_lam)):
        print("Beta: ", b, " Mu:", u, " Lambda: ", vector_lam[x], " Gamma: ", gam, " Volumen: ", v, " Particulas: ", n)

        ro, rvo = metodo1(b, u, vector_lam[x], gam, v, n)
        salida_resultado.append(ro)
        salida_esperado.append(rvo)

        print(" ")
        print(" ")

    return salida_resultado, salida_esperado


def metodo3_gamma(b, u, lam, vector_gam, v, n):
    """ Grupo fijo de valores con un vector iterable, Valores: +β,-µ,-λ,+γ,V,N """

    salida_resultado = []
    salida_esperado = []

    for x in range(len(vector_gam)):
        print("Beta: ", b, " Mu:", u, " Lambda: ", lam, " Gamma: ", vector_gam[x], " Volumen: ", v, " Particulas: ", n)

        ro, rvo = metodo1(b, u, lam, vector_gam[x], v, n)
        salida_resultado.append(ro)
        salida_esperado.append(rvo)

        print(" ")
        print(" ")

    return salida_resultado, salida_esperado


def main():

    # Valores iniciales
    B = 15      # Positivo
    U = -0.05   # Menor que cero
    lam = -0.3  # Menor que mu
    gam = 50    # Positivo

    # V Valor muy grande
    # N Numero total de particulas

    configuracion = [B, U, lam, gam]

    vect_n = [100, 250, 380, 490, 550]
    nv = generador_v(vect_n, 0.5)

    experimento(configuracion, nv, vect_n)

    print("###################################")

    vect_v = [70, 84, 96, 102, 158]
    nn = generador_n(vect_v, 500)

    experimento(configuracion, vect_v, nn)

    return 0


if __name__ == '__main__':
    main()
