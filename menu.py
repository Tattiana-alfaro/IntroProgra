
import persona
import libro
import os

def menuPrincipal():
    os.system('cls')

    texto = """
    ****************************************
    *          MENU  PRINCIPAL             *
    ****************************************
    
    1. Manejo de Personas
    2. Manejo de Libros
    3. Salir

    ****************************************
 
    """
    return texto

def menuPersonas():
    os.system('cls')

    texto = """
    ****************************************
    *    MENU  SECUNDARIO - PERSONAS       *
    ****************************************
    
    1. Ordernar lista de personas
    2. Imprimir lista de personas
    3. Buscar Persona
    4. Volver al menu principal
    5. Salir

    ****************************************
 
    """
    return texto

def menuLibros():
    os.system('cls')

    texto = """
    ****************************************
    *    MENU  SECUNDARIO - LIBROS         *
    ****************************************
    
    1. Ver Lista de Libros
    2. Buscar Libros
    3. Ver Prestamo de libros
    4. Volver al menu principal
    5. Salir

    ****************************************
 
    """
    return texto

def imprimirOpcionesOrdenLista():
    os.system('cls')

    texto =  """
    ****************************************
    Como desea ordenar la lista?:
    1. Ascedente
    2. Descendete
    ****************************************
    """
    return texto

def manejoMenuPersonas():
    
    print(menuPersonas())
    opcion = int(input("Seleccione una opcion: "))

    
    if(opcion == 1):
        print(imprimirOpcionesOrdenLista)
        opcion = int(input(imprimirOpcionesOrdenLista()))
        if (opcion == 1):
            persona.ordenarListaPersonas(True)
        else:
            persona.ordenarListaPersonas(False)
        # Necesitamos programar la funcionalidad de ordenar lista de personas, esta funcion esta en el modulo de personas.
    
    if(opcion == 2):
        persona.imprirListaPersona()
        
    if(opcion == 3):
        print("PENDIENTE")
    
    if(opcion == 4):
        manejoMenuPrincipal()
    
    if(opcion == 5):
        print("Muchas Gracias!")
        quit
    

def manejoMenuLibros():
    print(menuLibros())
    opcion = int(input("Seleccione una opcion: "))

    if(opcion == 1):
        libro.imprirListaLibro()
    
    if(opcion == 2):
        print("PENDIENTE")
    
    if(opcion == 3):
        print("PENDIENTE")
    
    if(opcion == 4):
        manejoMenuPrincipal()
    
    if(opcion == 5):
        print("Muchas Gracias!")
        quit

def manejoMenuPrincipal():
    print(menuPrincipal())
    opcion = int(input("Seleccione una opcion: "))

    if (opcion == 1):
        manejoMenuPersonas()

    if (opcion == 2):
        manejoMenuLibros()

    if (opcion == 3):
        print("Muchas Gracias!")


