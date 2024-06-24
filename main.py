from models.data import pharmacies, drugs, patients, workers
from crud_phar import read_phar, create_phar, update_phar, remove_phar, show_phar_coords, showcase_workers
from crud_drug import read_drug, remove_drug, update_drug, create_drug, show_drug_coords
from crud_pat import read_pat, create_pat, update_pat, remove_pat, show_pat_coords, pat_showcase


if __name__ == '__main__':
    print('Logowanie')
    print('Login: Nazwisko twórcy')
    print('Hasło: grupa wydzialowa')
    print('')

    Login = "ORŁOWSKI"
    Haslo = "WIG23GW3S0"
    login: str = input("Podaj login:")
    haslo: str = input("Podaj haslo:")
    if Login == login and Haslo == haslo:
        print("Sukces")
    else:
        print("Błędny login lub haslo")
        login: str = input("Podaj login:")
        haslo: str = input("Podaj haslo:")

    print('Witaj użytkowniku!')
    while True:
        print('Menu:')
        print('0. Zakończ program')
        print('1. Pokaż listę aptek')
        print('2. Pokaż listę leków')
        print('3. Pokaż listę pacjentów')
        menu_option = input('Wybierz dostępną funkcję z menu: ')

        if menu_option == '0':
            break

        elif menu_option == '1':
            print('Lista dostępnych aptek wygląda następująco:')
            read_phar(pharmacies)
            print('0. Cofnij')
            print('1. Edytuj dane apteki')
            print('2. Dodaj nową aptekę do listy')
            print('3. Usuń aptekę z listy')
            print('4. Sprawdź współrzędne apteki')
            print('5. Pokaż listę pacjentów zarejestrowanych w aptece: ')
            print('6. Pokaż listę pracowników aptece: ')
            sub_menu1_option = input('Wybierz dostępną funkcję z menu: ')

            if sub_menu1_option == '0':
                continue

            elif sub_menu1_option == '1':
                update_phar(pharmacies)
                print('Edytowano')

            elif sub_menu1_option == '2':
                create_phar(pharmacies)
                print('Dodano nową aptekę')

            elif sub_menu1_option == '3':
                remove_phar(pharmacies)
                print('Usunięto. ')

            elif sub_menu1_option == '4':
                show_phar_coords(pharmacies)

            elif sub_menu1_option == '5':
                pat_showcase(patients)

            elif sub_menu1_option == '6':
                showcase_workers(workers)

        elif menu_option == '2':
            print('Lista dostępnych leków, i miast gdzie są dostępne wygląda następująco:')
            read_drug(drugs)
            print('0. Cofnij')
            print('1. Edytuj dane leku')
            print('2. Dodaj nowy lek do listy')
            print('3. Usuń lek z listy')
            print('4. Sprawdź współrzędne miasta, w którym dostępny jest lek: ')
            sub_menu2_option = input('Wybierz dostępną funkcję z menu: ')

            if sub_menu2_option == '0':
                continue

            elif sub_menu2_option == '1':
                update_drug(drugs)
                print('Edytowano')

            elif sub_menu2_option == '2':
                create_drug(drugs)
                print('Dodano nową aptekę')

            elif sub_menu2_option == '3':
                remove_drug(drugs)
                print('Usunięto. ')

            elif sub_menu2_option == '4':
                show_drug_coords(drugs)

        elif menu_option == '3':
            print('Lista klientów wygląda następująco:')
            read_pat(patients)
            print('0. Cofnij')
            print('1. Edytuj dane pacjenta')
            print('2. Dodaj nowego pacjenta')
            print('3. Usuń pacjenta z listy')
            print('4. Sprawdź współrzędne miasta, gdzie przyjmowany jest pacjent: ')
            sub_menu3_option = input('Wybierz dostępną funkcję z menu: ')

            if sub_menu3_option == '0':
                continue

            elif sub_menu3_option == '1':
                update_pat(patients)
                print('Edytowano')

            elif sub_menu3_option == '2':
                create_pat(patients)
                print('Dodano nową aptekę')

            elif sub_menu3_option == '3':
                remove_pat(patients)
                print('Usunięto. ')

            elif sub_menu3_option == '4':
                show_pat_coords(patients)
