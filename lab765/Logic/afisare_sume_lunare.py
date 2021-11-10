from Domain.cheltuiala import get_suma, get_data, get_numar_apartament


def afisare_sume_lunare(cheltuieli):
    """
    Functia returneaza valoarea cheltuielii aferenta fiecarei luni.
    :param cheltuieli:o lista de cheltuieli
    :return:
    """
    result = {}
    for cheltuiala in cheltuieli:
        suma = get_suma(cheltuiala)
        data = get_data(cheltuiala)
        nr_ap = get_numar_apartament(cheltuiala)
        luna = data[3] + data[4]
        if nr_ap not in result:
            result[nr_ap] = {}
            result[nr_ap]['luna'] = luna
            result[nr_ap]['suma'] = suma
        else:
            if luna in result[nr_ap]['luna']:

                result[nr_ap]['suma'] = result[nr_ap]['suma'] + suma
            else:
                result[nr_ap]['luna'] = luna
                result[nr_ap]['suma'] = suma
    return result
