
import os
import pandas as pd
from win32com.client import Dispatch

xl = Dispatch("Excel.Application")

def checkDir():
    pathDir = 'C:\\RAJ_Vault\\Lean Cost\\FTS\\0FTS02081_LC.xlsx'
    if os.path.isfile(pathDir):
        print('yes')
        xl.Workbooks.Open(pathDir, ReadOnly=False)
        #xl.Workbooks(xlname).Worksheets("Sheet1").Activate()
        xl.Visible = 1
    else:
        print('no')

def openLC():
    pathLc = 'C:\\Adams\\Python\\SolidWorksFunctions\\0FTS02081.lc'
    if os.path.isfile(pathLc):
        print('yes')
        # open the file using open() function
        #file = open(pathLc)
        # Reading from file
        #print(file.read())
    else:
        print('no')

openLC()
