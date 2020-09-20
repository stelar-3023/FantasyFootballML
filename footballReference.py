from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.pro-football-reference.com/")
print(driver.title)
