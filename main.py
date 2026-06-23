# ==========================================
# GENERADOR SEGURO DE CONTRASEÑAS
# Autor: David Brito Toapanta
# Asignatura: Lógica de Programación
# ==========================================

import random
import string


def generar_contrasena(longitud, mayusculas, minusculas, numeros, simbolos):
    caracteres = ""

    if mayusculas:
        caracteres += string.ascii_uppercase

    if minusculas:
        caracteres += string.ascii_lowercase

    if numeros:
        caracteres += string.digits

    if simbolos:
        caracteres += string.punctuation

    contrasena = ""

    for i in range(longitud):
        contrasena += random.choice(caracteres)

    return contrasena


def seleccionar_caracteres():
    while True:
        print("\nSeleccione los tipos de caracteres:")

        usar_mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == "s"
        usar_minusculas = input("¿Incluir minúsculas? (s/n): ").lower() == "s"
        usar_numeros = input("¿Incluir números? (s/n): ").lower() == "s"
        usar_simbolos = input("¿Incluir símbolos especiales? (s/n): ").lower() == "s"

        if usar_mayusculas or usar_minusculas or usar_numeros or usar_simbolos:
            return usar_mayusculas, usar_minusculas, usar_numeros, usar_simbolos
        else:
            print("\nError: debe seleccionar al menos un tipo de carácter.")


def main():
    print("=" * 50)
    print("GENERADOR SEGURO DE CONTRASEÑAS")
    print("=" * 50)

    while True:
        longitud = int(input("\nIngrese la longitud de la contraseña: "))

        if longitud < 8:
            print("La longitud mínima recomendada es 8 caracteres.")
        else:
            mayusculas, minusculas, numeros, simbolos = seleccionar_caracteres()

            contrasena = generar_contrasena(
                longitud,
                mayusculas,
                minusculas,
                numeros,
                simbolos
            )

            print("\nContraseña generada:")
            print(contrasena)

        continuar = input("\n¿Desea generar otra contraseña? (s/n): ").lower()

        if continuar != "s":
            print("\nPrograma finalizado.")
            break


main()
