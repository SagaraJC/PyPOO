from cosas import Alumno
from cosas import Perro

def main():
    al1 = Alumno("Jose", 19, "ICO")
    print(vars(al1))
    al1.__nombre = "Diego"
    print(vars(al1))
    al1.set_nombre("María")
    print(vars(al1))
    print("----------- To String")
    print(al1)
    al1.set_edad(9999)
    print(al1)
    al1.estudiar(4)
    print("----------- Perro")
    perro1 = Perro("Poodle", 2, 0.35)
    print(vars(perro1))
    perro1.raza = "de la calle" #Set en notación pythonic
    print(vars(perro1))
    print(perro1)

    cachorro = Perro.es_cachorro(perro1.edad)
    print(cachorro)

    Perro.dormir()
    danes = Perro.perro_grande(0.8)
    print(danes)
main()