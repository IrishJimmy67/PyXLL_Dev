import pandas as pd
import numpy as np
from pyxll import xl_macro, xl_app, Formatter, XLCell, xlcAlert, xl_menu
from win32com.client import constants
from dataclasses import dataclass


@xl_macro
def range_to_df():
    xlcAlert("Hello")
    xl = xl_app()

    # tempRange = 'B1'
    # tempRange2 = 'E2'
    # tempRange3 = 'A6:B7'
    # searchRange = 'A1:D4'
    #
    # x = pd.DataFrame({"A": ['Jim', 6], "B": ['Paula', 8]}, index=None)
    # arr_x = x.to_numpy()

    # 'xl' is an instance of the Excel.Application object

    # Get the current ActiveSheet (same as in VBA)
    sheet = xl.ActiveSheet

    # Call the 'Range' method on the Sheet
    xl_range = sheet.Range(tempRange)
    # xl_range = sheet.Range('A1:I1')
    # xl_range.Merge()
    xl_range.Select()
    # xl_range.FormulaR1C1 = "Test"
    xl_range.Formula = "=$B$2+$C$2"

    xl_range = sheet.Range(tempRange2)
    xl_range.Select()
    xl_range.Formula = "=MIN(COLUMN(" + searchRange + "))+COLUMNS(" + searchRange + ")-1"

    xl_range = sheet.Range(tempRange3)
    xl_range.Select()
    xl_range.Value = arr_x


# make a dataclass with decorator
@dataclass
class DataClassAccount:
    SNAM: str
    acc_cust: int


# make an object with values required by dataclass
DataClassObject = DataClass_Account("JLYONS", 123456)

# view dataclass object
print(DataClassObject)