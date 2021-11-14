from Domain.cheltuiala import get_suma


def suma(cheltuiala):
    return get_suma(cheltuiala)


def ordonare_descrescator_suma(cheltuieli):
    """
    Functia returneaza lista de cheltuieli in ordine descrescatoare a sumei lor.
    :param cheltuieli: o lista de cheltuieli
    :return: o lista de cheltuieli obtinuta prin ordonarea sumelor lor in ordine descrescatoare
    """
    if suma is int:
        return sorted(cheltuieli, key=suma, reverse=True)