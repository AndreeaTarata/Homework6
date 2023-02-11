# 1. Clasa Factura
# Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
# avea aceeași serie), număr, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fara serie
# Metode:
# ● schimbă_cantitatea(cantitate)
# ● schimbă_prețul(pret)
# ● schimbă_nume_produs(nume)
#
# ● generează_factura() - va printa tabelar dacă reușiți
# Factura seria x numar y
# Data: generați automat data de azi
# Produs | cantitate | preț bucată | Total
# Telefon | 7 | 700 | 49000
# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/

# from datetime import date
# today = date.today()
# print(today)
#
# from datetime import datetime
# now = datetime.now()
# print(now)
#
# import datetime
# # timp_prezent = datetime.datetime.now()
# # print(timp_prezent.year)
# # print(timp_prezent.month)
# # print(timp_prezent.day)
#
# class Factura:
#     seria = 'x'
#     def __init__(self, numar, nume_produs, cantitate, pret_buc):
#         self.numar = numar
#         self.nume_produs = nume_produs
#         self.cantitate = cantitate
#         self.pret_buc = pret_buc
#     def schimba_cant(self, cant):
#         self.cantitate = cant
#         print(cant)
#     def schimba_pretul(self, pret):
#         self.pret_buc = pret
#         print(pret)
#     def schimba_nume_produs(self, nume):
#         self.nume_produs = nume
#         print(nume)
#     def genereaza_factura(self):
#         today = datetime.datetime.now().strftime("%y-%m-%d")
#         print(f'Factura seria {self.seria} numar {self.numar}')
#         print(f'Data: {today}')
#         print("Produs | cantitate | pret bucata | Total")
#         total = self.cantitate*self.pret_buc
#         print(f'{self.nume_produs}  |  {self.cantitate}        |      {self.pret_buc}     |     {total}')
#
# factura1 = Factura(1, 'lapte', 3, 20)
# factura1.schimba_cant(5)
# factura1.schimba_pretul(25)
# factura1.schimba_nume_produs('carne')
# factura1.genereaza_factura()
#
# factura2 = Factura(2, 'oua', 5, 10)
# factura2.schimba_cant(7)
# factura2.schimba_pretul(15)
# factura2.schimba_nume_produs('mere')
# factura2.genereaza_factura()
#
# factura3 = Factura(10, 'telefon', 5, 705)
# factura3.schimba_cant(7)
# factura3.schimba_pretul(700)
# factura3.schimba_nume_produs('telefoane')
# factura3.genereaza_factura

# 2.Clasa Masina
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
# culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate mașinile cand ies din fabrica sunt gri
# Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
# Culori disponibile = alegeți voi 5-7 culori
# Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
# Inmatriculata = False
# Constructor: model, viteza_maxima
# Metode:
# ● descrie() - se vor printa toate atributele, în afară de culori_disponibile
# ● înmatriculare() - va schimba atributul înmatriculată în True
# ● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
# culoare e în opțiunea de culori disponibile, altfel afișați o eroare
# ● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
# negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
# accelera până la viteza maximă
# ● franeaza() - mașina se va opri și va avea viteza 0
#
# class Masina:
#     marca = 'VW'
#     model = None
#     viteza_maxima = None
#     culoare_disponibila = ['alb', 'verde', 'rosu', 'galben']
#     culoare = 'gri'
#     viteza_actuală = 0
#     inmatriculata = False
#
#     def __init__(self, model, viteza_maxima):
#         self.model = model
#         self.viteza_maxima = viteza_maxima
#
#     def descrie(self):
#         print(
#             f'{self.marca} {self.model} de culoare {self.culoare}; Inmatriculata? {self.inmatriculata}. Viteza cu care stationraza: {self.viteza_actuală} si viteza la care poate ajunge: {self.viteza_maxima}')
#
#     def inmatriculata(self):
#         self.inmatriculata = True
#         print(self.inmatriculata)
#
#     def vopseste(self, culoare):
#         if culoare in self.culoare_disponibila:
#             print(f'Masina va fi vopsita in culoarea {culoare}')
#         else:
#             print (f'Eroare: culoarea {culoare} nu face parte din catalogul nostru')
#     def accelereaza(self, viteza):
#         if viteza < 0:
#             print(f'Eroarea. Viteza nu poate fi negativa!')
#         else:
#             if viteza > self.viteza_maxima:
#                 viteza = self.viteza_maxima
#                 print(f'Am accelerat pana la viteza {self.viteza_maxima}')
#             else:
#                 print(f'Aveti viteza de {viteza}')
#
#     def franeaza(self):
#         self.viteza_maxima = 0
#         print(f'Masina se va opri si are valoarea {self.viteza_maxima}')
#
# masina1 = Masina('Passat', 250)
# masina1.descrie()
# masina1.inmatriculata()
# masina1.vopseste('galben')
# masina1.vopseste('negru')
# masina1.accelereaza(20)
# masina1.accelereaza(-50)
# masina1.accelereaza(500)
# masina1.franeaza()


# 3. Clasa TodoList
# Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
# La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
# Metode:
#
# ● adauga_task(nume, descriere) - se va adauga in dict
# ● finalizează_task(nume) - se va sterge din dict
# ● afișează_todo_list() - doar cheile
# ● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
# printăm detalii suplimentare.
# ○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
# adauge.
# ○ Dacă acesta răspunde nu - la revedere
# ○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
# dict

class TodoList:
    def __init__(self):
        self.todo = {}
    def adauga_task(self, nume, descriere):
        self.todo[nume] = descriere
        print(self.todo)
    def finalizeaza_task(self, nume):
        if nume in self.todo:
            del self.todo[nume]
        else:
            print("Taskul nu exista in lista.")
    def afiseaza_todo_list(self):
        print(list(self.todo.keys()))

    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task in self.todo:
            print('Taskul exista deja')
        else:
            answer = input(f"Taskul '{nume_task}' nu exista in lista. Doresc sa-l adaug? (da/nu) ")
            if answer == "da":
                descriere = input("Introduceti detalii despre task:")
                self.todo[nume_task] = descriere
                print(self.todo)
            else:
                print("La revedere.")

TodoList1 = TodoList()
TodoList1.adauga_task('PM', 'QA')
TodoList1.finalizeaza_task('ok')
TodoList1.afiseaza_todo_list()
TodoList1.afiseaza_detalii_suplimentare('PM')
# TodoList2 = TodoList()
# TodoList2.adauga_task('PM', 'QA')
# TodoList2.finalizeaza_task('ok')
# TodoList2.afiseaza_todo_list()
# TodoList2.afiseaza_detalii_suplimentare('TEMA')