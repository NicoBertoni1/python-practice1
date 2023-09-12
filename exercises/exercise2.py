"""Lógica Simple y Cortocircuito"""


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si al menos una de las variables es True.
"""

esta_lloviendo = True
riego_activado = True

if (esta_lloviendo = True and riego_activado = True):
  print(piso_mojado)
elif(esta_lloviendo = True and riego_activado = False):
  print(piso_mojado)
elif (esta_lloviendo = False and riego_activado = True):
  print(piso_mojado)
else:
  print(no esta mojado)

assert piso_mojado


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si el área es mayor a 5.
Restricción: Usar NOT.
"""

lado_cuadrado = 5
area_cuadrado = pow(lado_cuadrado, 2)

if (area_cuadrado > 5):
  area_mayor_a_cinco = True

assert area_mayor_a_cinco


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si el número 1 es divisible por 7 y al mismo tiempo el número 2 no lo es.
"""

numero_1 = 49
numero_2 = 50
resto = 0

if (numero_1 / 7 = resto) and (numero_2 / 7 != resto):
  print(True)


assert resultado


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
el mismo valor de la variable 3.
Restricción: sólo usar OR, NOT y el mecanismo de cortocircuito.
"""

variable_01 = False
variable_02 = True
variable_03 = 80
variable_04 = "90"
variable_05 = 100

# COMPLETAR - INICIO

# COMPLETAR - FIN

assert resultado == 80
