import Checker
import Domain_Storage
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root = Tk()

def opencustomize():
    global customizeWindow
    customizeWindow = Toplevel(root)
    customizeWindow.title('Domains To Check')
    customizeWindow.geometry('400x400')
    Domain_Storage.create_domainlist(customizeWindow)
    new_domain = ttk.Button(customizeWindow, text='Add New Domain', command=lambda: openNewDomain())
    new_domain.grid()
    customizeWindow.focus()

def openNewDomain():
    newDomain = Toplevel(root)
    newDomain.title('Add a New Domain')
    newDomain.geometry('300x300')
    domain_label = ttk.Label(newDomain, text="New Domain")
    domainInpt = ttk.Entry(newDomain)
    trigger_labl = ttk.Label(newDomain, text='New Trigger')
    triggerInpt = ttk.Entry(newDomain)
    domain_label.grid()
    domainInpt.grid()
    trigger_labl.grid()
    triggerInpt.grid()
    submitButton = ttk.Button(newDomain, text='Create New Domain Trigger', command=lambda: Domain_Storage.newDomain(domainInpt.get(), triggerInpt.get()))
    submitButton.grid()

def getFile():
    global file
    file = filedialog.askopenfilename(title = 'Select a CSV', filetype = [('Excel files', '.csv')])
    Checker.getfile(file)
    button3 = button = ttk.Button(root, text='Start Compliance Checker', command=lambda: Checker.compliance_checker())
    button3.grid()
    file_label = ttk.Label(root, text="File Selected")
    file_label.grid()

def startup():
    root.title("Compliance Checker")
    mainframe = ttk.Frame(root, padding='3 3 12 12')
    mainframe = ttk.Frame(root, padding= "3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    button = ttk.Button(mainframe, text='Select File', command=lambda: getFile())
    button2 = ttk.Button(mainframe, text='Customize', command=lambda: opencustomize())

    button.grid()
    button2.grid()

    root.mainloop()

startup()
