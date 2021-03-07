import xlrd 

path = "TestData//libros.xlsx"
wb = xlrd.open_workbook(path)
sheet = wb.sheet_by_index(0)
miLista = []
sortedList = []

class Persona:
    idLibro = ""
    nombre = ""
    genero = ""
    autor = ""

    def __init__(self, idLibro, nombre, correo, autor):
        self.idLibro = idLibro
        self.nombre = nombre
        self.correo = correo
        self.autor = autor

def cargarListaLibros():
    pass



