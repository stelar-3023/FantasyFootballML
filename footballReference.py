from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

url = "https://www.pro-football-reference.com/years/2019/fantasy.htm"

driver.get(url)

# Print title of website
print(driver.title)

# Extract lists of players based on xpath
players = driver.find_elements_by_xpath('//td[@data-stat="player"]')

# create empty array to store data
data = []

# loop over players
for player in players:
    player_name = player.text
    data.append({"Player": player_name})
    
# close driver
driver.quit()

# save to pandas dataframe    
df = pd.DataFrame(data)
print(df.head())

# write to csv
df.to_csv(r"E:\\FantasyFootballML\\player.csv")