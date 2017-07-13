import math
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import time
import sys


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
        # print ("Numerador: ",numerador)
        # print ("Denominador: ",denominador)
        # print ("fraccion 1: ",fraccion1)
        # print ("fraccion 2: ",fraccion2)
        # print ("Ro: ",ro)

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


def calculo_mu(rho, gamma, lamdda):
    mu = 2 * rho * gamma + lamdda
    return mu


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


def graficador(datos_x, datos_y, titulo, titulo_x, titulo_y, leyenda, ajuste_ejes=False):
    if len(datos_x) != 0 or len(datos_y) != 0:

        # Pesonalizar marco
        fig = plt.figure(facecolor='w', edgecolor='k', figsize=[8, 6])
        # Color del rectángulo de la figura, Color del perímetro de la figura, tamaño figura

        # Informacion grafico
        plt.title(titulo, fontsize=20, fontweight='bold', color='b')  # Titulo grafico
        plt.xlabel(titulo_x, fontsize=20, fontweight='bold', color='b')  # Titulo eje x
        plt.ylabel(titulo_y, fontsize=20, fontweight='bold', color='b')  # Titulo eje y
        # Titulo, tamaño texto, tipo texto, color texto

        # Rejilla fondo
        plt.grid(True)
        plt.grid(linestyle='--', linewidth=1, color='0.5')
        # Estilo_linea, Ancho_linea, Color_linea

        if ajuste_ejes:
            minimo_x = min(datos_x)
            maximo_x = max(datos_x)
            minimo_y = min(datos_y)
            maximo_y = max(datos_y)
            # Limites grafico
            plt.xlim(minimo_x, maximo_x)
            plt.ylim(minimo_y, maximo_y)

        # Graficar datos
        plt.plot(
            datos_x, datos_y,
            # Datos x, Datos y
            linestyle='-', linewidth=2, color='r',
            # Estilo_linea, Ancho_linea, Color_linea
            marker='d', markeredgecolor='b', markerfacecolor='c', markersize=7, fillstyle='full',
            # Estilo_puntos, Color_Borde_puntos, Color_relleno_puntos, tamaño_puntos, tipo_relleno_puntos
            label=leyenda
            # Etiqueta
        )

        # Mostrar leyenda
        plt.legend(prop={'size': 25}, fontsize=10, markerscale=2.5, loc='center right', bbox_to_anchor=(1.4, 0.5))
        # Tamaño leyenda, tamaño texto, tamaño icono, posicion dentro del grafico, posicion en coordenadas

        # Mostrar grafico
        plt.show()
    else:
        print("Vector vacio")


def grafico_3D_malla_mu(vector_gamma, vector_rho, lamdda, titulo, lyx, lyy, lyz):

    # Creamos la figura
    fig = plt.figure(figsize=[15, 10])  # Tamaño figura
    ax = fig.gca(projection='3d')  # Dibujar en 3D

    # Informacion grafico
    plt.title(titulo, fontsize=20, fontweight='bold', color='b')
    ax.set_xlabel(lyx, fontsize=20, fontweight='bold', color='b', labelpad=30)
    ax.set_ylabel(lyy, fontsize=20, fontweight='bold', color='b', labelpad=30)
    ax.set_zlabel(lyz, fontsize=20, fontweight='bold', color='b', labelpad=30)
    # Titulo, tamaño texto, tipo texto, color texto, espaciado texto

    # Texto flotante
    # ax.text2D(0.5, 0.5,"Texto 2D", fontsize=20, fontweight='bold', color='b', transform=ax.transAxes)
    # posicion x, posicion y, titulo, tamaño texto, tipo texto, color texto, ubicar

    # Cargar datos
    X = vector_gamma
    Y = vector_rho

    # Obtenemos las coordenadas a partir de los vectores creados
    X, Y = np.meshgrid(X, Y)  # Malla

    # Fomula a evaluar (mu)
    Z = 2 * Y * X + lamdda

    # Graficar alambrado
    ax.plot_wireframe(X, Y, Z, linewidth=2, color='b')

    # Limites ejes
    # ax.set_xlim(0, 10)
    # ax.set_ylim(0, 10)
    # ax.set_zlim(0, 10)

    # Fijar la posicion inicial de la grafica
    # ax.view_init(45, -35)
    # elev , azim

    # elev = almacena el ángulo de elevación en el plano z.
    # Azim = almacena el ángulo azimutal en el plano x, y.

    # Acercamiento
    # ax.dist = 10

    # Mostrar grafico
    plt.show()


def grafico_3D_plano_mu(vector_gamma, vector_rho, lamdda, titulo, lyx, lyy, lyz):

    # Creamos la figura
    fig = plt.figure(figsize=[15, 10])  # Tamaño figura
    ax = fig.gca(projection='3d')  # Dibujar en 3D

    # Informacion grafico
    plt.title(titulo, fontsize=20, fontweight='bold', color='b')
    ax.set_xlabel(lyx, fontsize=20, fontweight='bold', color='b', labelpad=30)
    ax.set_ylabel(lyy, fontsize=20, fontweight='bold', color='b', labelpad=30)
    ax.set_zlabel(lyz, fontsize=20, fontweight='bold', color='b', labelpad=30)
    # Titulo, tamaño texto, tipo texto, color texto, espaciado texto

    # Texto flotante
    # ax.text2D(0.5, 0.5,"Texto 2D", fontsize=20, fontweight='bold', color='b', transform=ax.transAxes)
    # posicion x, posicion y, titulo, tamaño texto, tipo texto, color texto, ubicar

    # Cargar datos
    X = vector_gamma
    Y = vector_rho

    # Obtenemos las coordenadas a partir de los vectores creados
    X, Y = np.meshgrid(X, Y)  # Malla

    # Fomula a evaluar (mu)
    Z = 2 * Y * X + lamdda

    # Graficar superficie
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    # cm = plasma,inferno,Blues,hot,BrBG,RdGy,RdBu,cool,coolwarm,bwr,hsv,jet,nipy_spectral,gist_ncar

    # Limites ejes
    # ax.set_xlim(0, 10)
    # ax.set_ylim(0, 10)
    # ax.set_zlim(0, 10)

    # Insertar barra de color que mapea los valores a colores
    fig.colorbar(surf, shrink=0.5, aspect=10)

    # Fijar la posicion inicial de la grafica
    # ax.view_init(45, -35)
    # elev , azim

    # elev = almacena el ángulo de elevación en el plano z.
    # Azim = almacena el ángulo azimutal en el plano x, y.

    # Acercamiento
    # ax.dist = 10

    # Mostrar grafico
    plt.show()


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


def metodo4(vector_rho, vector_gamma, lamdda):
    mu = []

    for x in range(len(vector_rho)):
        resultado = calculo_mu(vector_rho[x], vector_gamma[x], lamdda)
        mu.append(resultado)

    return mu


