# -*- coding: utf-8 -*-
import aleatorio as a
import media as m

lista = a.glint(2);

media = m.media(lista)
mediana = m.mediana(lista)
moda = m.moda(lista)

print("Minha lista é "+str(lista))
print("A média é "+str(media))
print("A mediana é "+str(mediana))
print("A moda é "+str(moda))