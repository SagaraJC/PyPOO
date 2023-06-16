from cosas import *

def main():
    per1 = Persona("José", 19)
    print(per1)
    print(Persona.descripcion)

    print("Herencia Alumno-------------------")
    al1 = Alumno("José", 19, "2344598", "ICO")
    print(al1)
    print(Alumno.descripcion)

    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "Juan"
    print(al2)
    al2.dormir()

    print("Herencia Profesor-----------------")
    profe1 = Profesor("Jesús", 30+16, 2684, "Ingeniería de Software")
    print(profe1)
    profe1.dormir()

    print("Herencia Ayudante profe-------------")
    ayudante = AyudanteProfesor("Adrián",20,2546,"ICO",1325,"Ing de Software", 4)
    print(ayudante)
    ayudante.dormir()

main()