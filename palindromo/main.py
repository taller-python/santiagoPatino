""" Ejercicio para definir si una palabra ingresada por consola es palindroma """

def es_palindroma(word):
    """ Retorna falso o verdadero dependiendo si la palabra es palindroma """
    return word[::-1] == word

print(es_palindroma(input('Ingrese una palabra: ')))
