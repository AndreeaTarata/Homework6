def cont_bancar(user, iban, pin, adresa, cont_economii, cont_credit):
    print(f'{user}')
    print(f'{iban}')
    print(f'{pin}')
    print(f'{adresa}')
    print(f'{cont_economii}')
    print(f'{cont_credit}')
    return 'cont activ'

def log_in(user, password):
    print(f'Please enter your user name: {user}')
    print(f'Please enter your user name: {password}')
    return 'sucessful login'

def generate_report(report):
    print(f'<h1>{report}</h1>')


log_in_status = log_in('Petre', 1234)
print(log_in_status)
generate_report(log_in_status)
x = cont_bancar('Popescu', 'TP100BTRL', 7777, 'Str. Raiului', 'RO1233', 'RO1300')
print(x)

