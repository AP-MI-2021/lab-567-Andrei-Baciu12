def creeaza_noua_cheltuiala(id, numar_apartament, suma, data, tipul_cheltuielii):
    return [id, numar_apartament, suma, data, tipul_cheltuielii]


def get_id(cheltuiala):
    return cheltuiala[0]


def get_numar_apartament(cheltuiala):
    return cheltuiala[1]


def get_suma(cheltuiala):
    return cheltuiala[2]


def get_data(cheltuiala):
    return cheltuiala[3]


def get_tipul_cheltuielii(cheltuiala):
    return cheltuiala([4])


def get_str(cheltuiala):
    return(f'Cheltuiala de la {get_numar_apartament(cheltuiala)} cu id {get_id(cheltuiala)} este in valoare de\
    {get_suma(cheltuiala)} din data de {get_data(cheltuiala)} si e de tip {get_tipul_cheltuielii(cheltuiala)}')