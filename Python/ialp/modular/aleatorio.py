# -*- coding: utf-8 -*-
# GERA LISTA ALEATÓRIA
import random

def glint(tam):
    lista = []
    for i in range(tam):
        lista.append(random.randint(0, tam))
    return lista