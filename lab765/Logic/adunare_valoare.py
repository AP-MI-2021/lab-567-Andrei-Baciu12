from Domain.cheltuiala import creeaza_cheltuiala, get_data, get_id, get_numar_apartament, get_suma, \
    get_tipul_cheltuielii


def aduna_valoare(valoare, data, cheltuieli):
    """
    Functia aduna valoarea data de utilizator la valoarea initiala a sumei date dintr-o data citita de la tastatura.
    :param valoare: un numar introdus de la tastatura
    :param data: data care trebuie sa fie prin lista de cheltuieli
    :param cheltuieli: lista de cheltuieli
    :return: lista de cheltuieli cu sumele modificate
    """
    result_list = []
    if len(data) != 10:
        raise ValueError("Data introdusa nu este relevanta!")
    if len(data) != 10 and (data[2] != '.' and data[5] != '.'):
        raise ValueError("Data introdusa nu este conforma!")
    zi = data[0] + data[1]
    luna = data[3] + data[4]
    an = data[6] + data[7] + data[8] + data[9]
    if 31 < int(zi) < 1:
        raise ValueError("Data introdusa nu este corecta!")
    if 12 < int(luna) < 1:
        raise ValueError("Luna data este invalida!")
    if 2021 < int(an) < 1900:
        raise ValueError("Anul dat nu se potriveste!")
    for cheltuiala in cheltuieli:
        if get_data(cheltuiala) == data:
            cheltuiala_obtinuta = creeaza_cheltuiala(get_id(cheltuiala),
                                                     get_numar_apartament(cheltuiala),
                                                     get_suma(cheltuiala) + valoare,
                                                     get_data(cheltuiala),
                                                     get_tipul_cheltuielii(cheltuiala))
            result_list.append(cheltuiala_obtinuta)
            print('Adunarea valorii s-a realizat cu succes!')
        else:
            print("Nu exista cheltuieli din data introdusa!")
    return result_list
