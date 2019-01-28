# -*- coding: utf-8 -*-
nome = input ("Digite seu nome: "+"\nOu Digite Limpa para apagar o conteúdo do arquivo.")

if nome == "limpa" or nome == "Limpa" or nome == "Limpar":
    A = open ("arq2.txt", "w")
    A.close ()

else:

    v1_str = input ("Digite o valor de x:  ")
    v2_str = input ("Digite o valor de y:  ")

    v1_int = int(v1_str)
    v2_int = int(v2_str)


    def sum(x, y):
        return x + y
    s = sum(v1_int, v2_int)
    def multiply(x, y):
        return x * y
    m = multiply(v1_int, v2_int)

    print (nome)


    if nome == "Joao":
            print (sum(s,m))
            s_str = str(s)
            A = open ("arq2.txt", "a")
            A.write (v1_str+" | "+v2_str+" | "+nome+" | "+s_str+"\n\n")
            A.close ()
    else:
            print (m)
            m_str = str(m)
            A = open ("arq2.txt", "a")
            A.write (v1_str+" | "+v2_str+" | "+nome+" | "+m_str+"\n\n")
            A.close ()