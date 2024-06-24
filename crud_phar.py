import requests


def get_coordinates(phar_location):
    url = f'https://nominatim.openstreetmap.org/search?format=json&q={phar_location}'
    response = requests.get(url)
    data = response.json()
    if data and len(data) > 0:
        first_result = data[0]
        lat = float(first_result['lat'])
        lon = float(first_result['lon'])
        print(f"Latitude: {lat}")
        print(f"Longitude: {lon}")
        return [lat, lon]
    else:
        print("Nie udało się znaleźć współrzędnych dla podanej lokalizacji.")
        return None


def read_phar(pharmacies) -> None:
    for index, pharmacy in enumerate(pharmacies, start=1):
        print(f"{index}. {pharmacy['phar_name']}, {pharmacy['phar_location']}")
        print('________________________________________________________________________________')


def create_phar(pharmacies) -> None:
    phar_name: str = input('Podaj nazwę apteki: ')
    phar_location: str = input('Podaj adres i kod pocztowy apteki: ')
    pharmacy: dict = {'phar_name': phar_name, 'phar_location': phar_location}
    pharmacies.append(pharmacy)


def update_phar(pharmacies) -> None:
    index: int = int(input('Którą aptekę edytować (podaj numer porządkowy)?: '))
    if 1 <= index <= len(pharmacies):
        pharmacy = pharmacies[index - 1]
        new_phar_name = input('Wprowadź nową nazwę apteki: ')
        new_phar_location = input('Wprowadź nowy adres i kod pocztowy apteki: ')
        pharmacy['phar_name'] = new_phar_name
        pharmacy['phar_location'] = new_phar_location
    else:
        print("Niepoprawny numer apteki.")


def remove_phar(pharmacies: list[dict]) -> None:
    index: int = int(input('Którą aptekę usunąć z listy? (podaj numer porządkowy): '))
    if 1 <= index <= len(pharmacies):
        pharmacy = pharmacies[index - 1]
        pharmacies.remove(pharmacy)


def show_phar_coords(pharmacies: list[dict]) -> None:
    index = int(input('Współrzędne której apteki chcesz poznać? (podaj numer porządkowy): '))
    if 1 <= index <= len(pharmacies):
        phar_location = pharmacies[index - 1]['phar_location']
        get_coordinates(phar_location)
    else:
        print("Podano niepoprawny numer apteki.")
