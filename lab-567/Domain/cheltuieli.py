def creeaza_cheltuiala(numar_apartament, suma, data, tipul_cheltuielii):
    """

    :param numar_apartament: numarul apartamentului care a realizat cheltuiala
    :param suma: suma cheltuielii
    :param data: data aferenta cheltuielii
    :param tipul_cheltuielii: tipul cheltuielii
    :return: o cheltuiala
    """
    return {
        'nr_ap': numar_apartament,
        'suma': suma,
        'data': data,
        'tip': tipul_cheltuielii

    }


def get_numar_apartament(cheltuiala):
    """
    Getter pentru numarul apartamentului
    :param cheltuiala:cheltuiala
    :return:numarul apartamentului
    """
    return cheltuiala['nr_ap']


def get_suma(cheltuiala):
    """
    Getter pentru suma cheltuielii
    :param cheltuiala: o cheltuiala
    :return: suma cheltuielii ca parametru
    """
    return cheltuiala['suma']


def get_data(cheltuiala):
    """
    Getter pentru data aferenta cheltuielii
    :param cheltuiala: o cheltuiala
    :return: data cheltuielii ca parametru
    """
    return cheltuiala['data']


def get_tipul_cheltuielii(cheltuiala):
    """
    Getter pentru tipul de cheltuiala
    :param cheltuiala: o cheltuiala
    :return: un tip de cheltuiala
    """
    return cheltuiala['tip']


def get_str(cheltuiala):
    return f'Cheltuiala de la {get_numar_apartament(cheltuiala)}, din {get_data(cheltuiala)}, este\
    in valoare de {get_suma(cheltuiala)}, si este de tipul {get_tipul_cheltuielii(cheltuiala)}'
