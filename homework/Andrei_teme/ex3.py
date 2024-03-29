from alegere import alegere_nr_utilizator
from numere import alegere_nr_random
from comparare import comparare_liste_nr

lista_nr_utilizator = alegere_nr_utilizator()
lista_nr_random = alegere_nr_random()

print(lista_nr_utilizator)
print(lista_nr_random)

comparare_liste_nr(lista_nr_utilizator,lista_nr_random)
