import folium
import requests
from bs4 import BeautifulSoup


def get_coords(phar_location):
    adres_url = f'https://pl.wikipedia.org/wiki/{phar_location}'
    response = requests.get(adres_url)
    response_html = BeautifulSoup(response.text, 'html.parser')
    latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
    longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
    print([latitude, longitude])
    return [latitude, longitude]


def read_phar(pharmacies) -> None:
    for index, pharmacy in enumerate(pharmacies, start=1):
        print(f"{index}. {pharmacy['phar_name']} {pharmacy['phar_location']}")
        print('________________________________________________________________________________')


def create_phar(pharmacies) -> None:
    phar_name: str = input('Podaj nazwę apteki: ')
    phar_location: str = input('Podaj miasto, w którym znajduje się apteka: ')
    pharmacy: dict = {'phar_name': phar_name, 'phar_location': phar_location}
    pharmacies.append(pharmacy)


def update_phar(pharmacies) -> None:
    index: int = int(input('Którą aptekę edytować (podaj numer porządkowy)?: '))
    if 1 <= index <= len(pharmacies):
        pharmacy = pharmacies[index - 1]
        new_phar_name = input('Wprowadź nową nazwę apteki: ')
        new_phar_location = input('Wprowadź miasto, w którym znajduje się apteka: ')
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
        get_coords(phar_location)
    else:
        print("Podano niepoprawny numer apteki.")


def showcase_workers(workers):
    pharm_name = input('Pracowników jakiej apteki chcesz zobaczyc? Podaj jej nazwę: ')
    worker_pharmacy = [worker for worker in workers if
                       worker['worker_pharmacy'] == pharm_name]
    if not worker_pharmacy:
        print('Ta apteka nie ma żadnych pracowników, którzy są zarejstrowani: ')
    else:
        for worker in worker_pharmacy:
            print(f" Imie i nazwisko: {worker['worker_name']}   Posada:{worker['worker_occupation']}")


def phar_map(pharmacies):
    map = folium.Map(location=[52, 20], zoom_start=7)
    for pharmacy in pharmacies:
        phar_name = pharmacy['phar_name']
        phar_location = pharmacy['phar_location']
        url = f"https://pl.wikipedia.org/wiki/{phar_location}"
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        print(
            f"Apteka: {phar_name}, Lokalizacja: {phar_location}, Szerokość Geograficzna: {latitude}, Długość Geograficzna: {longitude}")
        folium.Marker(
            location=[latitude, longitude],
            popup=f"{phar_name},\n{phar_location}",
            icon=folium.Icon(color='red')
        ).add_to(map)
    map.save('models/maps/map_pharmacies.html')
