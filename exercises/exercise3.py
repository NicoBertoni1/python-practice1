"""Comparación"""

"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si 2 personas tienen el mismo nombre pero distinta edad.
Aclaración: Se puede utilizar and, or y not.
"""

persona1 = "Kevin"
edad1 = 24
persona2 = "Kevin"
edad2 = 41

if (persona1 = persona2) and (edad1 != edad2):
  comparar_nombre_y_edad = True

assert comparar_nombre_y_edad


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si un auto no es de marca Ford y su modelo es igual o anterior al año 2000.
Aclaración: Se puede utilizar and, or y not.
"""

marca_del_auto = "Chevrolet"
modelo_de_auto = 1998

if  (marca-del_auto != "Ford") and (modelo_del_auto =< 2000):
  comparar_marca_y_modelo = True

assert comparar_marca_y_modelo


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si la superfice del campo 1 es menor a la del campo 2 y la superficie del
campo 2 es mayor a la del campo 3.
Restricción: Utilizar comparaciones encadenadas - No utilizar and, or ni not.
"""

campo1 = 85121
campo2 = 851212
campo3 = 8512

if (cammpo1 < campo2):
  elif (campo2 > campo3):
    comparar_superficie = True
else: 
    comparar_superficie = False

assert comparar_superficie


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si la cantidad de bananas es menor a la mitad de la cantidad de naranjas,
la mitad de naranjas es menor a dos veces la cantidad de manzanas y dos veces
la cantidad de manzanas es menor o igual a la cantidad de peras al cuadrado.
Restricción: Utilizar comparaciones encadenadas y no utilizar and, or ni not.
"""

bananas = 100
naranjas = 400
manzanas = 300
peras = 30

if (bananas < naranjas /2):
 elif( naranjas /2 < manzanas *2):
 elif(manzanas *2 <= peras **2):
  comparar_frutas = True
else:
comparar_frutas = False


assert comparar_frutas
