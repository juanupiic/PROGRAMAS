# -*- coding: utf-8 -*-
"""Algoritmo_ Escalada _Simple _y_ Primero _Mejor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-XCuaAWNZKhSRmgJ30Edq70qZJKBrgqr

NOMBRE: LUIS FERNANDO GALEANO MARTINEZ
MATERIA: Fundamentos de inteligencia artificial
introduccion: El código proporcionado implementa dos algoritmos de resolución para el problema del viajero Escalada Simple  y Primero el Mejor. El problema del viajero consiste en encontrar la ruta más corta que visite todas las ciudades proporcionadas una vez y regrese al punto de partida.
Conclusiones:El algoritmo de Escalada Simple busca mejorar iterativamente una solución inicial, seleccionando vecinos y moviéndose hacia el vecino que minimiza la distancia total. El proceso se repite hasta que no se puede mejorar más la solución actual.
El algoritmo de Primero el Mejor utiliza una estrategia de búsqueda en la que explora y expande los nodos según la distancia total, priorizando siempre el nodo con la menor distancia. Este enfoque puede ser más exhaustivo pero computacionalmente costoso.
Bibliografía: Russell, S., & Norvig, P. (2010). Artificial Intelligence: A Modern
Approach (3rd ed.). Pearson.
ECHO POR EL EQUIPO DE: LUIS FERNANDO GALEANO MARTINEZ  Y JUAN MANUEL GALINDO CORTES
"""

import math
import random

# Definición del problema del viajero
class TSP:
    def __init__(self, ciudades):
        self.ciudades = ciudades

    def distancia(self, ciudad1, ciudad2):
        x1, y1 = self.ciudades[ciudad1]
        x2, y2 = self.ciudades[ciudad2]
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    def distancia_total(self, ruta):
        distancia_total = 0
        for i in range(len(ruta) - 1):
            distancia_total += self.distancia(ruta[i], ruta[i + 1])
        distancia_total += self.distancia(ruta[-1], ruta[0])  # Volver a la primera ciudad
        return distancia_total

# Algoritmo de Escalada Simple (Hill Climbing)
def escalada_simple(tsp, ruta_inicial):
    mejor_ruta = ruta_inicial
    mejor_distancia = tsp.distancia_total(mejor_ruta)

    while True:
        vecinos = generar_vecinos(mejor_ruta)
        mejor_vecino = min(vecinos, key=lambda x: tsp.distancia_total(x))

        if tsp.distancia_total(mejor_vecino) < mejor_distancia:
            mejor_ruta = mejor_vecino
            mejor_distancia = tsp.distancia_total(mejor_vecino)
        else:
            break

    return mejor_ruta, mejor_distancia

# Algoritmo de Primero el Mejor (Best-First Search)
def primero_el_mejor(tsp, ruta_inicial):
    frontera = [ruta_inicial]
    explorado = set()

    while frontera:
        ruta_actual = frontera.pop(0)

        if tuple(ruta_actual) not in explorado:
            explorado.add(tuple(ruta_actual))
            vecinos = generar_vecinos(ruta_actual)

            for vecino in vecinos:
                if tuple(vecino) not in explorado:
                    frontera.append(vecino)

            frontera.sort(key=lambda x: tsp.distancia_total(x))

    mejor_ruta = explorado.pop()
    mejor_distancia = tsp.distancia_total(mejor_ruta)

    return mejor_ruta, mejor_distancia

# Función auxiliar para generar vecinos intercambiando dos ciudades aleatorias
def generar_vecinos(ruta):
    vecinos = []

    for i in range(len(ruta) - 1):
        for j in range(i + 1, len(ruta)):
            vecino = ruta[:i] + [ruta[j]] + ruta[i + 1:j] + [ruta[i]] + ruta[j + 1:]
            vecinos.append(vecino)

    return vecinos

# Ejemplo de uso
ciudades = {
    0: (0, 0),
    1: (1, 2),
    2: (3, 1),
    3: (5, 2),
    4: (6, 0)
}

problema_viajero = TSP(ciudades)
ruta_inicial = [0, 1, 2, 3, 4]

# Escalada Simple
solucion_escalada_simple, distancia_escalada_simple = escalada_simple(problema_viajero, ruta_inicial)
print("Escalada Simple:")
print("Ruta:", solucion_escalada_simple)
print("Distancia:", distancia_escalada_simple)
print()

# Primero el Mejor
solucion_primero_el_mejor, distancia_primero_el_mejor = primero_el_mejor(problema_viajero, ruta_inicial)
print("Primero el Mejor:")
print("Ruta:", solucion_primero_el_mejor)
print("Distancia:", distancia_primero_el_mejor)

import matplotlib.pyplot as plt

def visualizar_ciudades(ciudades, titulo):
    x = [ciudades[i][0] for i in ciudades]
    y = [ciudades[i][1] for i in ciudades]

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, c='red', marker='o')
    plt.title(titulo)
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')

    for ciudad, coordenadas in ciudades.items():
        plt.annotate(str(ciudad), (coordenadas[0], coordenadas[1]), textcoords="offset points", xytext=(0, 5), ha='center')

    plt.show()

def visualizar_ruta(ciudades, ruta, titulo):
    x = [ciudades[i][0] for i in ruta]
    y = [ciudades[i][1] for i in ruta]

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker='o', linestyle='-', color='blue')
    plt.title(titulo)
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')

    for ciudad, coordenadas in ciudades.items():
        plt.annotate(str(ciudad), (coordenadas[0], coordenadas[1]), textcoords="offset points", xytext=(0, 5), ha='center')

    plt.show()

# Visualizar ciudades y soluciones
visualizar_ciudades(ciudades, "Ubicación de Ciudades")

# Escalada Simple
visualizar_ruta(ciudades, solucion_escalada_simple, "Escalada Simple - Ruta Óptima")

# Primero el Mejor
visualizar_ruta(ciudades, solucion_primero_el_mejor, "Primero el Mejor - Ruta Óptima")



import math

# Función objetivo (puede ser modificada según el problema)
def funcion_objetivo(x):
    return -x**2  # Encontrar el máximo de la función -x^2



# Algoritmo de Escalada Simple
def escalada_simple(func_objetivo, punto_inicial, paso=0.1, max_iter=100):
    punto_actual = punto_inicial

    for _ in range(max_iter):
        valor_actual = func_objetivo(punto_actual)
        punto_siguiente = punto_actual + paso
        valor_siguiente = func_objetivo(punto_siguiente)

        if valor_siguiente > valor_actual:
            punto_actual = punto_siguiente
        else:
            break

    return punto_actual, func_objetivo(punto_actual)

# Algoritmo de Primero el Mejor (Best-First Search)
def primero_el_mejor(func_objetivo, punto_inicial, paso=0.2, max_iter=100):
    frontera = [(punto_inicial, func_objetivo(punto_inicial))]

    for _ in range(max_iter):
        punto_actual, _ = frontera.pop(0)
        punto_siguiente = punto_actual + paso
        valor_siguiente = func_objetivo(punto_siguiente)
        frontera.append((punto_siguiente, valor_siguiente))
        frontera.sort(key=lambda x: x[1], reverse=True)

    mejor_punto, mejor_valor = frontera[0]
    return mejor_punto, mejor_valor

# Ejemplo de uso
punto_inicial = 2.0

# Escalada Simple
resultado_escalada_simple = escalada_simple(funcion_objetivo, punto_inicial)
print("Escalada Simple:", resultado_escalada_simple)

# Primero el Mejor
resultado_primero_el_mejor = primero_el_mejor(funcion_objetivo, punto_inicial)
print("Primero el Mejor:", resultado_primero_el_mejor)