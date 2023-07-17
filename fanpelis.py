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

    # Encontrar todas las etiquetas iframe
    iframes = soup.find_all('iframe')

    if iframes:
        # Extraer el valor del atributo data-src de cada etiqueta iframe y mostrarlo en pantalla
        for iframe in iframes:
            data_src = iframe.get('data-src')
            if data_src:
                print(data_src)
            else:
                print('No se encontró el atributo data-src en una etiqueta iframe.')
    else:
        print('No se encontraron etiquetas <iframe> en la página.')
else:
    print('La solicitud no fue exitosa. Código de estado:', response.status_code)
