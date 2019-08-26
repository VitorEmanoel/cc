poles_machine_rate = [1, 3, 2.5]

def print_head():
    print("[#] Calculadora para maquinas de poste")
    print("")
    print("[#] Maquinas ativas:", len(poles_machine_rate))

def user_input():
    return int(input("[+] Digite quantidade de dias de produção que deseja calcular: "))

def calc_result(days):
    production_per_day = 0
    for rate in poles_machine_rate:
        production_per_day += rate
    print("")
    print("[@] Por dua será produzido", production_per_day)
    print("[@] Durante", days, "será produzido", (production_per_day * days))

print_head()
calc_result(user_input())
