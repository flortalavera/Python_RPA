import datetime
from create_tables.db import engine
from create_tables.unify import mainTable, totalRecordsTable, convertTableCines

# Add Datatime column to each table
uploadDate = datetime.datetime.today()
totalRecordsTable['Fecha de carga'] = uploadDate
convertTableCines['Fecha de carga'] = uploadDate
mainTable['Fecha de carga'] = uploadDate

# Replace null value
totalRecordsTable.fillna('nulo', inplace = True)
convertTableCines.fillna('nulo', inplace = True)
mainTable.fillna('nulo', inplace = True)

# Create tables in Data Base
mainTable.to_sql('Main_table', con=engine, if_exists="replace", index=False)

totalRecordsTable.to_sql('Records_table', con=engine, if_exists="replace", index=False)

convertTableCines.to_sql('Cines_table', con=engine, if_exists="replace", index=False)