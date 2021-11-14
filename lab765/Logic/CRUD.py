from Domain.cheltuiala import get_numar_apartament, creeaza_cheltuiala


def create(lista_cheltuieli: list, _id: int, numar_apartament: int, suma: float, data: str, tipul_cheltuielii: str):
    """
    Functia creeaza o cheltuiala
    :param _id:id-ul cheltuielii
    :param lista_cheltuieli:lista de cheltuieli
    :param numar_apartament:un numar de apartament
    :param suma:suma cheltuielii
    :param data:data aferenta cheltuielii
    :param tipul_cheltuielii:tipul de cheltuiala
    :return:o lista de cheltuielii formata din lista de cheltuielii si noua cheltuiala creata
    """
    if numar_apartament < 1:
        raise ValueError("Numarul apartamentului trebuie sa fie un numar intreg si pozitiv!")
    if tipul_cheltuielii != "intretinere" and tipul_cheltuielii != "alte cheltuieli" and tipul_cheltuielii != "canal":
        raise ValueError("Tipul cheltuielii trebuie sa fie doar unul din cele 3 mentionate!")
    if len(data) != 10:
        raise ValueError("Data introdusa nu este relevanta!")
    if len(data) != 10 and (data[2] != '.' and data[5] != '.'):
        raise ValueError("Data introdusa nu este conforma!")
    if _id < 1 and _id is not int:
        raise ValueError("Id-ul dat nu este bun!")
    zi = data[0] + data[1]
    luna = data[3] + data[4]
    an = data[6] + data[7] + data[8] + data[9]
    if 31 < int(zi) < 1:
        raise ValueError("Data introdusa nu este corecta!")
    if 12 < int(luna) < 1:
        raise ValueError("Luna data este invalida!")
    if 2021 < int(an) < 1900:
        raise ValueError("Anul dat nu se potriveste!")
    cheltuiala = creeaza_cheltuiala(_id, numar_apartament, suma, data, tipul_cheltuielii)
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
    if numar_apartament < 1:
        raise ValueError("Numarul apartamentului trebuie sa fie un numar intreg si pozitiv!")
    return lista_cheltuieli


def update(lista_cheltuieli, noua_cheltuiala):

    lista_actualizata = []
    for cheltuiala in lista_cheltuieli:
        if get_numar_apartament(noua_cheltuiala) != get_numar_apartament(cheltuiala):
            lista_actualizata.append(cheltuiala)

        else:
            lista_actualizata.append(noua_cheltuiala)
    if get_numar_apartament(noua_cheltuiala) < 1:
        raise ValueError("Numarul apartamentului trebuie sa fie un numar intreg si pozitiv!")
    return lista_actualizata


def delete(lista_cheltuieli: list, numar_apartament):
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
    if numar_apartament < 1:
        raise ValueError("Numarul apartamentului trebuie sa fie un numar intreg si pozitiv!")
    return lista_de_cheltuiala
