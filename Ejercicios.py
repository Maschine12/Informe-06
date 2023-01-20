# - Realizar operaciones de unión, intersección y diferencia
# de conjuntos
# - Calcular la diferencia entre dos conjuntos
# - Calcular la diferencia simétrica entre 3 conjuntos


"""
1.-
"""
# Union
import random as rm


# Datos conjuntos , minimo valor , maximo valor
def generador_Conjuntos(datos_conjunto, minimo, Maximo):
    lista_datos = []
    for i in range(datos_conjunto):
        a = rm.randint(minimo, Maximo)
        lista_datos.append(a)
    # Conviertiendo a tupla
    tupla_A = tuple(lista_datos)
    # Convirtiendo a conjunto
    Z = set(tupla_A)
    return Z
# union de conjuntos


def union_conjuntos(A, B, C):
    D = A | B | C
    return D
# interseccion de conjuntos


def interseccion_conjuntos(A, B, C):
    D = A & B 
    E = D & C
    if E == set():
        return "{}"
    else:
        return E
# Diferencia en orden de entrada


def diferencia(A, B, C):
    D = (A - B) - C
    return D

# diferencia simetrica entre conjuntos


def diferencia_simetrica(A, B, C):
    # C = union_conjuntos(A,B) - interseccion_conjuntos(A,B)
    D = (A ^ B) ^ C
    return D


# Creando conjuntos
A = generador_Conjuntos(20, 10, 30)  # nro de datos , minimo , maximo
B = generador_Conjuntos(20, -20, 20)  # nro de datos , minimo , maximo
C = generador_Conjuntos(10, -5, 18)

print("Conjunto A :", A, "\nConjunto B :", B, "\nConjunto C:", C)

print("Union")
print(union_conjuntos(A, B, C))

print("Interseccion ")
print(interseccion_conjuntos(A, B, C))

print("Diferencia")
print(diferencia(B, A, C))

print("Diferencia simetrica")
print(diferencia_simetrica(A, B, C))