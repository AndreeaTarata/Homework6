# 1. Revizualizează întâlnirea 6 și ia notițe în caz că ți-a scăpat ceva.
# Pentru toate clasele, creați cel puțin 2 obiecte cu valori diferite și apelați toate
# metodele clasei.
# Te rog să scrii pe canalul de comunicare scrisă unde întâmpini dificultăți și te
# ajut.
# Dacă stai blocat > 30 min, cere indiciu.
#
# class Cerc:
#
#     def __init__(self, raza, culoare):
#         self._raza = raza
#         self._culoare = culoare
#
#     def descriere_cerc(self):
#         print(f'{self._culoare}, {self._raza}')
#
#     def aria(self):
#         aria = self._raza * self._raza
#         return aria
#
#     def diametru(self):
#         diametru = self._raza + self._raza
#
#         print(diametru)
#
#     def circumferinta(self):
#         circumferinta = 2 * 3.14159 * self._raza
#         print(circumferinta)
#
#
# cercul1 = Cerc(5, 'alb')
# cercul2 = Cerc(4, 'portocaliu')
# aria_cerc = cercul1.aria()
# print(aria_cerc)
# cercul1.descriere_cerc()
#
# print(cercul1.aria())
# cercul1.diametru()
# cercul1.circumferinta()
#
# cercul2.descriere_cerc()
#
# print(cercul2.aria())
# cercul2.diametru()
# cercul2.circumferinta()

# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
#
# self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
# descrie().

class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self._lungime = lungime
        self._latime = latime
        self._culoare = culoare
    def descrie(self):
        print(f'Dreptungiul are lungimea de {self._lungime}, si latimea {self._latime}, si culoarea {self._culoare}')
    def aria(self):
        print(self._lungime * self._latime)
    def perimetru(self):
        print(2*self._lungime + 2*self._latime)
    def schimba_culoarea(self, nou):
        self._culoare = nou

# drept1 = Dreptunghi(5, 3, 'alb')
# drept1.descrie()
# drept1.aria()
# drept1.perimetru()
# drept1.schimba_culoarea('rosu')
# drept1.descrie()
#
# drept2 = Dreptunghi(8, 4, 'albastru')
# drept2.descrie()
# drept2.aria()
# drept2.perimetru()
# drept2.schimba_culoarea('orange')
# drept2.descrie()

# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)

class Angajat:
    def __init__(self, nume, prenume, salariu):
        self._nume= nume
        self._prenume = prenume
        self._salariu = salariu
    def descrie(self):
        print(f'Numele angajatului este {self._nume} {self._prenume} si are {self._salariu}')
    def nume_complet(self):
        print(f'{self._nume}, {self._prenume}')
    def salariu_lunar(self):
        print(f'Salariu lunar: {self._salariu}')
    def salariu_anula(self):
        salariu_anual = 12*self._salariu
        print(f'Salariu anual este: {salariu_anual}')
    def marire_salariu(self, procent):

        marire_salariu = self._salariu + (procent*self._salariu/100)
        print(f'Salariul marit este: {marire_salariu}')

# angajata1 = Angajat('Andreea', 'Ion', 15000)
# angajata1.descrie()
# angajata1.nume_complet()
# angajata1.salariu_lunar()
# angajata1.salariu_anula()
# angajata1.marire_salariu(50)
#
# angajata2 = Angajat('Ioana', 'Marin', 15000)
# angajata2.descrie()
# angajata2.nume_complet()
# angajata2.salariu_lunar()
# angajata2.salariu_anula()
# angajata2.marire_salariu(50)

# 4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)

class Cont():
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are în contul {self.iban} suma de {self.sold} lei')
    def debitare_cont(self, suma1):
        print(f'{self.titular_cont} a adaugat {suma1}')
    def creditare_suma(self, suma2):
        print(f'{self.titular_cont} a scos {suma2}')

titular1 = Cont('RO123XX', 'Ion Magu', 10000)
titular1.afisare_sold()
titular1.debitare_cont(20)
titular1.creditare_suma(50)

titular2 = Cont('RO8888888TT', 'Raluca Ileana', 750000)
titular2.afisare_sold()
titular2.debitare_cont(2222)
titular2.creditare_suma(5555)