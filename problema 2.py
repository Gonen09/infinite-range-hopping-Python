import math
import matplotlib.pyplot as plt


def generador_v(vector_n, constante):

    """ Genera un vector de V's a partir de un vector de N's y una constante"""

    v = []

    for x in range(len(vector_n)):
        nv = vector_n[x] / constante
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


def calculo_final(b, u, lam, gam, v, n):

    """ Calcular el valor real y el esperado """

    ro = calculo_ro(b, u, lam, gam, v, n)
    vro = calculo_validador(u, lam, gam)

    print("Valor real: ", ro)
    print("Valor esperado: ", vro)

    return ro, vro


def experimento(valores, vector_v, vector_n):

    """ La idea es tener un grupo fijo de valores e iterar con un N y un V, Valores: todos menos v y n 	"""

    salida_resultado = []
    salida_esperado = []

    for x in range(len(vector_n)):
        ro, rvo = calculo_final(valores[0], valores[1], valores[2], valores[3], vector_v[x], vector_n[x])
        salida_resultado.append(ro)
        salida_esperado.append(rvo)

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
