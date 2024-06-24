pharmacies: list[dict] = [
    {'phar_name': 'Apteka Dr Max', 'phar_location': 'Warszawa'},
    {'phar_name': 'Super Apteka', 'phar_location': 'Legnica'},
    {'phar_name': 'Apteka Kartezjusza', 'phar_location': 'Lublin'},
    {'phar_name': 'Apteka Barnabas', 'phar_location': 'Toruń'},
    {'phar_name': 'Apteka Picipolo', 'phar_location': 'Chełm'}
]

patients: list[dict] = [
    {'pat_name': 'Mariusz', 'pat_surname': 'Kowalski', 'pat_pharmacy': 'Apteka Dr Max', 'pat_drug': 'Rutinoscrobin',
     'pat_location': 'Warszawa'},
    {'pat_name': 'Maryla', 'pat_surname': 'Bonkowska', 'pat_pharmacy': 'Apteka Kartezjusza',
     'pat_drug': 'Apap', 'pat_location': 'Lublin'},
    {'pat_name': 'Marian', 'pat_surname': 'Paluch', 'pat_pharmacy': 'DOZ Apteka Dbam o Zdrowie', 'pat_drug': 'Paracetamol',
     'pat_location': 'Warszawa'},
]

drugs: list[dict] = [
    {'drug_name': 'Apap', 'drug_location': 'Warszawa'},
    {'drug_name': 'Paracetamol', 'drug_location': 'Legnica'},
    {'drug_name': 'Rutinoscorbin', 'drug_location': 'Lublin'},
    {'drug_name': 'Renigast MAX', 'drug_location': 'Toruń'},
    {'drug_name': 'Altacet-ICE', 'drug_location': 'Chełm'}
]

workers: list[dict] = [
    {'worker_name': 'Mariusz Smagała','worker_pharmacy': 'Apteka Kartezjusza', 'worker_occupation':'Farmaceuta' },
    {'worker_name': 'Mariusz Śmigała','worker_pharmacy': 'Apteka Kartezjusza', 'worker_occupation':'Ochroniarz' },
    {'worker_name': 'Mariusz Skakała','worker_pharmacy': 'Apteka Kartezjusza', 'worker_occupation':'Sprzątacz' },
    {'worker_name': 'Dariusz Fajtłapa','worker_pharmacy': 'Super Apteka', 'worker_occupation':'Farmaceuta' },
    {'worker_name': 'Marcin Cwaniak','worker_pharmacy': 'Apteka Picipolo', 'worker_occupation':'Farmaceuta' },
    {'worker_name': 'Alfred Alberto','worker_pharmacy': 'Apteka Barnabas', 'worker_occupation':'Sprzątacz' },
    {'worker_name': 'Maksiu Kupiec','worker_pharmacy': 'Apteka Dr Max', 'worker_occupation':'Handlarz' },
]