from Logic.CRUD import create
from UserInterface.Console import handle_new_list, handle_undo, handle_redo


def test_undo_redo():
    list_versions = [[]]
    current_versions = 0
    lista = []
    lista = create(lista, 1, 2, 100, "11.11.2021", "canal")
    list_versions, current_versions = handle_new_list(list_versions, current_versions, lista)
    lista = create(lista, 2, 20, 110, "14.11.2021", "canal")
    list_versions, current_versions = handle_new_list(list_versions, current_versions, lista)
    lista = create(lista, 3, 30, 150, "13.11.2021", "intretinere")
    list_versions, current_versions = handle_new_list(list_versions, current_versions, lista)
    assert lista == [{'id': 1, 'nr_ap': 2, 'suma': 100, 'data': '11.11.2021', 'tip': 'canal'},
                     {'id': 2, 'nr_ap': 20, 'suma': 110, 'data': '14.11.2021', 'tip': 'canal'},
                     {'id': 3, 'nr_ap': 30, 'suma': 150, 'data': '13.11.2021', 'tip': 'intretinere'}]
    lista, current_versions = handle_undo(list_versions, current_versions)
    lista, current_versions = handle_undo(list_versions, current_versions)
    assert lista == [{'id': 1, 'nr_ap': 2, 'suma': 100, 'data': '11.11.2021', 'tip': 'canal'}]
    lista, current_versions = handle_undo(list_versions, current_versions)
    assert lista == []
    lista = []
    lista = create(lista, 1, 2, 100, "11.11.2021", "canal")
    list_versions, current_versions = handle_new_list(list_versions, current_versions, lista)
    lista = create(lista, 2, 20, 110, "14.11.2021", "canal")
    list_versions, current_versions = handle_new_list(list_versions, current_versions, lista)
    lista = create(lista, 3, 30, 150, "13.11.2021", "intretinere")
    list_versions, current_versions = handle_new_list(list_versions, current_versions, lista)
    assert lista == [{'id': 1, 'nr_ap': 2, 'suma': 100, 'data': '11.11.2021', 'tip': 'canal'},
                     {'id': 2, 'nr_ap': 20, 'suma': 110, 'data': '14.11.2021', 'tip': 'canal'},
                     {'id': 3, 'nr_ap': 30, 'suma': 150, 'data': '13.11.2021', 'tip': 'intretinere'}]
    lista, current_versions = handle_undo(list_versions, current_versions)
    lista, current_versions = handle_undo(list_versions, current_versions)
    assert lista == [{'id': 1, 'nr_ap': 2, 'suma': 100, 'data': '11.11.2021', 'tip': 'canal'}]
    lista, current_versions = handle_redo(list_versions, current_versions)
    assert lista == [{'id': 1, 'nr_ap': 2, 'suma': 100, 'data': '11.11.2021', 'tip': 'canal'},
                     {'id': 2, 'nr_ap': 20, 'suma': 110, 'data': '14.11.2021', 'tip': 'canal'}]
    lista, current_versions = handle_redo(list_versions, current_versions)
    assert lista == [{'id': 1, 'nr_ap': 2, 'suma': 100, 'data': '11.11.2021', 'tip': 'canal'},
                     {'id': 2, 'nr_ap': 20, 'suma': 110, 'data': '14.11.2021', 'tip': 'canal'},
                     {'id': 3, 'nr_ap': 30, 'suma': 150, 'data': '13.11.2021', 'tip': 'intretinere'}]
    lista, current_versions = handle_undo(list_versions, current_versions)
    lista, current_versions = handle_undo(list_versions, current_versions)
    assert lista == [{'id': 1, 'nr_ap': 2, 'suma': 100, 'data': '11.11.2021', 'tip': 'canal'}]
    lista, current_versions = handle_undo(list_versions, current_versions)
    assert lista == []
    lista, current_versions = handle_redo(list_versions, current_versions)
    lista, current_versions = handle_redo(list_versions, current_versions)
    assert lista == [{'id': 1, 'nr_ap': 2, 'suma': 100, 'data': '11.11.2021', 'tip': 'canal'},
                     {'id': 2, 'nr_ap': 20, 'suma': 110, 'data': '14.11.2021', 'tip': 'canal'}]
