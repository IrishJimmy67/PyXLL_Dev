import pandas as pd
import configparser
import pyodbc
import sys
import plotly.graph_objects as go

from pyxll import xl_func, plot
import plotly.express as px

from pyxll import xl_func, DataFrameFormatter
from pyxll import xl_macro, xl_app, xlcAlert
from win32com.client import constants

from pandas import DataFrame
import psycopg2

#
# config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
# config.read('pyXLL_Test.ini')
# Debug_Mode = config.getboolean('SETTINGS', 'Debug_Mode')
# Con1_server = config['DATABASE SETTINGS']['Con1_server']
# Con1_database = config['DATABASE SETTINGS']['Con1_database']
# Con1_username = config['DATABASE SETTINGS']['Con1_username']
# Con1_password = config['DATABASE SETTINGS']['Con1_password']
# Con1_querystring = config['DATABASE SETTINGS']['Con1_querystring']

# conn = psycopg2.connect(
#     host="localhost",
#     database="JimsDB",
#     user="jlyons",
#     password="password")


@xl_func()
def python_func():
    return "Hello from Jimbo"


@xl_func("string[]:string[]")
def python_func2(ReportName):
    return ReportName

#
# @xl_func("string:string")
# def python_func2(ReportName):
#     return ReportName


@xl_func
def plotly_plot():
    # Get some sample data from plotly.express
    animals = ['giraffes', 'orangutans', 'monkeys']

    fig = go.Figure(data=[
        go.Bar(name='SF Zoo', x=animals, y=[20, 14, 23]),
        go.Bar(name='LA Zoo', x=animals, y=[12, 18, 29])
    ])
    # Change the bar mode
    fig.update_layout(barmode='group', width=500, height=250)
    fig.update_layout(margin=dict(l=20, r=20, t=20, b=20),)

    # Show the figure in Excel using pyxll.plot
    plot(fig)


# The DataFrameFormatter object can be used for format DataFrames returned to Excel from PyXLL.
df_formatter = DataFrameFormatter()


@xl_func(": dataframe<index=None, columns=True>", auto_resize=True,
         formatter=df_formatter)
def db_test():
    Con1_server = r'JIMS-LAPTOP\SQLEXPRESS'
    Con1_database = 'GJ_Dev'
    Con1_username = 'GJ_User'
    Con1_password = 'password'
    Con1_querystring = 'SELECT pk_id, ReportName FROM GJ_Report_Catalog'

    cnxn1 = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=' + Con1_server + ';DATABASE=' + Con1_database + ';UID=' + Con1_username + ';PWD=' + Con1_password)
    #cur = cnxn1.cursor()

    # cur = conn.cursor()
    #
    # cur.execute("""SELECT pk_id, report_type FROM public.report_type""")
    # query_results = cur.fetchall()
    # df_results = DataFrame(query_results)
    #
    # return df_results
    df_results = pd.read_sql(Con1_querystring, cnxn1)
    return df_results
    #print(dfAccounts.head(10))


@xl_macro("string ReportName:")
def py_macro3(ReportName="Demonstration Report"):
    # Get the Excel.Application instance
    xlcAlert("Hello from macro3")

    xl = xl_app()
#   xlcAlert("Orientation and Margins Begin")
    pic_path = "D:\Development\pyXll_Test\Haverford_CORP_TAG_B_resize.jpg"

    list_RHeader_Cells = [
        {"rangeStart": "J1", "rangeEnd": "N1", "H_Align": constants.xlRight, "V_Align": constants.xlTop, "IsBold": True},
        {"rangeStart": "J2", "rangeEnd": "N2", "H_Align": constants.xlRight, "V_Align": constants.xlTop, "IsBold": True},
        {"rangeStart": "J3", "rangeEnd": "N3", "H_Align": constants.xlRight, "V_Align": constants.xlTop, "IsBold": True},
        {"rangeStart": "J4", "rangeEnd": "N4", "H_Align": constants.xlRight, "V_Align": constants.xlTop, "IsBold": True},
        {"rangeStart": "J8", "rangeEnd": "N8", "H_Align": constants.xlRight, "V_Align": constants.xlTop, "IsBold": True}
    ]

    xl.ActiveSheet.PageSetup.Orientation = constants.xlLandscape

    xl.ActiveSheet.PageSetup.RightMargin = xl.InchesToPoints(0.25)
    xl.ActiveSheet.PageSetup.LeftMargin = xl.InchesToPoints(0.25)
    xl.ActiveSheet.PageSetup.TopMargin = xl.InchesToPoints(0.25)
    xl.ActiveSheet.PageSetup.BottomMargin = xl.InchesToPoints(0.25)
    xl.ActiveSheet.PageSetup.HeaderMargin = xl.InchesToPoints(0)
    xl.ActiveSheet.PageSetup.FooterMargin = xl.InchesToPoints(0)

#    xlcAlert("Orientation and Margins set!")

    # Get the active sheet
    sheet = xl.ActiveSheet

    # # Set Header Bar Colors
    Bar1_Range = sheet.Range('A6:N6')
    Bar1_Range.Select()
    setattr(xl.Selection.Interior, 'Color', 10053171)

    Bar2_Range = sheet.Range('A7:N7')
    Bar2_Range.Select()
    setattr(xl.Selection.Interior, 'Color', 14474460)

    xl_Rows = sheet.Rows("5:7")
    xl_Rows.Select()
    xl.Selection.RowHeight = 8.25

    xl_Rows = sheet.Rows("10:60")
    xl_Rows.Select()
    xl.Selection.RowHeight = 9.75

    # Call the 'Range' method on the Sheet
    # Merge all necessary cells

    for dic in list_RHeader_Cells:
        tmpRange = dic['rangeStart'] + ":" + dic['rangeEnd']
#        xlcAlert(tmpRange)
        xl_range = sheet.Range(tmpRange)
        xl_range.Select()
        setattr(xl_range, 'HorizontalAlignment', dic['H_Align'])
        setattr(xl.Selection.Font, 'Bold', dic['IsBold'])

        xl.Selection.Merge()

        xl.Selection.VerticalAlignment = constants.xlTop

    xl.ActiveSheet.Shapes.AddPicture(Filename=pic_path, LinkToFile=0, SaveWithDocument=-1,
                                     Left=1, Top=1, Width=170, Height=67)

    RepName_Range = sheet.Range('J8:N8')
    RepName_Range.Select()
    xl.ActiveCell.FormulaR1C1 = ReportName


if __name__ == "__main__":
    print(db_test())
#   macro3()



