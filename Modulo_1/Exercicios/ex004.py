# -*- coding: utf-8 -*-

msg = input('Digite algo: ')

print(type(msg))
print('Isso que você digitou é Numérico? ', msg.isnumeric())
print('Isso que você digitou é Alfanumérico? ', msg.isalnum())
print('Isso que você digitou é Alfabético? ', msg.isalpha())
print('Isso que você digitou é Dígito? ', msg.isdigit())
print('Isso que você digitou é Espaço? ', msg.isspace())
print('Isso que você digitou dá pra imprimir? ', msg.isprintable())
print('Isso que você digitou está em caixa baixa? ', msg.islower())
print('Isso que você digitou é Identificável? ', msg.isidentifier())
print('Isso que você digitou está Capitalizado? ', msg.istitle())