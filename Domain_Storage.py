import os.path
from tkinter import ttk
from tkinter import *
from tkinter import scrolledtext
from os.path import exists
import pandas as pd
from csv import writer

def check_create_file():
    if os.path.exists('domain.csv'):
        domain_df = pd.read_csv(encoding="utf-32", filepath_or_buffer='domain.csv')
    else:
        domain = []
        trigger = []
        dict = {'Domain': domain, 'Trigger': trigger}
        dom_frame = pd.DataFrame(dict)
        dom_frame.to_csv('domain.csv')

def create_domainlist(customizeWindow):
    check_create_file()
    domainArea = 'Domain              Title Trigger\n'
    domain_df = pd.read_csv('domain.csv')
    domains = pd.Series(domain_df['Domain'])
    triggers = pd.Series(domain_df['Trigger'])
    domainList = []
    triggerList = []
    for domain in domains:
        domainList.append(domain)
    for trigger in triggers:
        triggerList.append(trigger)
    for domain in domainList:
        domainArea = domainArea + domain + " -----> " + triggerList[domainList.index(domain)] + "\n"

    text_area = scrolledtext.ScrolledText(customizeWindow,
                                      wrap = WORD,
                                      width = 40,
                                      height = 10,
                                      font = ("Times New Roman",
                                              15))
    text_area.grid(column = 0, pady = 10, padx = 10)
    text_area.insert(INSERT, domainArea)
    text_area.configure(state='disabled')

def newDomain(domain, trigger):
    new_domain_dict = {'domain': [domain], 'trigger': [trigger]}
    new_domain = pd.DataFrame(data=new_domain_dict)
    new_domain.to_csv('domain.csv', mode='a', header=False, index=False)

def create_domainarray():
    domain_df = pd.read_csv('domain.csv')
    domains = pd.Series(domain_df['Domain'])
    triggers = pd.Series(domain_df['Trigger'])
    domainList = []
    triggerList = []
    for domain in domains:
        domainList.append(domain)
    for trigger in triggers:
        triggerList.append(trigger)
    zipped = zip(domainList, triggerList)
    global domainArray
    domainArray = dict(zipped)
