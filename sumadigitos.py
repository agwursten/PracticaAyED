# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 11:30:52 2022

@author: alumno
"""

def suma_digito(numero):
    if (numero == 0):
        return 0
    else: 
        return suma_digito(numero//10) + numero % 10
    
print(suma_digito(280))