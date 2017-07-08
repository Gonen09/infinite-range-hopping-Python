import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

B = 15  # Temperatura inversa
U = 0.5
LAM = 3
N = 10
K = 0.3  # Entero positivo


def f1(b, u, lam, N):
    sumatoria = 0
    for n in range(1, N):
        sumatoria += n*math.exp(b*((u+lam-1)*n-lam*math.pow(n, 2)))
    return sumatoria


def f2(b, u, lam, N):
    sumatoria = 0.0
    for n in range(N):
        resul = math.exp(b*((u+lam-1)*n-lam*math.pow(n, 2)))
        sumatoria += resul
    return sumatoria


def grafica(x, y, foto=False):
    if len(x) != 0 or len(y) != 0:
        plt.plot(x, y, 'bo')
        limInfx = min(x)-1
        limSupx = max(x)+1
        limInfy = min(y)-1
        limSupy = max(y)+1
        plt.axis([limInfx, limSupx, limInfy, limSupy])  # Longitud ejes x,y

        # define plot size in inches (width, height) & resolution(DPI)
        # plt.figure(figsize=(20, 10), dpi=100)
        # plt.figure(figsize=(2,2))

        if foto == True:
            fig = plt.gcf()
            fig.set_size_inches(18.5, 10.5)
            fig.savefig('test2png.png', dpi=100)
        plt.show()
    else:
        print("Vector vacio")


class Grafica:
    def __init__(self):
        self.x = []
        self.listaY = []

        self.limInfx = 0
        self.limSupx = 0
        self.limInfy = 0
        self.limSupy = 0

        self.fig, self.ax = plt.subplots()

    def funcionX(self, func):
        self.x = func

    def agregarFuncionY(self, y, color, figura, variable):
        self.listaY.append([y, color, figura, variable])
        if len(self.listaY) == 1:
            self.limInfx = min(self.x) - 1
            self.limSupx = max(self.x) + 1
            self.limInfy = min(y) - 1
            self.limSupy = max(y) + 1
        else:
            if min(y) - 1 < self.limInfy:
                self.limInfy = min(y) -1

            if max(y) + 1 > self.limSupx:
                self.limInfy = max(y) +1

    def ajusteEjes(self):
        pass

    def mostrarGrafico(self):
        for y in self.listaY:
            self.ax.plot(self.x, y[0], y[1]+y[2], linewidth=2, label='B: '+str(y[3]))
        legend = self.ax.legend(shadow=True)
        plt.show()


class FuncionRo(object):
    def __init__(self):
        self.densidad_punto = 200.0
        self.rango_eje_x = [-10, 15]
        self.u = []  # ejex
        self.ro = []  # ejey
        self.b = B # inversa de la temperatura
        self.n = N
        self.lam = LAM

    def funcionRo(self):
        densidad_puntos = self.densidad_punto
        rango_de_U = self.rango_eje_x
        x = self.u = []
        y = self.ro = []
        u = rango_de_U[0]

        for i in range(int(densidad_puntos)):
            u += (rango_de_U[1] - rango_de_U[0]) / densidad_puntos
            try:
                ro = f1(self.b, u, self.lam, self.n) / f2(self.b, u, self.lam, self.n)
                x.append(u)
                y.append(ro)
            except ZeroDivisionError:
                print('Division por cero')
                break
            except OverflowError:
                print('overflow')
                break
        return x, y


class AnimacionDensidad:
    def __init__(self):
        self.funcion = FuncionRo()
        # self.figura = plt.figure()
        self.fig = plt.figure()
        self.ax = plt.axes(xlim=(-10, 15), ylim=(-1, 4))
        self.line, = self.ax.plot([], [],'k.', lw=2)
        self.ax.set_title('ro vs mu')
        self.ax.set_xlabel('mu')
        self.ax.set_ylabel('ro')
        self.ax.legend(labels="funcion ro")
        self.text = self.ax.text(-7, 3, r'an equation: $E=mc^2$', fontsize=15)
        self.densidad = 1.0

    def init(self):
        self.line.set_data([], [])
        return self.line,

    def actualizacion(self, i):
        if self.funcion.densidad_punto<1000:
            # print self.funcion.densidad_punto
            #self.ax.legend(labels=str(self.funcion.densidad_punto))
            
            self.funcion.densidad_punto += self.densidad
            self.funcion.funcionRo()
        self.line.set_data(self.funcion.u, self.funcion.ro)
        return self.line,

    def actualizacion1(self, i):
        if self.funcion.b < 50:
            self.text.set_text(r'\gamma'+ str(round(self.funcion.b,2)))
            self.funcion.b += 0.1
            self.funcion.funcionRo()
        self.line.set_data(self.funcion.u, self.funcion.ro)
        return self.line,



def arreglos_B_XY(B, u, lam, N):
    densidad_puntos = 1000.0
    rango_de_U = [-10, 10]
    x = []
    y = []
    u = rango_de_U[0]

    for i in range(int(densidad_puntos)):
        u += (rango_de_U[1]-rango_de_U[0])/densidad_puntos
        try:
            ro = f1(B, u, lam, N)/f2(B, u, lam, N)
            x.append(u)
            y.append(ro)
        except ZeroDivisionError:
            print('Division por cero')
            break
        except OverflowError:
            print('overflow')
            break
    return x,y


"""
funcion = FuncionRo()
funcion.funcionRo()
#x,y=arreglos_B_XY(B, U, LAM, N)
grafico = Grafica()
grafico.funcionX(funcion.u)
grafico.agregarFuncionY(funcion.ro, 'r', '.', 2)

#x,y=arreglos_B_XY(15, U, LAM, N)
#grafico.funcionX(x)
funcion.b = 20
funcion.funcionRo()
grafico.agregarFuncionY(funcion.ro, 'b', '.', 15)
"""
# grafico.mostrarGrafico()

animacionB = AnimacionDensidad()
animacionB.funcion.densidad_punto = 150.0
animacionB.funcion.b = 0.0
anim = animation.FuncAnimation(animacionB.fig, animacionB.actualizacion1,init_func=animacionB.init, frames=120, interval=80, blit=False)

animacionD = AnimacionDensidad()
animacionD.funcion.densidad_punto = 2
anim1 = animation.FuncAnimation(animacionD.fig, animacionD.actualizacion,init_func=animacionD.init,frames=200, interval=120, blit=False)

# line_ani = animation.FuncAnimation(animacionD.fig, animacionD.actualizacion, 25, interval=200, blit=True, repeat=True)

# anim.save('basic_animation.mp4', fps=30)
# anim.save('im.mp4', writer="ffmpeg")
# plt.show()






