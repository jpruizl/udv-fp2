class Punto:

    array_de_puntos = []

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        print("(" + str(self.x) + ", " + str(self.y) + ")")
    
    def cuadrante(self):
        if self.x[0] == '-' and self.y[0] != '-':
            print('Cuadrante 2')
        elif self.x[0] == '-' and self.y[0] == '-':
            print('Cuadrante 3')
        elif self.y[0] == '-':
            print('Cuadrante 4')
        else:
            print('Cuadrante 1')
        
        punto = [int(self.x), int(self.y)]
        self.array_de_puntos.append(punto)
    
    def vector(self):
        resultado_x = self.array_de_puntos[0][0] - self.array_de_puntos[1][0]
        resultado_y = self.array_de_puntos[0][1] - self.array_de_puntos[1][1]
        print('resultado x: ', resultado_x)
        print('resultado y: ', resultado_y)



if __name__ == '__main__':
    plano = Punto('10','10')
    plano.cuadrante()
    plano.__str__()
    plano = Punto('5', '5')
    plano.cuadrante()
    plano.__str__()
    plano.vector()
    