import requests
from bs4 import BeautifulSoup


def get_coords(pat_location):
    adres_url = f'https://pl.wikipedia.org/wiki/{pat_location}'
    response = requests.get(adres_url)
    response_html = BeautifulSoup(response.text, 'html.parser')
    latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
    longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
    print([latitude, longitude])
    return [latitude, longitude]


def read_pat(patients) -> None:
    for index, patient in enumerate(patients, start=1):
        print(f"{index}. {patient['pat_name']} {patient['pat_surname']} {patient['pat_location']}")
        print('________________________________________________________________________________')


def create_pat(patients) -> None:
    pat_name: str = input('Podaj imie pacjenta: ')
    pat_surname: str = input('Podaj nazwisko pacjenta: ')
    pat_location: str = input('Podaj miasto, w którym pacjent korzysta z apteki: ')
    patient: dict = {'pat_name': pat_name, 'pat_surname': pat_surname, 'pat_location': pat_location}
    patients.append(patient)


def update_pat(patients) -> None:
    index: int = int(input('Dane którego pacjenta edytować(podaj numer porządkowy)?: '))
    if 1 <= index <= len(patients):
        patient = patients[index - 1]
        new_pat_name = input('Wprowadź nowe imie pacjenta: ')
        new_pat_surname = input('Wprowadź nowe nazwisko pacjenta: ')
        new_pat_location = input('Wprowadź miasto, w którym pacjent korzysta z apteki: ')
        patient['pat_name'] = new_pat_name
        patient['pat_surname'] = new_pat_surname
        patient['pat_location'] = new_pat_location
    else:
        print("Niepoprawny numer pacjenta.")


def remove_pat(patients: list[dict]) -> None:
    index: int = int(input('Którą aptekę usunąć z listy? (podaj numer porządkowy): '))
    if 1 <= index <= len(patients):
        patient = patients[index - 1]
        patients.remove(patient)


def show_pat_coords(patients: list[dict]) -> None:
    index = int(input('Współrzędne której apteki chcesz poznać? (podaj numer porządkowy): '))
    if 1 <= index <= len(patients):
        pat_location = patients[index - 1]['pat_location']
        get_coords(pat_location)
    else:
        print("Podano niepoprawny numer pacjenta.")
