from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


driver.get("https://www.pro-football-reference.com/years/2019/fantasy.htm")

# Print title of website
print(driver.title)

# Extract lists of players based on xpath
player = driver.find_elements_by_xpath('//td[@data-stat="player"]')
team = driver.find_elements_by_xpath('//td[@data-stat="team"]') 
#print(player)

# Print out all players and teams on current page
num_players = len(player)
for i in range(num_players):
    print(player[i].text + " " + team[i].text)





driver.close()