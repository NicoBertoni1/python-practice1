"""Strings"""


"""
Formatear las siguientes variables de tipo string en un único string.
Restricción: Utilizar el operador +.
"""

variable_01 = "¡Buenos "
variable_02 = "días "
variable_03 = "a todos!"

variable_01 = "¡Buenos "
variable_02 = "días "
variable_03 = "a todos!"

strings_concatenados == concatenar(variable_01, variable_02, variable_03)

assert strings_concatenados == "¡Buenos días a todos!"


"""
Formatear los siguientes strings en un único string.
Restricción: Usar directamente los strings y la concatenación automática (no
usar operadores).
"""

# "¡Mamá "
# "estoy concatenando "
# "strings!"

variable1 = "!Mamá "
varibale2 = "estoy concatenando "
variable3 = " strings"

strings_concatenados == concatenar(variable1, variable2, variable3)
print(strings_concatenados)

assert strings_concatenados == "¡Mamá estoy concatenando strings!"


"""
Formatear las siguientes variables en un único string.
Aclaración: Se debe convertir la variable entera a string
Restricción: Utilizar el operador +.
"""

variable_01 = "Le debo "
variable_02 = 600
variable_03 = " pesos a un amigo."

variable2 = int(variable_02)

strings_concatenados == concatenar(variable_01, variable2, variable_03)
print(strings_concatenados)

assert strings_concatenados == "Le debo 600 pesos a un amigo."


"""
Formatear las siguientes variables en un único string.
Aclaración: No es necesario realizar conversiones de tipo.
Restricción: Utilizar el método format.
"""

variable_01 = "Le debo "
variable_02 = 6
variable_03 = " pesos a un amigo hace "
variable_04 = " años."
variable_05 = "Ezequiel"

strings_concatenados == concatenar(variable_01, str(variable_02), variable_03, variable_04, str(variable_05))
print(strings_concatenados)

assert (
    strings_concatenados == "Le debo 6 pesos a un amigo hace 6 años. Se llama Ezequiel"
)


"""
Formatear las siguientes variables en un único string.
Restricción: Utilizar f-Strings.
"""

variable_01 = "Le pagué "
variable_02 = 2
variable_03 = " pesos que le debía a Ezequiel, me faltan $"
variable_04 = 4

strings_concatenados ==({}{}{}{} .format(variable_01, str(



assert strings_concatenados == "Le pagué 2 pesos que le debía a Ezequiel, me faltan $4"
