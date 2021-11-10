from Domain.cheltuiala import creeaza_cheltuiala, get_str, get_numar_apartament, get_data, get_tipul_cheltuielii, \
    get_suma, get_id
from Logic.CRUD import create, read, update, delete
from Logic.adunare_valoare import aduna_valoare
from Logic.afisare_sume_lunare import afisare_sume_lunare
from Logic.determinare_valoare_mare import determina_cea_mai_mare_cheltuiala
from Logic.ordonare_descrescator import ordonare_descrescator_suma
from Logic.stergere_cheltuiala import stergere_cheltuiala


def show_menu():
    print(" 1 -> CRUD ")
    print(" 2 -> Stergere cheltuiala pentru un apartament dat")
    print(" 3 -> Adunare o valoare la o cheltuiala")
    print(" 4 -> Determinarea celei mai mari cheltuieli de un tip")
    print(" 5 -> Ordonare cheltiueli in mod descrescator dupa suma")
    print(" 6-> Afisare sume cheltuieli per luna")
    print(" z -> Undo")
    print(" y -> Redo")
    print(" x -> Exit!!!")


def handle_new_list(list_versions, current_versions, cheltuieli):
    while current_versions < len(list_versions) - 1:
        list_versions.pop()
    list_versions.append(cheltuieli)
    current_versions += 1
    return list_versions, current_versions


def handle_undo(list_versions, current_versions):
    if current_versions < 1:
        print("Nu se mai poate face undo!")
        return
    current_versions -= 1
    return list_versions[current_versions], current_versions


def handle_redo(list_versions, current_versions):
    if current_versions == len(list_versions) - 1:
        print("Nu se mai poate face redo!")
        return
    current_versions += 1
    return list_versions[current_versions], current_versions


def handle_afisare_cheltuieli_luna(cheltuieli):
    cheltuielile_date = afisare_sume_lunare(cheltuieli)
    for numar_apartament in cheltuielile_date:
        print(f"Ap. cu nr. {numar_apartament} are o cheltuiala in valoare de\
 {cheltuielile_date[numar_apartament]['suma']} in luna {cheltuielile_date[numar_apartament]['luna']}")


def run_ui(cheltuieli):
    list_versions = [cheltuieli]
    current_versions = 0

    while True:
        show_menu()
        optiune = input('Introduceti optiunea: ')
        if optiune == '1':
            cheltuieli = handle_crud(cheltuieli)
            list_versions, current_versions = handle_new_list(list_versions, current_versions, cheltuieli)
        elif optiune == 'x':
            break
        elif optiune == '2':
            cheltuieli = handle_stergere(cheltuieli)
            list_versions, current_versions = handle_new_list(list_versions, current_versions, cheltuieli)
        elif optiune == '3':
            cheltuieli = handle_aduna(cheltuieli)
            list_versions, current_versions = handle_new_list(list_versions, current_versions, cheltuieli)
        elif optiune == '4':
            cheltuieli = handle_pret_mare(cheltuieli)
            list_versions, current_versions = handle_new_list(list_versions, current_versions, cheltuieli)
        elif optiune == '5':
            cheltuieli = handle_ordonare(cheltuieli)
            list_versions, current_versions = handle_new_list(list_versions, current_versions, cheltuieli)
        elif optiune == '6':
            cheltuieli = handle_afisare_cheltuieli_luna(cheltuieli)
            list_versions, current_versions = handle_new_list(list_versions, current_versions, cheltuieli)
        elif optiune == 'z':
            cheltuieli, current_versions = handle_undo(list_versions, current_versions)
        elif optiune == 'y':
            cheltuieli, current_versions = handle_redo(list_versions, current_versions)
        else:
            print('Optiune invalida!')
    return cheltuieli


def handle_ordonare(cheltuieli):
    try:
        cheltuieli = ordonare_descrescator_suma(cheltuieli)
    except ValueError as ve:
        print('Eroare:', ve)

    return cheltuieli


def handle_pret_mare(cheltuieli):
    try:
        valoare_mare = determina_cea_mai_mare_cheltuiala(cheltuieli)
        print(valoare_mare)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
    return cheltuieli


def handle_aduna(cheltuieli):
    try:
        data = input("Introduceti o data de forma(DD.MM.YYYY): ")
        valoare = int(input("Dati o valoare: "))
        return aduna_valoare(valoare, data, cheltuieli)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
    return cheltuieli


def undo(cheltuieli, list_versions, current_versions):
    if len(list_versions) > 0:
        current_versions.append(cheltuieli)
        cheltuieli = list_versions.pop()
    else:
        print("Nu se mai poate face undo!")
    return cheltuieli


def redo(cheltuieli, list_versions, current_versions):
    if len(current_versions) > 0:
        list_versions.append(cheltuieli)
        cheltuieli = current_versions.pop()
    else:
        print("Nu se mai poate face redo!")
    return cheltuieli


def handle_stergere(lista):
    try:
        numar_apartament = int(input('Dati numar apartament: '))
        return stergere_cheltuiala(numar_apartament, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
    return lista


def handle_add(cheltuieli):
    try:
        id = int(input("Dati id-ul apartamentului: "))
        numar_apartament = int(input("Dati numarul apartamentului: "))
        suma = float(input("Dati suma cheltuielii: "))
        data = input("Dati data aferenta cheltuielii: ")
        tipul = input("Dati tipul cheltuielii: ")
        return create(cheltuieli, id, numar_apartament, suma, data, tipul)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
    return cheltuieli


def handle_show(cheltuieli):
    for cheltuiala in cheltuieli:
        print(get_str(cheltuiala))


def handle_show_details(cheltuieli):
    try:
        numar_apartament = int(input("Dati numarul apartamentului: "))
        cheltuiala = read(cheltuieli, numar_apartament)
        print(f'Id-ul apartamentului: {get_id(cheltuiala)}')
        print(f'Numar apartament: {get_numar_apartament(cheltuiala)}')
        print(f'Suma: {get_suma(cheltuiala)}')
        print(f'Data: {get_data(cheltuiala)}')
        print(f'Tip: {get_tipul_cheltuielii(cheltuiala)}')
    except ValueError as ve:
        print("Eroare: {}".format(ve))
    return cheltuieli


def handle_update(cheltuieli):
    try:

        id = int(input("Dati id cheltuiala: "))
        numar_ap = int(input('Dati numar apartament: '))
        suma = float(input('dati suma aferenta cheltuielii: '))
        data = input('dati data: ')
        tipul = input('dati tipul de cheltuiala: ')
        return update(cheltuieli, creeaza_cheltuiala(id, numar_ap, suma, data, tipul))
    except ValueError as ve:
        print("Eroare: {}".format(ve))
    return cheltuieli


def handle_delete(cheltuieli):
    try:
        numar_ap = int(input('dati numarul apartamentului: '))
        cheltuieli = delete(cheltuieli, numar_ap)
        print('Stergerea a fost realizata cu succes!! ')
        return cheltuieli
    except ValueError as ve:
        print("Eroare: {}".format(ve))
    return cheltuieli


def handle_crud(cheltuieli):
    print('1. Adaugare')
    print('2. Stergere')
    print('3. Modificare')
    print('a. Afisare')
    print('c. Afisare detalii cheltuieli')
    optiune = input("Alegeti optiunea: ")
    if optiune == '1':
        cheltuieli = handle_add(cheltuieli)
    elif optiune == '2':
        cheltuieli = handle_delete(cheltuieli)
    elif optiune == '3':
        cheltuieli = handle_update(cheltuieli)
    elif optiune == 'a':
        handle_show(cheltuieli)
    elif optiune == 'c':
        handle_show_details(cheltuieli)
    else:
        print('optiune invalida')
    return cheltuieli
