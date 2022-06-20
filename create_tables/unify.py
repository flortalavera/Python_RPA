import pandas as pd

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

print(mainTable)

# RECORDS TABLE

# CINES TABLE