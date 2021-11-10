from Domain.cheltuiala import get_tipul_cheltuielii, get_suma


def determina_cea_mai_mare_cheltuiala(cheltuieli):
    """
    Functia determina cea mai mare suma a unei cheltuiueli de un tip dat
    :param cheltuieli: o lista de cheltuieli
    :return: cea mai mare cheltuiala de un tip
    """
    try:
        lista = {}
        for cheltuiala in cheltuieli:
            tip = get_tipul_cheltuielii(cheltuiala)
            suma = get_suma(cheltuiala)
            if tip not in lista:
                lista[tip] = cheltuiala
            else:
                if suma > get_suma(lista[tip]):
                    lista[tip] = cheltuiala
        return lista
    except ValueError as ve:
        print("Eroare: {}".format(ve))
    return cheltuieli
