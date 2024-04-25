
# Integrantes

# Carlos Daniel Gómez Aguilar - 1506323
# Josué David Bautista Orózco - 1532523

from binary_search_tree import BinarySearchTree
import os


arbol_indexador = BinarySearchTree()


def leer_archivos():
    # Obtener la lista de archivos en el directorio actual
    archivos = os.listdir('.')

    # Iterar sobre cada archivo en la lista
    for archivo in archivos:
        # Verificar si el archivo es un archivo regular (no un directorio)
        if os.path.isfile(archivo) and archivo.endswith('.txt'):
            # Abre el archivo
            with open(archivo) as archivo_leer:

                '''# Lee todo el contenido del archivo
                contenido = archivo_leer.read()
                print(contenido)'''

                for lineas in archivo_leer:

                    split = lineas.split()
                    for i in split:
                        arbol_indexador.insert((i.lower()))

                '''print('Leyendo archivo:', archivo_leer.name)'''


def comparar_alfabeticamente(texto1, texto2):
    palabras1 = texto1.split()
    palabras2 = texto2.split()

    for palabra1, palabra2 in zip(palabras1, palabras2):
        if palabra1 < palabra2:
            return f"{texto1} va primero"
        elif palabra1 > palabra2:
            return f"{texto2} va primero"

    # Si las palabras son iguales hasta el momento,
    # se determina por la longitud total del texto
    if len(texto1) < len(texto2):
        return f"{texto1} va primero"
    elif len(texto1) > len(texto2):
        return f"{texto2} va primero"
    else:
        return "Ambos textos son iguales en términos alfabéticos"


def mostrar_info_palabra(palabra):
    apariciones = {}
    for archivo in os.listdir('.'):
        if os.path.isfile(archivo) and archivo.endswith('.txt'):
            with open(archivo) as archivo_leer:
                veces_en_archivo = 0
                for linea in archivo_leer:
                    palabras_linea = linea.split()
                    veces = palabras_linea.count(palabra)
                    veces_en_archivo += veces
                if veces_en_archivo > 0:
                    if palabra not in apariciones:
                        apariciones[palabra] = {"archivos": [], "veces": []}
                    apariciones[palabra]["archivos"].append(archivo)
                    apariciones[palabra]["veces"].append(veces_en_archivo)

    if palabra in apariciones:
        archivos = ", ".join(apariciones[palabra]["archivos"])
        veces = ", ".join(map(str, apariciones[palabra]["veces"]))
        print(f"Palabra: {palabra}\n"
              f"Archivos: ({archivos})\n"
              f"Veces: ({veces})")
    else:
        print("La palabra no se encuentra en ningún archivo.")


def main():
    leer_archivos()
    while True:
        print("\nMenú:")
        print("1. Ver árbol binario de búsqueda")
        print("2. Mostrar información sobre una palabra")
        print("3. Salir")

        opcion = input("Ingrese el número de la opción que desea ejecutar: ")

        if opcion == "1":
            print("\nÁrbol binario de búsqueda:")
            inorder = arbol_indexador.inorder()
            print(inorder)
        elif opcion == "2":
            palabra = input("Ingrese la palabra de la que desea ver información: ")
            mostrar_info_palabra(palabra.lower())
        elif opcion == "3":
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción inválida. Por favor, ingrese una opción válida.")


main()
