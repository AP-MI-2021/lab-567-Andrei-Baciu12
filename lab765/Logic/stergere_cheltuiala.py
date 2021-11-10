from Domain.cheltuiala import get_numar_apartament
from Logic.CRUD import delete


def stergere_cheltuiala(nr_ap, lista):
    """
    Functia sterge o cheltuiala din lista de cheltuieli a unui apartament a carui numar il introducem.
    :param nr_ap: numarul apartamentului
    :param lista: lista de cheltuieli
    :return: lista de cheltuieli fara cheltuiala stearsa
    """
    try:

        for cheltuiala in lista:
            if get_numar_apartament(cheltuiala) == nr_ap:
                lista = delete(lista, nr_ap)

        return lista
    except ValueError as ve:
        print("Eroare: {}".format(ve))
    return lista
