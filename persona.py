import xlrd 
from operator import itemgetter, attrgetter

path = "TestData//personas.xlsx"
wb = xlrd.open_workbook(path)
sheet = wb.sheet_by_index(0)
miLista = []
sortedList = []

class Persona:
    codigo = ""
    nombre = ""
    correo = ""

    def __init__(self, codigo, nombre, correo):
        self.codigo = codigo
        self.nombre = nombre
        self.correo = correo

#Funcion para cargar la lista de personas
def cargarListaPersonas():
    for i in range(sheet.nrows):
        persona = Persona(sheet.cell_value(i, 0), sheet.cell_value(i, 1), sheet.cell_value(i, 2))
        miLista.append(persona)
    return miLista

#Funcion para imprimir la lista de personas
def imprirListaPersona():
    miLista = cargarListaPersonas
    for Persona in miLista():
        print(Persona.codigo, " - ", Persona.nombre, " - ", Persona.correo)

# Funcion para ordenar lista de personas por NOMBRE
def ordenarListaPersonas(orden):
    #Lista ordenada ascendente
    miLista = cargarListaPersonas()
    miLista.sort(key=lambda x: x.nombre, reverse=False)
    if (orden == 1):
        miLista.sort(key=lambda x: x.nombre, reverse=False)
    else:
        miLista.sort(key=lambda x: x.nombre, reverse=True)
    
    for Persona in miLista:
        print(Persona.codigo, " - ", Persona.nombre, " - ", Persona.correo)   
    
    miLista.clear()

#Funcion para buscar personas.
def buscarPersona():

    encontrado = False
    texto = """
    Por cual atributo le gustaria buscar
    1. Codigo
    2. Nombre
    3. Correo
    """
    print(texto)
    opcion = input("Digite una opcion: ")
    miLista = cargarListaPersonas()
    if (int(opcion) == 1):
        attributo = input("Digite el codigo que desea buscar: ")
        for Persona in miLista:
            if str(attributo.capitalize()) in str(Persona.codigo).capitalize():
                encontrado = True
                print("Se ha encontrado el siguiente registro: ")
                print("CODIGO: ", Persona.codigo) 
                print("NOMBRE: ", Persona.nombre) 
                print("CORREO: ", Persona.correo) 
        
    if (int(opcion) == 2):
        attributo = input("Digite el nombre que desea buscar: ")
        for Persona in miLista:
            if str(attributo.capitalize()) in str(Persona.nombre).capitalize():
                encontrado = True
                print("Se ha encontrado el siguiente registro: ")
                print("CODIGO: ", Persona.codigo) 
                print("NOMBRE: ", Persona.nombre) 
                print("CORREO: ", Persona.correo) 

    if (int(opcion) == 3):
        attributo = input("Digite el correo que desea buscar: ")
        for Persona in miLista:
            if str(attributo.capitalize()) in str(Persona.correo).capitalize():
                encontrado = True
                print("Se ha encontrado el siguiente registro: ")
                print("CODIGO: ", Persona.codigo) 
                print("NOMBRE: ", Persona.nombre) 
                print("CORREO: ", Persona.correo) 
    else:
        if encontrado == False:
            print("No se ha encontrado ninguna coincidencia")
    miLista.clear()

    