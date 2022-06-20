import requests
import pandas as pd
import io
from pathlib import Path

urlMuseos = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv"
urlCines = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv"
urlBibliotecas = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv"

# MUSEOS
getInformationMuseos = requests.get(urlMuseos).content
readFileMuseos = pd.read_csv(io.StringIO(getInformationMuseos.decode('utf-8')))

filepath = Path('museos/2022-junio/museos-20-06-2022.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
readFileMuseos.to_csv(filepath) 

# CINES
getInformationCines = requests.get(urlCines).content
readFileCines = pd.read_csv(io.StringIO(getInformationCines.decode('utf-8')))

filepath = Path('cines/2022-junio/cines-20-06-2022.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
readFileCines.to_csv(filepath)

# BIBLIOTECAS
getInformationBibliotecas = requests.get(urlBibliotecas).content
readFileBibliotecas = pd.read_csv(io.StringIO(getInformationBibliotecas.decode('utf-8')))

filepath = Path('bibliotecas/2022-junio/bibliotecas-20-06-2022.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
readFileBibliotecas.to_csv(filepath)