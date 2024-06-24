from models.data import pharmacies
from crud_phar import read_phar, create_phar, update_phar, remove_phar, show_phar_coords

if __name__ == '__main__':
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
