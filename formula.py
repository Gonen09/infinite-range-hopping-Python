import math
import matplotlib.pyplot as plt
import time

def f1(b , u , lam, N):
    sumatoria = 0
    for n in range(1, N):
        sumatoria+=n*math.exp(b*((u+lam-1)*n-lam*math.pow(n, 2)))
    return sumatoria

def f2(b , u , lam, N):
    sumatoria = 0.0
    for n in range(N):
        resul = math.exp(b*((u+lam-1)*n-lam*math.pow(n, 2)))
        sumatoria+= resul
    return sumatoria

def grafica(x, y, foto = False):
    if (len(x)!=0 or len(y)!=0):
        plt.plot(x, y, 'bo')
        limInfx=min(x)-1
        limSupx=max(x)+1
        limInfy=min(y)-1
        limSupy=max(y)+1
        plt.axis([limInfx, limSupx, limInfy, limSupy]) #Longitud ejes x,y

        #define plot size in inches (width, height) & resolution(DPI)
        #plt.figure(figsize=(20, 10), dpi=100)
        #plt.figure(figsize=(2,2))
        if foto ==True:
            fig = plt.gcf()
            fig.set_size_inches(18.5, 10.5)
            fig.savefig('test2png.png', dpi=100)
        plt.show()
    else:
        print("Vector vacio")


class Grafica():
    def __init__(self):
        self.x = []
        self.listaY=[]

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
            if min(y) -1 < self.limInfy:
                self.limInfy = min(y) -1

            if max(y) +1 > self.limSupx:
                self.limInfy = max(y) +1

    def ajusteEjes(self):
        pass


    def mostrarGrafico(self):
        for y in self.listaY:
            self.ax.plot(self.x, y[0], y[1]+y[2],linewidth = 2, label = 'B: '+str(y[3]))
        legend = self.ax.legend(shadow=True)
        plt.show()



def arreglos_B_XY(B, u, lam, N):
    densidad_puntos = 50.0
    rango_de_U = [-10, 10]
    x = []
    y = []
    u = rango_de_U[0]

    for i in range(int(densidad_puntos)):
        u += (rango_de_U[1]-rango_de_U[0])/densidad_puntos
        try:
            ro =  f1(B, u, lam, N)/f2(B, u, lam, N)
            x.append(u)
            y.append(ro)
        except ZeroDivisionError:
            print('Division por cero')
            break
        except OverflowError:
            print('overflow')
            break
    return x,y

B = 2  #Temperatura inversa
U = 0.5
lam =  3
N = 10
K = 0.3 # Entero positivo


x,y=arreglos_B_XY(B, U, lam, N)
grafico = Grafica()
grafico.funcionX(x)
grafico.agregarFuncionY(y, 'r', '*', 2)

x,y=arreglos_B_XY(15, U, lam, N)
grafico.agregarFuncionY(y, 'b', 'o', 15)
grafico.mostrarGrafico()



