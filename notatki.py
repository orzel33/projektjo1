import folium
import requests
from bs4 import BeautifulSoup

from models.data import pharmacies


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
            icon=folium.Icon(color='green')
        ).add_to(map)
    map.save('models/maps/map_pharmacies.html')


