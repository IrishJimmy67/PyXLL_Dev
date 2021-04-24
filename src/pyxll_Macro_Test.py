
from pyxll import xl_macro, xl_app, Formatter, XLCell, xlcAlert
from win32com.client import constants


@xl_macro
def popup_messagebox():
    xlcAlert("Hello")
    xl = xl_app()

    tempRange = 'B1'
    tempRange2 = 'E2'
    searchRange = 'A1:D4'
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
# def format_cover_page():
#     app = xl_app()
#     selection = app.Selection.
#
#     formatter = Formatter
#
#     selection.rows("1:1").RowHeight = 41.25
# Range("A1:I1").Select
# ActiveCell.FormulaR1C1 = "Haverford Trust Portfolio Proposal"
# With
# Selection
# .HorizontalAlignment = xlCenter
# .VerticalAlignment = xlCenter
# .WrapText = False
# .Orientation = 0
# .AddIndent = False
# .IndentLevel = 0
# .ShrinkToFit = False
# .ReadingOrder = xlContext
# .MergeCells = False
# End
# With
# Selection.Merge
# With
# Selection
# .HorizontalAlignment = xlCenter
# .VerticalAlignment = xlCenter
# .WrapText = False
# .Orientation = 0
# .AddIndent = False
# .IndentLevel = 0
# .ShrinkToFit = False
# .ReadingOrder = xlContext
# .MergeCells = True
# End
# With
# With
# Selection.Interior
# .Pattern = xlSolid
# .PatternColorIndex = xlAutomatic
# .ThemeColor = xlThemeColorAccent1
# .TintAndShade = 0
# .PatternTintAndShade = 0
# End
# With
# With
# Selection.Font
# .Name = "Abadi"
# .Size = 24
# .Strikethrough = False
# .Superscript = False
# .Subscript = False
# .OutlineFont = False
# .Shadow = False
# .Underline = xlUnderlineStyleNone
# .ThemeColor = xlThemeColorDark1
# .TintAndShade = 0
# .ThemeFont = xlThemeFontMinor
# End
# With

    #add button and assign macro
    # ActiveSheet.Buttons.Add(336, 121.5, 93.75, 14.25).Select
    # Selection.OnAction = "Macro4"