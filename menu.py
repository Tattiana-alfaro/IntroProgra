
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

# Funcion para desplegar las opciones de volver al menu anterior
# Recibe por parametro el valor para determinar si regresa al menu de libro o al menu de personas
def imprimirVolveralmMenuAnterior(menuPadre):
    opcion = input("Desea volver al menu anterior (Y/N)?: ")

    if opcion.capitalize() == "Y":
        if menuPadre == 1:
            manejoMenuPersonas()
        if menuPadre == 2:
            manejoMenuLibros()
    else:
        print("Muchas Gracias!")
        quit


def manejoMenuPersonas():
    
    print(menuPersonas())
    opcion = int(input("Seleccione una opcion: "))

    #Opcion: Ordenar lista de personas
    if(opcion == 1):
        
        print(imprimirOpcionesOrdenLista)
        orden = int(input(imprimirOpcionesOrdenLista()))
        persona.ordenarListaPersonas(orden)
        #La siguiente funcion despliega las opciones para volver al menu anterior. 1 - Menu de Personas / 2 - Menu de Libros
        imprimirVolveralmMenuAnterior(1)

    # Opcion: Imprimir lista de personas    
    if(opcion == 2):        
        persona.imprirListaPersona()
        #La siguiente funcion despliega las opciones para volver al menu anterior. 1 - Menu de Personas / 2 - Menu de Libros
        imprimirVolveralmMenuAnterior(1)

    # Opcion: Buscar Persona    
    if(opcion == 3):        
        persona.buscarPersona()
        #La siguiente funcion despliega las opciones para volver al menu anterior. 1 - Menu de Personas / 2 - Menu de Libros
        imprimirVolveralmMenuAnterior(1)
    
    #Opcion: Volver al Menu principal
    if(opcion == 4):
        manejoMenuPrincipal()
    
    #Opcion: Salir del sistema
    if(opcion == 5):
        print("Muchas Gracias!")
        quit
    

def manejoMenuLibros():
    os.system('cls')
    print(menuLibros())
    opcion = int(input("Seleccione una opcion: "))

    # Opcion: Ver Lista de libros
    if(opcion == 1):
        libro.imprirListaLibro()
        #La siguiente funcion despliega las opciones para volver al menu anterior. 1 - Menu de Personas / 2 - Menu de Libros
        imprimirVolveralmMenuAnterior(2)
    
    # Opcion: Buscar Libros
    if(opcion == 2):
        libro.buscarLibro()
        #La siguiente funcion despliega las opciones para volver al menu anterior. 1 - Menu de Personas / 2 - Menu de Libros
        imprimirVolveralmMenuAnterior(2)
    
    # Opcion Ver Prestamo de libros
    if(opcion == 3):
        libro.cargardisponibilidad()
        #La siguiente funcion despliega las opciones para volver al menu anterior. 1 - Menu de Personas / 2 - Menu de Libros
        imprimirVolveralmMenuAnterior(2)
    
    #Opcion Volver al menu princpial
    if(opcion == 4):
        manejoMenuPrincipal()
    
    #Opcion para salir del sistema
    if(opcion == 5):
        print("Muchas Gracias!")
        quit

# Funcion manejar las opciones del menu principal.
def manejoMenuPrincipal():
    print(menuPrincipal())
    opcion = int(input("Seleccione una opcion: "))
    # Despliega el menu de personas.
    if (opcion == 1):
        manejoMenuPersonas()

    #Despliega el menu de libros.
    if (opcion == 2):
        manejoMenuLibros()

    #Opcion de salir.
    if (opcion == 3):
        print("Muchas Gracias!")


