import requests;
from bs4 import BeautifulSoup;
import pandas as pd

url = "https://listado.mercadolibre.com.ar/celulares#D[A:celulares,L:undefined]"

response= requests.get(url)

if response.status_code== 200:
    soup = BeautifulSoup(response.text, 'html.parser') #convierte la devolucion en un texto y lo parsea
    productos= soup.find_all('div', class_="ui-search-result__wrapper") #a esa devolucion voy a buscar un div y que tenga la propiedad class que sea igual a lo que le paso
    lista_productos=[]

    for producto in productos:
        titulo=producto.find('h2', class_="poly-box poly-component__title") #que por cada producto en productos busque un h2 con la siguiente clase(titulo)
        marca=producto.find('span', class_="poly-component__brand")
        precio= producto.find('span', class_="andes-money-amount__fraction")

        if titulo and precio:
            datos_producto={
                'Titulo': titulo.text.strip(),
                'Marca': marca.text.strip() if marca else 'N/A',
                'Precio': precio.text.strip()
            }
            lista_productos.append(datos_producto)
        
    df= pd.DataFrame(lista_productos)
    
    
    
else:
    print("Error al cargar via web, codigo:", response.status_code)