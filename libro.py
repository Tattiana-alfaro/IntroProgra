import xlrd 

path = "TestData//libros.xlsx"
wb = xlrd.open_workbook(path)
sheet = wb.sheet_by_index(0)
miLista = []


class Libro:
    idLibro = ""
    nombre = ""
    genero = ""
    autor = ""

    def __init__(self, idLibro, nombre, genero, autor):
        self.idLibro = idLibro
        self.nombre = nombre
        self.genero = genero
        self.autor = autor

def cargarListaLibros():
    for i in range(sheet.nrows):
        libro = Libro(sheet.cell_value(i, 0), sheet.cell_value(i, 1), sheet.cell_value(i, 2), sheet.cell_value(i, 3))
        miLista.append(libro)
    return miLista

def imprirListaLibro():
    for Libro in cargarListaLibros():
        print(Libro.idLibro, " - ", Libro.nombre, " - ", Libro.genero, " - ", Libro.autor)

