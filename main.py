# ==========================================
# GENERADOR SEGURO DE CONTRASEÑAS
# Autor: David Brito Toapanta
# Asignatura: Lógica de Programación
# ==========================================

import random
import string


def generar_contrasena(longitud, mayusculas, minusculas, numeros, simbolos):

    caracteres = ""

    # Agregar tipos de caracteres seleccionados
    if mayusculas:
        caracteres += string.ascii_uppercase

    if minusculas:
        caracteres += string.ascii_lowercase

    if numeros:
        caracteres += string.digits

    if simbolos:
        caracteres += string.punctuation

    # Validar que exista al menos un tipo de carácter
    if len(caracteres) == 0:
        return None

    contrasena = ""

    # Generar contraseña utilizando un ciclo repetitivo
    for i in range(longitud):
        contrasena += random.choice(caracteres)

    return contrasena


print("=" * 50)
print("GENERADOR SEGURO DE CONTRASEÑAS")
print("=" * 50)

# Solicitar longitud
longitud = int(input("Ingrese la longitud de la contraseña: "))

# Validar longitud mínima
if longitud < 8:
    print("\nLa longitud mínima recomendada es 8 caracteres.")
else:

    print("\nSeleccione los tipos de caracteres:")

    usar_mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == "s"
    usar_minusculas = input("¿Incluir minúsculas? (s/n): ").lower() == "s"
    usar_numeros = input("¿Incluir números? (s/n): ").lower() == "s"
    usar_simbolos = input("¿Incluir símbolos especiales? (s/n): ").lower() == "s"

    contrasena = generar_contrasena(
        longitud,
        usar_mayusculas,
        usar_minusculas,
        usar_numeros,
        usar_simbolos
    )

    if contrasena:
        print("\nContraseña generada:")
        print(contrasena)
    else:
        print("\nError: Debe seleccionar al menos un tipo de carácter.")

print("\nPrograma finalizado.")
