import math

class Intervalos(object):
    def __init__(self, x, y, xk):
        self.x = x
        self.y = y
        self.n = len(x)
        self.xk = xk

    def calcular(self):
        xavg = sum(self.x)/self.n
        yavg = sum(self.y)/self.n

        sumxy = sum(a*b for a,b in zip(self.x,self.y))
        sumx2 = sum(a*a for a in self.x)

        b1 = (sumxy - self.n*xavg*yavg)/(sumx2 - self.n*xavg**2)
        b0 = yavg - b1*xavg

        yk = b0 + b1*self.xk

        # error estándar
        sr = 0
        for i in range(self.n):
            sr += (self.y[i] - (b0 + b1*self.x[i]))**2

        s = math.sqrt(sr/(self.n-2))

        sumx = sum((xi - xavg)**2 for xi in self.x)

        t = 2.262  # aprox (puedes ajustar según tabla)

        rango = t * s * math.sqrt(1 + 1/self.n + ((self.xk - xavg)**2 / sumx))

        upi = yk + rango
        lpi = yk - rango

        return yk, upi, lpi