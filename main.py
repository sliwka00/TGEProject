import schedule
import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import shutil
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import win32com.client as win32
import pandas as pd
from datetime import datetime, timedelta
import datetime as dt
import schedule
import time
import numpy as np
import xlrd
import urllib.request
import requests
import sys
import getpass
import json
import schedule
import time
import lxml


sciezkaWebDriver=r"C:\Users\psliwa\PycharmProjects\Pobieranie_danych_tge\chromedriver.exe"  # do ściezki doklejam chromedriver, który wczesniej instaluje ze strony (sprawdź wersje chrome i sciągnij odpowiedni chromedriver)
# https://chromedriver.chromium.org/downloads     link do sciągniecia chromedrivera
ileDni=1
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #znalezione na stackoverflow: https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python
driver.get(sciezkaWebDriver)            #znalezione na stackoverflow
#driver = webdriver.Chrome(executable_path=sciezkaWebDriver)      pierwotny kod od Mateusza
d = datetime.today() - timedelta(days=int(ileDni))
dzien = d.strftime("%d-%m-%Y")
url = 'https://tge.pl/energia-elektryczna-otf?dateShow='+dzien+'&dateAction=prev'
page = driver.get(url)
time.sleep(1)
df = pd.read_html(driver.page_source, header = 0, decimal=",", thousands='.')
print(df[0])
df[0] = df[0].drop('Unnamed: 1',axis=1)
df = df[0]
print(df['Liczba kontraktów'])
df #wysietli gotowa ramke
