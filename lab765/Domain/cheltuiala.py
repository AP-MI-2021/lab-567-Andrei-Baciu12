def creeaza_cheltuiala(id_: int, numar_apartament, suma, data: str, tipul_cheltuielii):
    """
    Functia creeaza o cheltuiala si o returneaza ca un dictionar
    :param id_: id-ul cheltuiala
    :param numar_apartament: numar apartament aferent cheltuielii
    :param suma: suma cheltuiala
    :param data: data cheltuielii
    :param tipul_cheltuielii: tipul cheltuielii
    :return: o cheltuiala
    """
    return {
        'id': id_,
        'nr_ap': numar_apartament,
        'suma': suma,
        'data': data,
        'tip': tipul_cheltuielii

    }


def get_id(cheltuiala):
    """
    Getter pentru id-ul cheltuielii
    :param cheltuiala: o cheltuiala
    :return: id-ul cheltuielii ca parametru
    """
    return cheltuiala['id']


def get_numar_apartament(cheltuiala):
    """
    Getter pentru numarul apartamentului
    :param cheltuiala:cheltuiala
    :return:numarul apartamentului
    """
    try:
        return cheltuiala['nr_ap']
    except TypeError as ve:
        print("Eroare: {}".format(ve))


def get_suma(cheltuiala):
    """
    Getter pentru suma cheltuielii
    :param cheltuiala: o cheltuiala
    :return: suma cheltuielii ca parametru
    """
    try:
        return cheltuiala['suma']
    except TypeError as ve:
        print("Eroare: {}".format(ve))


def get_data(cheltuiala):
    try:
        return cheltuiala['data']
    except TypeError as ve:
        print("Eroare: {}".format(ve))


def get_tipul_cheltuielii(cheltuiala):
    """
    Getter pentru tipul de cheltuiala
    :param cheltuiala: o cheltuiala
    :return: un tip de cheltuiala
    """
    return cheltuiala['tip']


def get_str(cheltuiala):
    return f'Cheltuiala de la nr. {get_numar_apartament(cheltuiala)} cu id {get_id(cheltuiala)} din \
 {get_data(cheltuiala)} este in valoare de {get_suma(cheltuiala)} si este de tipul {get_tipul_cheltuielii(cheltuiala)}'
