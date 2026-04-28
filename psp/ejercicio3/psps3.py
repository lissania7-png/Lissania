import math
class Correlacion(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x)

    def calcular(self):
        sumx = sum(self.x)
        sumy = sum(self.y)
        sumxy = sum(a*b for a,b in zip(self.x,self.y))
        sumx2 = sum(a*a for a in self.x)
        sumy2 = sum(b*b for b in self.y)

        numer = (self.n * sumxy) - (sumx * sumy)
        denom = math.sqrt((self.n * sumx2 - sumx**2)*(self.n * sumy2 - sumy**2))

        r = numer / denom
        r2 = r**2

        # t de student
        t = abs(r) * math.sqrt((self.n - 2) / (1 - r**2))

        return r, r2, t
    