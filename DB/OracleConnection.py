import cx_Oracle
import config
import pandas as pd

connection = None
try:
    connection = cx_Oracle.connect(
        "hr",
        "hr",
        "xe",
        encoding='UTF-8')

    # show the version of the Oracle Database
    print(connection.version)
    df = pd.read_sql('select * from employees',connection)
    print(df.head())
except cx_Oracle.Error as error:
    print(error)
finally:
    # release the connection
    if connection:
        connection.close()
