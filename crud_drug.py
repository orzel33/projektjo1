import folium
import requests
from bs4 import BeautifulSoup


def get_coords(drug_location):
    adres_url = f'https://pl.wikipedia.org/wiki/{drug_location}'
    response = requests.get(adres_url)
    response_html = BeautifulSoup(response.text, 'html.parser')
    latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
    longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
    print([latitude, longitude])
    return [latitude, longitude]


def read_drug(drugs) -> None:
    for index, drug in enumerate(drugs, start=1):
        print(f"{index}. {drug['drug_name']}, {drug['drug_location']}")
        print('________________________________________________________________________________')


def create_drug(drugs) -> None:
    drug_name: str = input('Podaj nazwę leku: ')
    drug_location: str = input('Podaj miasto, w którym znajduje się apteka, gdzie dostępny jest lek: ')
    drug: dict = {'drug_name': drug_name, 'drug_location': drug_location}
    drugs.append(drug)


def update_drug(drugs) -> None:
    index: int = int(input('Który lek edytować (podaj numer porządkowy)?: '))
    if 1 <= index <= len(drugs):
        drug = drugs[index - 1]
        new_drug_name = input('Wprowadź nową nazwę leku: ')
        new_drug_location = input('Wprowadź miasto, w którym znajduje się apteka, gdzie dostępny jest lek: ')
        drug['drug_name'] = new_drug_name
        drug['drug_location'] = new_drug_location
    else:
        print("Niepoprawny numer leku.")


def remove_drug(drugs: list[dict]) -> None:
    index: int = int(input('Który lek usunąć z listy? (podaj numer porządkowy): '))
    if 1 <= index <= len(drugs):
        drug = drugs[index - 1]
        drugs.remove(drug)


def show_drug_coords(drugs: list[dict]) -> None:
    index = int(input('Współrzędne której apteki, gdzie znajduje się lek chcesz poznać? (podaj numer porządkowy): '))
    if 1 <= index <= len(drugs):
        drug_location = drugs[index - 1]['drug_location']
        get_coords(drug_location)
    else:
        print("Podano niepoprawny numer leku.")

def drug_map(drugs):
    map = folium.Map(location=[52, 20], zoom_start=7)
    for drug in drugs:
        drug_name = drug['drug_name']
        drug_location = drug['drug_location']
        url = f"https://pl.wikipedia.org/wiki/{drug_location}"
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        print(
            f"Lekarstwo: {drug_name}, Lokalizacja: {drug_location}, Szerokość Geograficzna: {latitude}, Długość Geograficzna: {longitude}")
        folium.Marker(
            location=[latitude, longitude],
            popup=f"{drug_name},\n{drug_location}",
            icon=folium.Icon(color='purple')
        ).add_to(map)
    map.save('models/maps/map_drugs.html')