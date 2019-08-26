DOLAR = 4.13
EURO = 4.6

def print_menu():
    print("[#] Conversor de moedas")
    print("")
    print("[1] - Real para dolar")
    print("[2] - Real para euro")
    print("")

def read_menu_entry():
    menu_option = 0
    menu_option = int(input("[?] Escolha a sua opção: "))
    if (menu_option != 1 and menu_option != 2):
        print("")
        print("[X] Valor invalido")
        return read_menu_entry()
    return menu_option

def calc_to_euro(real):
    return real * EURO

def calc_to_dolar(real):
    return real * DOLAR

def user_option(option):
    if (option == 1):
        print("")
        return float(input("[1] Digite o valor em real a ser convertido para dolar: "))
    elif (option == 2):
        print("")
        return float(input("[2] Digite o valor em real a ser convertido para euro: "))

def calc_value(option, user_value):
    if (option == 1):
        print("")
        print("[1] R$", user_value, "em dolar é", calc_to_dolar(user_value), "$")
    elif (option == 2):
        print("")
        print("[2] R$", user_value, "em euro é", calc_to_euro(user_value))

def process_option(option):
    user_value = user_option(option)
    calc_value(option, user_value)

print_menu()
option = read_menu_entry()
process_option(option)
