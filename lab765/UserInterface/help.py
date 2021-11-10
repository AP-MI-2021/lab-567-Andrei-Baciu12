
# from Logic.CRUD import delete, creeaza_cheltuiala
#
#
#
#
# def meniu():
#     print(" add, id, nr_ap, suma, data, tip")
#     print(" delete, nr_ap")
#     print(" exit")
#
#
# def command_line(list):
#     while True:
#         optiune = input("Dati optiunea! ")
#         if optiune == 'ajutor':
#             meniu()
#         else:
#             options = optiune.split(";")
#             if options[0] == "iesire":
#                 break
#             else:
#                 for cheltuiala in options:
#                     option = cheltuiala.split(",")
#                 if option[0] == "add":
#                     try:
#                         id = option[1]
#                         nr_ap = int(option[2])
#                         suma = int(option[3])
#                         data = option[4]
#                         tip = option[5]
#                         list = creeaza_cheltuiala(id, nr_ap, suma, data, tip)
#                     except ValueError as ve:
#                         print("Eroare: {}".format(ve))
#                         return list
#                 elif option[0] == "delete":
#                     try:
#                         nr_ap = option[1]
#                         list = delete(list, nr_ap)
#                     except ValueError as ve:
#                         print("Eroare: {}".format(ve))
#                         return list
#                 else:
#                     print("Optiune invalida!")
