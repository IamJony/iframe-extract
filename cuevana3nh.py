#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup

# Obtener la URL de la línea de comandos
url = sys.argv[1] 

response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener el contenido HTML de la página web
    html = response.text

    # Crear un objeto BeautifulSoup para analizar el HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar todas las etiquetas li clase clili
    lis = soup.find_all('li', class_='clili')
    if lis:
        # Extraer el valor del atributo data-video de cada etiqueta li y mostrarlo en pantalla
        for li in lis:
            data_video = li.get('data-video')
            if data_video:
                print(data_video)
            else:
                print('No se encontró el atributo data-video en una etiqueta li.')
    else:
        print('No se encontraron etiquetas <li con clases clili> en la página.')
else:
  print('La solicitud no fue exitosa. Código de estado:', response.status_code)
