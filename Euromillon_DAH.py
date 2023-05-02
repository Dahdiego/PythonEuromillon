# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 09:53:08 2021

@author: DiegoAlonsoHernando
"""

import LibEuromillon_DAH

#Listas vacías
listanumeros=[]
listaestrellas=[]
listaresnum=[]
listaresest=[]

x=0
v=0
y=0
a=0
print("Euromillón de Diego Alonso Hernando")
print()
#Boleto inicial
print ("BIENVENIDO AL EUROMILLÓN")
print("--------------------")
print("| 1 10 19 28 37 46 |")
print("| 2 11 20 29 38 47 |")
print("| 3 12 21 30 39 48 |")
print("| 4 13 22 31 40 49 |")
print("| 5 14 23 32 41 50 |")
print("| 6 15 24 33 42    |")
print("| 7 16 25 34 43    |")
print("| 8 17 26 35 44    |")
print("| 9 18 27 36 45    |")
print("--------------------")
print("| 1 5 9  |")
print("| 2 6 10 |")
print("| 3 7 11 |")
print("| 4 8 12 |")
print("---------------------------------------------------------")
print("POR FAVOR SELECCIONE 5 NÚMEROS Y 2 ESTRELLAS PARA JUGAR")
print("---------------------------------------------------------")

#Llamada a la función para seleccionar los números
LibEuromillon_DAH.pedirNum(x, listanumeros)

#Llamada a la función para seleccionar las estrellas
LibEuromillon_DAH.pedirEstr(v, listaestrellas)

#Llamada a la función para que salga el boleto con los números tachados
LibEuromillon_DAH.marcarNum(listanumeros)

#Llamada a la función para que salga el boleto con las estrellas tachadas
LibEuromillon_DAH.marcarEstr(listaestrellas)

#Llamada a la función para generar los números y estrellas ganadoras
LibEuromillon_DAH.generarGanadores(y, a, listaresnum, listaresest)

#Llamada a la función para mostrar tus números y estrellas acertadas y dar el premio final.
LibEuromillon_DAH.darPremios(listanumeros, listaestrellas, listaresnum, listaresest)







