from Domain.cheltuiala import get_suma


def ordonare_descrescator_suma(cheltuieli):
    """
    Functia returneaza lista de cheltuieli in ordine descrescatoare a sumei lor.
    :param cheltuieli: o lista de cheltuieli
    :return: o lista de cheltuieli obtinuta prin ordonarea sumelor lor in ordine descrescatoare
    """
    return sorted(cheltuieli, key=get_suma, reverse=True)
