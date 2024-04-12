# Primjenom računalnog razmišljanja osmislite i implementirajte
# funkciju koja traži postoji li element u sortiranoj listi.
# Funkcija vraća True ako je element u listi, inače False.
# Pretpostavka: lista je uvijek sortirana od najmanjeg do najvećeg elementa.

# Za pomoć imate tri funkcije:
#   - `sredina(lista)`
#       - vraća srednji element u listi.
#   - `uzmi_desno_od_sredine(lista)`
#       - vraća novu listu, od srednjeg elementa do kraja liste
#       - srednji element nije uključen u novu listu!
#   - `uzmi_lijevo_od_sredine(lista)`
#       - vraća novu listu, od početka liste do srednjeg elementa
#       - srednji element nije uključen


def sredina(lista):
    mid = len(lista) // 2
    return lista[mid]


def uzmi_desno_od_sredine(lista):
    mid = len(lista) // 2
    return lista[mid + 1:]


def uzmi_lijevo_od_sredine(lista):
    mid = len(lista) // 2
    return lista[:mid]


def trazi(lista, element):
    if __name__ == '__main__':
    lista = [1, 3, 5, 7, 9, 11, 13]
    ciljani_element = 7
    if binary_search(lista, ciljani_element):
        print(f"Element {ciljani_element} je pronađen.")
    else:
        print(f"Element {ciljani_element} nije pronađen.")
    pass


# Program pri pokretanju testira ispravnost implementacije funkcije trazi
def main():
    lista = [1, 2, 3, 4, 5]
    for i in range(len(lista)):
        assert trazi(lista, lista[i])

    assert trazi([1, 2, 3, 4, 5], 10) is False

    lista = sorted(['a', 'c', 'z', 'f', 'e', 'e', 'r', 'w'])
    for i in range(len(lista)):
        assert trazi(lista, lista[i])

    assert trazi([], 10) is False

    print('Implementacija je ispravna')


if __name__ == '__main__':
    main()
