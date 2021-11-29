import Domain_Storage
import pandas as pd
from bs4 import BeautifulSoup as bs
import random as rnd
import time as time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium_stealth import stealth
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import requests

s=Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

def getfile(file):
    global CheckFile
    CheckFile = file
    global df
    df = pd.read_csv(file)
    global urls
    urls = pd.Series(df['Listing URL'])

def get_soup(listing):
    time.sleep((rnd.randint(3000,5000)/1000))
    url = str(listing)
    driver.get(url)
    soup = bs(driver.page_source, 'html.parser')
    driver.close()
    global title
    title = str(soup.title).split('<title>')
    title = title[1]
    title = title.split('</title>')
    title = title[0]

def instantiate_driver():
    global driver
    driver = webdriver.Chrome(service=s, options=options, executable_path=r"C:\Users\DIPRAJ\Programming\adclick_bot\chromedriver.exe")
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
def get_domain(listing):
    global domain
    domain = listing.split('https://')
    domain = domain[1]
    domain = domain.split('/')
    domain = domain[0]

def currentlyChecking():
    global root
    root = Tk()
    root.title('Currently Checking')
    root.geometry('300x150')
    global progress
    root.update()
    progress = ttk.Progressbar(root, orient = HORIZONTAL,
              length = 250, mode = 'determinate')
    label = ttk.Label(root, text='Compliance Checker is Currently Running')
    global num_label
    num_label = ttk.Label(root, text='')
    label.grid()
    progress.grid()
    num_label.grid()
    root.update()

def save_new_file():
    file_path = str(CheckFile).split('/')
    file_name = file_path.pop()
    file_path = '/'.join(file_path)
    file_name = file_name.split('.csv')
    file_name = file_name[0] + ' (Checked using Compliance Checker).csv'
    file_path = file_path + '/' + file_name
    df.to_csv(path_or_buf = file_path, index=False)

def compliance_checker():
    global compliance
    compliance = []
    currentlyChecking()
    print(CheckFile)
    for listing in urls:
        instantiate_driver()
        get_soup(listing)
        get_domain(listing)
        Domain_Storage.create_domainarray()
        if domain in Domain_Storage.domainArray:
            if title == Domain_Storage.domainArray[domain]:
                compliance.append('d')
            elif str(requests.get(listing)) == '<Response [403]>':
                compliance.append(' ')
            else:
                compliance.append('u')
        else:
            compliance.append('No Title Trigger Stored')
        progress['value'] = ((len(compliance)/len(urls)) * 100)
        num_label['text']=str(len(compliance)) + '/' + str(len(urls))
        root.update()
    df['Compliance'] = compliance
    save_new_file()
