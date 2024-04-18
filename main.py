
# Integrantes

# Carlos Daniel Gómez Aguilar - 1506323
# Josué David Bautista Orózco

from binary_search_tree import BinarySearchTree


# Abre el archivo en modo de lectura ('r')
with open('mayda cayo.txt', 'r') as file:
    # Lee todo el contenido del archivo
    contenido = file.read()
    print(contenido)
    print('leyendo archivo', file.name)


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


def main():
    # Ejemplo de uso
    texto1 = "hola"
    texto2 = "perro"
    print(comparar_alfabeticamente(texto1, texto2))  # Salida: hola va primero

    texto3 = "holav"
    texto4 = "holato"
    print(comparar_alfabeticamente(texto3, texto4))  # Salida: holap va primero


main()
