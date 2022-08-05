
import SW  # My file
import os
import ctypes
import pandas as pd
import win32com.client
from win32com.client import Dispatch
xl = Dispatch("Excel.Application")


def getSWfile():
    global SWfile
    fname = SW.RootName()
    fname = fname.split("\\")[-1]
    SWfile=fname.split("\\")[-1]
    return fname.split(".")[0] + ("_LC.xlsx")


def extractCost(yourFileName):
    df = pd.read_excel(yourFileName, sheet_name='Information')
    df1 = df.drop(df.index[[0, 1, 2]])
    df1 = df1.fillna("")
    df1 = df1.T
    obj = df1.loc[df1[4] == 'TOTAL (unit)']
    EstCost = obj.values[0][2]
    obj1 = df1.loc[df1[3] == 'BATCH']
    EstCostLot = obj1.values[0][2]
    SW.PropMgrSetProp("EstCost", EstCost)
    SW.PropMgrSetProp("EstCostLot", EstCostLot)
    ctypes.windll.user32.MessageBoxW(0, f"Estimate cost and lot size were added to {SWfile}", "Confirmation", 0)


def askForCost(costItem):
    '''If the Lean cost file does not exist, Send an e-mail asking for it to be created
    '''
    outlook = win32com.client.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = 'dummy_email@gmail.com'
    mail.Subject = 'Costing Requested'
    mail.HTMLBody = '<h3>This is HTML Body</h3>'
    mail.Body = f"Please provide a cost estimate for SolidWorks file {costItem}"
    mail.Send()

    ctypes.windll.user32.MessageBoxW(0, "A lean cost spreadsheet could not be found.\n \n"
                                        "An e-mail was sent requesting a cost estimate.", "Information", 0)


def find(name, path):
    xlFileExists=0
    for root, dirs, files in os.walk(path):
        for file in files:
            if name in file:
                xlFileExists=1
                ftarget= os.path.join(root, name)
    if xlFileExists:
        extractCost(ftarget)
    if not xlFileExists:
        askForCost(SWfile)


def openLC_XLfile():
    xl.Visible = True
    wb = xl.Workbooks.Open(ftarget)
    f = open(ftarget, "r")


if __name__ == '__main__':
    name=getSWfile()
    ftarget=find(name, 'c:\\RAJ_Vault\\')
