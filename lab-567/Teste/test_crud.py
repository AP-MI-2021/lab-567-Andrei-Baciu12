from Domain.cheltuieli import creeaza_cheltuiala
from Domain.cheltuieli import get_numar_apartament
from Logic.CRUD import create
from Logic.CRUD import delete
from Logic.CRUD import read
from Logic.CRUD import update


def get_data():
    return [
        creeaza_cheltuiala(1, 100, '27.09.2021', 'alte cheltuieli'),
        creeaza_cheltuiala(5, 250, '12.10.2021', 'intretinere'),
        creeaza_cheltuiala(6, 300, '20.09.2021', 'canal'),
        creeaza_cheltuiala(7, 200, '12.01.2021', 'alte cheltuieli')
    ]


def test_create():
    cheltuieli = get_data()
    noua_cheltuiala = creeaza_cheltuiala(2, 50, '31.10.2021', 'intretinere')
    lista_noua_de_cheltuieli = create(cheltuieli, 2, 50, '31.10.2021', 'intretinere')
    assert len(lista_noua_de_cheltuieli) == len(cheltuieli) + 1
    assert noua_cheltuiala in lista_noua_de_cheltuieli


def test_read():
    cheltuieli = get_data()
    o_cheltuiala = cheltuieli[2]
    assert read(cheltuieli, get_numar_apartament(o_cheltuiala)) == o_cheltuiala


def test_update():
    cheltuieli = get_data
    new_cheltuiala = creeaza_cheltuiala(5, 210, '10.10.2020', 'alte cheltuieli')
    cheltuiala1 = update(cheltuieli, new_cheltuiala)
    assert new_cheltuiala in cheltuiala1
    assert cheltuiala1 not in cheltuieli


def test_delete():
    cheltuieli = get_data()
    to_delete = 6
    cheltuiala_stearsa = read(cheltuieli, to_delete)
    stergere_cheltuiala = delete(cheltuieli, to_delete)
    assert cheltuiala_stearsa not in stergere_cheltuiala
    assert cheltuiala_stearsa in cheltuieli
    assert len(stergere_cheltuiala) == len(cheltuieli) - 1


def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()
