from cosas import Libro
from cosas import Autor
from cosas import Alumno

def main():
    l1 = Libro.libro_planeta("El Perfume", Autor("Patrick", "PS"), 1980)
    print(l1)

    l1.autor.pseudonimo = l1.autor.pseudonimo.lower()
    print(l1)

    print("----Herencia----")
    al1 = Alumno("Jose", 20, "23232", "ICO", 9)
    al1.nombre = "Pepe"
    print(vars(al1))
main()