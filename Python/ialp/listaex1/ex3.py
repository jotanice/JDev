# -*- coding: utf-8 -*-
# Escreva um programa que resolva uma equação de segundo grau.
# ax² + bx + c = 0
# (-b +- sqtr(b²-4ac))/2

from math import sqrt

a = input("Digite o valor de a: ")
b = input("Digite o valor de b: ")
c = input("Digite o valor de c: ")

delta = int(b)**2 - (4*int(a)*int(c))
raiz_delta = sqrt(delta)

x1 = (-int(b) + raiz_delta)/(2*int(a))
x2 = (-int(b) - raiz_delta)/(2*int(a))

print ("x1 = %d" %x1)
print ("x2 = %d" %x2)