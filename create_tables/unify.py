import pandas as pd
from db import engine

bibliotecas_file = "C:\\Cursos\\Python\\Calyx\\challengeCalyx\\input_files\\bibliotecas\\2022-junio\\bibliotecas-20-06-2022.csv"
cines_file = "C:\\Cursos\\Python\\Calyx\\challengeCalyx\\input_files\\cines\\2022-junio\\cines-20-06-2022.csv"
museos_file = "C:\\Cursos\\Python\\Calyx\\challengeCalyx\\input_files\\museos\\2022-junio\\museos-20-06-2022.csv"


print("*** Merging multiple csv files into a single pandas dataframe ***")

# MERGE FILES
mainDataFrame = pd.concat(
    map(pd.read_csv, [bibliotecas_file, cines_file, museos_file]), ignore_index=True)


# MAIN TABLE
mainTable = mainDataFrame[['Cod_Loc', 'IdProvincia', 'IdDepartamento',
'Categoría', 'Provincia', 'Localidad', 'Nombre', 'Domicilio', 'CP', 'Teléfono',
'Mail', 'Web']]


# FOR PROVINCE AND CATEGORY
mainTable['total_registros_Prov_Categ'] = mainTable['Provincia'] + mainTable['Categoría']
mainTable['total_registros_fuente'] = mainDataFrame['Fuente']
mainTable['total_registros_categoria'] = mainTable['Categoría']

totalRecordsTable = mainTable[['total_registros_categoria', 'total_registros_fuente', 'total_registros_Prov_Categ']]


# CINES TABLE
cinesDataFrame = pd.read_csv(cines_file)
convertTableCines = cinesDataFrame[['Provincia', 'Pantallas', 'Butacas', 'espacio_INCAA']]


# Create tables in Data Base
mainDataFrame.to_sql('Main_table', con=engine, if_exists="replace", index=False)

totalRecordsTable.to_sql('Records_table', con=engine, if_exists="replace", index=False)

convertTableCines.to_sql('Cines_table', con=engine, if_exists="replace", index=False)