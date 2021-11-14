from Domain.cheltuiala import get_suma, get_numar_apartament
from Logic.CRUD import creeaza_cheltuiala
from Logic.afisare_sume_lunare import afisare_sume_lunare
from Logic.determinare_valoare_mare import determina_cea_mai_mare_cheltuiala
from Logic.ordonare_descrescator import ordonare_descrescator_suma
from Logic.stergere_cheltuiala import stergere_cheltuiala


def test_stergere_cheltuiala():
    lista = []
    lista = creeaza_cheltuiala(1, 1, 100, '27.09.2021', 'alte cheltuieli'),
    lista = creeaza_cheltuiala(2, 5, 250, '12.10.2021', 'intretinere'),
    lista = creeaza_cheltuiala(3, 6, 300, '20.09.2021', 'canal'),
    lista = creeaza_cheltuiala(4, 4, 200, '12.01.2021', 'alte cheltuieli')

    lista = stergere_cheltuiala(5, lista)
    assert len(lista) == 0
    lista1 = stergere_cheltuiala(1, lista)
    assert len(lista1) == 0


def test_ordonare_descrescator_suma():
    lista = []
    lista = creeaza_cheltuiala(1, 1, 100, '27.09.2021', 'alte cheltuieli'),
    lista = creeaza_cheltuiala(2, 5, 250, '12.10.2021', 'intretinere'),
    lista = creeaza_cheltuiala(3, 6, 300, '20.09.2021', 'canal'),
    lista = creeaza_cheltuiala(4, 4, 200, '12.01.2021', 'alte cheltuieli')

    list = ordonare_descrescator_suma(lista)
    assert get_suma(list[0]) == 300
    assert get_numar_apartament(list[1]) == 5


def test_determina_cea_mai_mare_cheltuiala():
    lista = []
    lista = creeaza_cheltuiala(1, 1, 100, '27.09.2021', 'alte cheltuieli'),
    lista = creeaza_cheltuiala(4, 4, 200, '12.01.2021', 'alte cheltuieli')

    list = determina_cea_mai_mare_cheltuiala(lista)
    assert list == {
        'alte cheltuieli': {'id-ul': 4, 'nr_ap': 4, 'suma': 200, 'data': '12.02.2021', 'tip': 'alte cheltuieli'}}


def test_afisare_sume_lunare():
    lista = []
    lista = creeaza_cheltuiala(1, 1, 100, '27.09.2021', 'alte cheltuieli'),
    lista = creeaza_cheltuiala(2, 5, 250, '12.10.2021', 'intretinere'),
    lista = creeaza_cheltuiala(3, 6, 300, '20.09.2021', 'canal'),
    lista = creeaza_cheltuiala(4, 4, 200, '12.10.2021', 'alte cheltuieli')

    result = afisare_sume_lunare(lista)
    assert len(result) == 1
    assert result[1] == {'luna': 9, 'suma': 400}
    assert result[2] == {'luna': 10, 'suma': 450}


def teste():
    test_afisare_sume_lunare()
    test_determina_cea_mai_mare_cheltuiala()
    test_ordonare_descrescator_suma()
