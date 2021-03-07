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

def cargarListaPersonas():
    for i in range(sheet.nrows):
        persona = Persona(sheet.cell_value(i, 0), sheet.cell_value(i, 1), sheet.cell_value(i, 2))
        miLista.append(persona)
    return miLista

def imprirListaPersona():
    miLista = cargarListaPersonas
    for Persona in miLista():
        print(Persona.codigo, " - ", Persona.nombre, " - ", Persona.correo)

def ordenarListaPersonas(opcion):
    #Lista ordenada ascendente
    miLista = cargarListaPersonas()
    if (opcion == 1):
        sortedList = sorted(miLista, str(key=attrgetter(1)))
    else:
        sortedList = sorted(miLista, key=attrgetter(1), reverse= True)
    
    for Persona in sortedList():
        print(Persona.codigo, " - ", Persona.nombre, " - ", Persona.correo)    

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
    attributo = ""
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

    