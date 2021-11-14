from Domain.cheltuiala import get_str
from Logic.CRUD import delete, create
from Logic.determinare_valoare_mare import determina_cea_mai_mare_cheltuiala


def show_detail(list):
    for cheltuiala in list:
        print(get_str(cheltuiala))


def menu():
    print(" add, id, nr_ap, suma, data, tip")
    print(" delete, nr_ap")
    print(" iesire")
    print(" show")
    print(" aduna, id, nr_ap, suma, data, tip, valoare(cu care vreti sa adunati)")
    print(" update, id, nr_ap, suma, data, tip")
    print(" biggest_value . ATENTIE!!! Dupa aceea introducem iesire pentru a afisa cea mai mare cheltuiala!!! ")


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
                    option = cheltuiala.split(sep=",")
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
                            nr_ap = option[1]
                            nr_ap = int(nr_ap)
                            list = delete(list, nr_ap)
                        except ValueError as ve:
                            print("Eroare: {}".format(ve))
                            return list
                    elif option[0] == "show":
                        try:
                            show_detail(list)
                        except ValueError as ve:
                            print("Eroare: {}".format(ve))
                    elif option[0] == "aduna":
                        try:
                            id_ul = int(option[1])
                            nr_ap = int(option[2])
                            suma = float(option[3])
                            data = str(option[4])
                            tip = str(option[5])
                            valoare = int(option[6])
                            list = create(list, id_ul, nr_ap, (suma + valoare), data, tip)
                        except ValueError as ve:
                            print("Eroare: {}".format(ve))
                    elif option[0] == "update":
                        try:
                            id_ul = int(option[1])
                            nr_ap = int(option[2])
                            suma = float(option[3])
                            data = str(option[4])
                            tip = str(option[5])
                            list1 = create(list, id_ul, nr_ap, suma, data, tip)
                            list = create(list1, id_ul, nr_ap, suma, data, tip)
                        except ValueError as ve:
                            print("Eroare: {}".format(ve))
                    elif option[0] == "biggest_value":
                        list = determina_cea_mai_mare_cheltuiala(list)
                    else:
                        print("Optiune invalida!")
