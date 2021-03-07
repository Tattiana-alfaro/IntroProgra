import xlrd 

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
    for Persona in cargarListaPersonas():
        print(Persona.codigo, " - ", Persona.nombre, " - ", Persona.correo)

def ordenarListaPersonas(ascendente):
    #Lista ordenada ascendente
    if (ascendente):
        sortedList = sorted(cargarListaPersonas())
    else:
        sortedList = sorted(cargarListaPersonas(), reverse=True)    
    for i in range(len(sortedList)):
        print(sortedList[i])
