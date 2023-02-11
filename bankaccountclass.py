class BankAccount:
    bank_name = 'Banca Transilvania'

    def __init__(self, user, pwd):  # constructorul face un tipar - pot sa definesc atribute de instanta
        self._user = user
        self._pwd = pwd

    def cont_bancar(self, iban, adresa, cont_economii, cont_credit):
        print(f'{self._user}')
        print(f'{iban}')
        print(f'{self._pwd}')
        print(f'{adresa}')
        print(f'{cont_economii}')
        print(f'{cont_credit}')
        return 'cont activ'

    def log_in(self):
        print(self.bank_name)
        print(BankAccount.bank_name)
        return f'{self._user} log_in with {self._pwd}'

    def interogare_sold(self, sold):
        status_log_in = self.log_in()
        if status_log_in == 'Andreea log_in with 0000':
            print(f'Soldul {self._user} este {sold}')
        else:
            print('user inexistent')

    @staticmethod
    def curs_valutar(moneda): # static metod care nu este dependent de cont
        if moneda == 'EURO':
            print('4.94')
        elif moneda == 'USD':
            print('4.5')
        else:
            print('curs inexistent pentru aceasta moneda')


user = input('please enter username: ')
pwd = input('please enter password: ')
bank_account_John = BankAccount(user, pwd)  # obiect
bsnk_account_Marry = BankAccount('Ion', '2222')
bank_account_John.cont_bancar('TP100BTRL', 'Str. Raiului', 'RO1233', 'RO1300')  # metode
bsnk_account_Marry.cont_bancar('TP200BTRL', 'Str. Rai', 'RO1233', 'R300')

bank_account_John.log_in()
log_in_status = bank_account_John.log_in()
print(log_in_status)
bank_account_John.interogare_sold(2000000)
bank_account_John.curs_valutar('EURO')

# TODO o clasa pentru un producator de masini