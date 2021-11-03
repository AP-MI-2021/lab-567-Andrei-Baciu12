from Domain.cheltuieli import creeaza_cheltuiala, get_str, get_numar_apartament, get_data, get_tipul_cheltuielii, \
    get_suma
from Logic.CRUD import create, read, update, delete


def show_menu():
    print(" 1 -> CRUD "
          " x -> Exit!!!")


def run_ui(cheltuieli):
    while True:
        show_menu()
        optiune = input('Introduceti optiunea: ')
        if optiune == '1':
            cheltuieli = handle_crud(cheltuieli)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida!')
    return cheltuieli


def handle_add(cheltuieli):
    numar_apartament = int(input("Dati numarul apartamentului: "))
    suma = float(input("Dati suma cheltuielii: "))
    data = input("Dati data aferenta cheltuielii: ")
    tipul = input("Dati tipul cheltuielii: ")
    return create(cheltuieli, numar_apartament, suma, data, tipul)


def handle_show(cheltuieli):
    for cheltuiala in cheltuieli:
        print(get_str(cheltuiala))


def handle_show_details(cheltuieli):
    numar_ap = int(input('dati numar apartament: '))
    cheltuiala = read(cheltuieli, numar_ap)
    print(f'Numar apartament: {get_numar_apartament(cheltuiala)}')
    print(f'Suma: {get_suma(cheltuiala)}')
    print(f'Data: {get_data(cheltuiala)}')
    print(f'Tip: {get_tipul_cheltuielii(cheltuiala)}')


def handle_update(cheltuieli):
    numar_ap = int(input('Dati numar apartament: '))
    suma = float(input('dati suma aferenta cheltuielii: '))
    data = input('dati data: ')
    tipul = input('dati tipul de cheltuiala: ')
    return update(cheltuieli, creeaza_cheltuiala(numar_ap, suma, data, tipul))


def handle_delete(cheltuieli):
    numar_ap = int(input('dati numarul apartamentului: '))
    cheltuieli = delete(cheltuieli, numar_ap)
    print('Stergerea a fost realizata cu succes!! ')
    return cheltuieli


def handle_crud(cheltuieli):
    while True:
        print('1. Adaugare')
        print('2. Stergere')
        print('3. Modificare')
        print('a. Afisare')
        print('b. Revenire')
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
        elif optiune == 'b':
            break
        else:
            print('optiune invalida')
    return cheltuieli
