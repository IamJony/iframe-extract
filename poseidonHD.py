import sys
import requests
from bs4 import BeautifulSoup

# Obtener la URL de la línea de comandos
url = sys.argv[1]

# Hacer una solicitud GET a la página web
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener el contenido HTML de la página web
    html = response.text

    # Crear un objeto BeautifulSoup para analizar el HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Encontrar todos los elementos <ul> con la clase "idTabs sourceslist"
    ul_elements = soup.find_all('ul', class_='idTabs sourceslist')

    if ul_elements:
        for i, ul_element in enumerate(ul_elements):
            # Encontrar todas las etiquetas <a> dentro del elemento <ul>
            a_elements = ul_element.find_all('a')

            if a_elements:
                # Extraer el valor del atributo "video" de cada etiqueta <a> y mostrarlo en pantalla
                for a in a_elements:
                    video_url = a.get('video')
                    if video_url:
                        print(video_url)
                    else:
                        print('No se encontró el atributo "video" en una etiqueta <a>.')
            else:
                print('No se encontraron etiquetas <a> dentro del elemento <ul>.')

            # Imprimir un espacio en pantalla después de cada grupo de <ul>
            if i < len(ul_elements) - 1:
                print()
    else:
        print('No se encontraron elementos <ul> con la clase "idTabs sourceslist" en la página.')
else:
    print('La solicitud no fue exitosa. Código de estado:', response.status_code)
