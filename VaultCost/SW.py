
import win32com.client
from win32com.client import Dispatch
global swApp
swApp = win32com.client.Dispatch("SldWorks.Application")


def RootName():
    '''Gets the full path name of the currently open SWorks document'''
    ActivePart()
    return swModel.getpathname


def ActivePart():
    global swModel
    swModel = swApp.ActiveDoc


def PropMgrSetProp(field,value):
    ActivePart()
    cpMgr = swModel.Extension.CustomPropertyManager("")
    if not cpMgr.Add2(field, 30,value):
        cpMgr.Set(field,value)
