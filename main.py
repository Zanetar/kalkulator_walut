def pln_eu():
    try:
        while True:
            pln=float(input('Wpisz ile PLN chcesz wymienić'))
            get=pln/4.67
            print(f'Dostajesz {get:.2f} eu')
            break
            return get
    except: print( 'Wybrałeś zły znak!')

def eu_pln():
    try:
        while True:
            eu=float(input('Wpisz ile EU chcesz wymienić'))
            get=eu*4.69
            print(f'Dostajesz {get:.2f} zł')
            break
        return get
    except:
        print('Wybrałeś zły znak!')


def pln_gbp():
    try:
        while True:
            pln = float(input('Wpisz ile PLN chcesz wymienić'))
            get = pln / 5.52
            print(f'Dostajesz {get:.2f} GBP')
            break
    except:
        print('Wybrałeś zły znak!')

def gbp_pln():
    try:
        while True:
            gbp=float(input('Wpisz ile GBP chcesz wymienić'))
            get=gbp*5.62
            print(f'Dostajesz {get:.2f} zł')
            break
    except: print('Wybrałeś zły znak!')

def menu():
    try:
        while True:
            print('Witaj w kalkulatorze walut')
            print('Co chcesz zrobić?')
            print('1. Zamiana PLN/EU')
            print('2. Zamiana EU/PLN ')
            print('3. Zamiana PLN/GBP')
            print('4. Zamiana GBP/PLN')
            print('x. Wyjście')
            choice=input('Dokonaj wyboru').upper()
            if choice=='X':
                print('Do widzenia')
                break
            else:
                choice=int(choice)
                if choice==1:
                    pln_eu()
                elif choice==2:
                    eu_pln()
                elif choice==3:
                    pln_gbp()
                elif choice==4:
                    gbp_pln()
                else:
                    print('Wybrałeś zły znak! Do widzenia')
                    break
    except: print('Wybrałeś zły znak! Do widzenia!')


menu() #wywołanie programu
