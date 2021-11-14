from UserInterface.Console import run_ui
from UserInterface.help import command_line


def alege_meniu():
    """
    Functia afiseaza meniul pe care il doresti.
    :return: unul din cele 2 meniuri
    """
    while True:
        lista = []
        print("1 -> Meniul 1")
        print("2 -> Meniul 2")
        print("x -> Exit")
        optiune = input("Alege optiune: ")
        if optiune == "1":
            run_ui(lista)
        elif optiune == "2":
            command_line(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune invalida!")
