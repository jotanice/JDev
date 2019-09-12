# -*- coding: utf-8 -*-
# Faça um programa que receba duas notas digitadas pelo usuário. 
# Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.
from statistics import *
nota1 = input("Digite sua primeira nota: ");
nota2 = input("Digite sua segunda nota: ");
lista = [int(nota1),int(nota2)];
#print(lista)

def media(lista):
    return mean(lista)

media = media(lista)

print("Sua média é: "+str(media))

if media >= 6:
    print("Você foi APROVADO!")
else:
    print("Você foi REPROVADO!")