# -*- coding: utf-8 -*-
# Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.
idade = input ("Digite sua idade: ")
print (idade)

if int(idade) >= 18:
    print("Você é maior de idade.")

else:
    print("Você é menor de idade.")