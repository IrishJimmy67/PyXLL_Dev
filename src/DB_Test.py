import pandas as pd
import configparser
import pyodbc

Con1_server = 'JIMS-LAPTOP\SQLEXPRESS'
Con1_database = 'GJ_Dev'
Con1_username = 'GJ_User'
Con1_password = 'password'
Con1_querystring = 'SELECT pk_id, ReportName FROM GJ_Report_Catalog'
Con1_querystring2 = "INSERT INTO [GJ_Scratch_Table]([TestValue]) VALUES ('Good Jimbo!')"
#Con1_querystring3 = "INSERT INTO [GJ_Scratch_Table]([TestValue]) VALUES (?)",'Good Jimbo2'




cnxn1 = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=' + Con1_server + ';DATABASE=' + Con1_database +
                       ';UID=' + Con1_username + ';PWD=' + Con1_password)
df_results = pd.read_sql(Con1_querystring, cnxn1)
print(df_results.head(10))

cursor = cnxn1.cursor()
#cursor.execute(Con1_querystring2)
cursor.execute("INSERT INTO [GJ_Scratch_Table]([TestValue]) VALUES (?)",'Good Jimbo2')

storedProc = "Exec [Test_Proc] @Test_Value = ?"
params = ("Good Jimbo3")

# Execute Stored Procedure With Parameters
cursor.execute(storedProc, params)

cnxn1.commit()

# cursor.execute("insert into products(id, name) values (?, ?)", 'pyodbc', 'awesome library')
# cnxn.commit()
# import psycopg2
# conn = psycopg2.connect(
#     host="localhost",
#     database="JimsDB",
#     user="jlyons",
#     password="password")
#
#
# cur = conn.cursor()
#
# cur.execute("""SELECT * FROM public.report_type""")
# query_results = cur.fetchall()
# print(query_results)
# print(type(query_results))