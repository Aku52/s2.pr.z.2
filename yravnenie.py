import numpy as np
import matplotlib.pyplot as plt

from math import sqrt


class Equation:

    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def discr(self):
        self.discriminant = self.b*2-4*self.a*self.c
        print('Дискриминант равен{self.discriminant}')

    def root_1(self):
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

    def dr_1_par(self):
        self.x1 = np.arange(-10, 10.01, 0.01)
        plt.plot(self.x1,self.x1**2)
        plt.show()

    def dr_1_par(self):
        self.x2 = np.arange(-10, 10.01, 0.01)
        plt.plot(self.x2,self.x2**2)
        plt.show()


class Derivative (Equation):

    def __init__(self,a,b,c,d):
        super(). __init__(self,a,b,c,d)

    def root_2(self):
        super().root_1()


    def deriv_y (self):
        y_der_1 = 2* self.a *self.x1+ self.b
        y_der_2 = 2* self.a *self.x2+ self.b
        print(f'Производная c x1 {y_der_1}')
        print(f'Производная c x2 {y_der_2}')


class Integral (Equation):

    def __init__(self,a,b,c,d):
        super(). __init__(self,a,b,c,d)

    def root_3(self):
        super().root_1()

    def int_y(self):
        y_int_1 = ((self.a*self.x1**3)/3)+ ((self.b*self.x1**2)/2)+(self.c*self.x1)+self.d
        y_int_2 = ((self.a*self.x2**3)/3)+ ((self.b*self.x2**2)/2)+(self.c*self.x2)+self.d
        print(f'Интеграл c x1 { y_int_1 }')
        print(f'Интеграл c x2 { y_int_2 }')

if __name__ == "__main__":

    print('Введите через enter a,b,c,d')
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())


    
        



