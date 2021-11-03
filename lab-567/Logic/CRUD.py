from Domain.cheltuieli import creeaza_cheltuiala
from Domain.cheltuieli import get_numar_apartament


def create(lista_cheltuieli: list, numar_apartament: int, suma: float, data: str, tipul_cheltuielii: str):
    """
    Functia creeaza o cheltuiala
    :param lista_cheltuieli:lista de cheltuieli
    :param numar_apartament:un numar de apartament
    :param suma:suma cheltuielii
    :param data:data aferenta cheltuielii
    :param tipul_cheltuielii:tipul de cheltuiala
    :return:o lista de cheltuielii formata din lista de cheltuielii si noua cheltuiala creata
    """
    cheltuiala = creeaza_cheltuiala(numar_apartament, suma, data, tipul_cheltuielii)
    return lista_cheltuieli + [cheltuiala]


def read(lista_cheltuieli: list, numar_apartament: int):
    """
    Citeste o cheltuiala dintr o baza de date ce contine mai multe cheltuieli
    :param lista_cheltuieli: lista de cheltuieli
    :param numar_apartament:numar apartamentului care a "facut" cheltuiala
    :return:cheltuiala aferenta numarului de apartament dat, lista de cheltuieli existente daca numar_apartament = None
    """
    cheltuiala_ceruta = None
    for cheltuiala in lista_cheltuieli:
        if get_numar_apartament(cheltuiala) == numar_apartament:
            cheltuiala_ceruta = cheltuiala
    if cheltuiala_ceruta:
        return cheltuiala_ceruta
    return lista_cheltuieli


def update(lista_cheltuieli, noua_cheltuiala):
    lista_actualizata = []
    for cheltuiala in lista_cheltuieli:
        if get_numar_apartament(noua_cheltuiala) != get_numar_apartament(cheltuiala):
            lista_actualizata.append(cheltuiala)
        else:
            lista_actualizata.append(noua_cheltuiala)

    return lista_actualizata


def delete(lista_cheltuieli: list, numar_apartament: int):
    """
    Functia sterge cheltuiala anumitui apartament
    :param lista_cheltuieli: lista memorata de cheltuieli
    :param numar_apartament: id_ul cheltuielii
    :return: lista memorata de cheltuieli fara cheltuiala apartamentului ce doreste a fi stearsa
    """
    lista_de_cheltuiala = []
    for cheltuiala in lista_cheltuieli:
        if get_numar_apartament(cheltuiala) != numar_apartament:
            lista_de_cheltuiala.append(cheltuiala)

    return lista_de_cheltuiala
