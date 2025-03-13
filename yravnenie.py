from math import sqrt

class equation:

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def discr(self):
        self.discriminant = self.b*2-4*self.a*self.c
        print('Дискриминант равен{self.discriminant}')

    def root(self):
        if self.discriminant>0:
            self.x1= (-self.b + sqrt(self.discriminant))/2*self.a
            self.x2= (-self.b - sqrt(self.discriminant))/2*self.a
            print(f'Первый корень равен {self.x1}')
            print(f'Второй корень равен{self.x2}')
        else:
             print('Нет корней')

    def x_ver(self):
        self.x_ver_1= -self.b/2*self.a
        print(f'Вершина параболы равна {self.x_ver_1}')

    def y_ver(self):
        self.y_ver_1= self.a*sqrt(self.x_ver_1)+self.b*self.x_ver_1+self.c
        print(f'Вершина параболы равна {self.y_ver_1}')

    def parabola(self,ver):

    


