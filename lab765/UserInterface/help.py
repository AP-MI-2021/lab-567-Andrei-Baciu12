from Logic.CRUD import delete, create
from UserInterface.Console import handle_show


def show_detail(list):
    for cheltuiala in list:
        print(handle_show(cheltuiala))


def menu():
    print(" add, id, nr_ap, suma, data, tip")
    print(" delete, nr_ap")
    print(" exit")


def command_line(list):
    menu()
    while True:
        optiune = input("Dati optiunea: ")
        if optiune == 'ajutor':
            menu()
        else:
            options = optiune.split(";")
            print(list)
            if options[0] == "iesire":
                break
            else:
                for cheltuiala in options:
                    option = cheltuiala.split(",")
                    if option[0] == "add":
                        try:
                            id_ul = int(option[1])
                            nr_ap = int(option[2])
                            suma = float(option[3])
                            data = str(option[4])
                            tip = str(option[5])
                            list = create(list, id_ul, nr_ap, suma, data, tip)
                        except ValueError as ve:
                            print("Eroare: {}".format(ve))
                            return list
                    elif option[0] == "delete":
                        try:
                            nr_ap = int(option[1])
                            list = delete(list, nr_ap)
                        except ValueError as ve:
                            print("Eroare: {}".format(ve))
                            return list

                    elif option[0] == "show":
                        show_detail(list)
                    else:
                        print("Optiune invalida!")
