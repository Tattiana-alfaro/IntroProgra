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

def buscarLibro():

    encontrado = False
    texto = """
    Por cual atributo le gustaria buscar
    1. Codigo Libro
    2. Nombre
    3. Genero
    4. Autor
    """
    print(texto)
    opcion = input("Digite una opcion: ")
    miLista = cargarListaLibros()
    if (int(opcion) == 1):
        attributo = input("Digite el codigo que desea buscar: ")
        for Libro in miLista:
            if str(attributo.capitalize()) in str(Libro.idLibro).capitalize():
                encontrado = True
                print("Se ha encontrado el siguiente registro: ")
                print("CODIGO: ", Libro.idLibro) 
                print("NOMBRE: ", Libro.nombre) 
                print("GENERO: ", Libro.genero) 
                print("AUTOR: ", Libro.autor) 
        
    if (int(opcion) == 2):
        attributo = input("Digite el nombre que desea buscar: ")
        for Libro in miLista:
            if str(attributo.capitalize()) in str(Libro.nombre).capitalize():
                encontrado = True
                print("Se ha encontrado el siguiente registro: ")
                print("CODIGO: ", Libro.idLibro) 
                print("NOMBRE: ", Libro.nombre) 
                print("GENERO: ", Libro.genero) 
                print("AUTOR: ", Libro.autor) 
        

    if (int(opcion) == 3):
        attributo = input("Digite el genero que desea buscar: ")
        for Libro in miLista:
            if str(attributo.capitalize()) in str(Libro.genero).capitalize():
                encontrado = True
                print("Se ha encontrado el siguiente registro: ")
                print("CODIGO: ", Libro.idLibro) 
                print("NOMBRE: ", Libro.nombre) 
                print("GENERO: ", Libro.genero) 
                print("AUTOR: ", Libro.autor) 

    if (int(opcion) == 4):
        attributo = input("Digite el autor que desea buscar: ")
        for Libro in miLista:
            if str(attributo.capitalize()) in str(Libro.autor).capitalize():
                encontrado = True
                print("Se ha encontrado el siguiente registro: ")
                print("CODIGO: ", Libro.idLibro) 
                print("NOMBRE: ", Libro.nombre) 
                print("GENERO: ", Libro.genero) 
                print("AUTOR: ", Libro.autor) 
        
    else:
        if encontrado == False:
            print("No se ha encontrado ninguna coincidencia")
    miLista.clear()