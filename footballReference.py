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
'''fantasy_pos = driver.find_elements_by_xpath('//td[@data-stat="fantasy_pos"]') 
age = driver.find_elements_by_xpath('//td[@data-stat="age"]') 
gamesplayed = driver.find_elements_by_xpath('//td[@data-stat="g"]') 
gamesstarted = driver.find_elements_by_xpath('//td[@data-stat="gs"]') 
pass_cmp = driver.find_elements_by_xpath('//td[@data-stat="pass_cmp"]') 
pass_att = driver.find_elements_by_xpath('//td[@data-stat="pass_att"]') 
pass_yds = driver.find_elements_by_xpath('//td[@data-stat="pass_yds"]') 
pass_td = driver.find_elements_by_xpath('//td[@data-stat="pass_td"]') 
pass_int = driver.find_elements_by_xpath('//td[@data-stat="pass_int"]') 
rush_att = driver.find_elements_by_xpath('//td[@data-stat="rush_att"]') 
rush_yds = driver.find_elements_by_xpath('//td[@data-stat="rush_yds"]') 
rush_yds_per_att = driver.find_elements_by_xpath('//td[@data-stat="rush_yds_per_att"]') 
rush_td = driver.find_elements_by_xpath('//td[@data-stat="rush_td"]') 
targets = driver.find_elements_by_xpath('//td[@data-stat="targets"]') 
rec = driver.find_elements_by_xpath('//td[@data-stat="rec"]') 
rec_yds = driver.find_elements_by_xpath('//td[@data-stat="rec_yds"]') 
rec_yds_per_rec = driver.find_elements_by_xpath('//td[@data-stat="rec_yds_per_rec"]') 
rec_td = driver.find_elements_by_xpath('//td[@data-stat="rec_td"]') 
fumbles = driver.find_elements_by_xpath('//td[@data-stat="fumbles"]') 
fumbles_lost = driver.find_elements_by_xpath('//td[@data-stat="fumbles_lost"]') 
all_td = driver.find_elements_by_xpath('//td[@data-stat="all_td"]') 
two_pt_md = driver.find_elements_by_xpath('//td[@data-stat="two_pt_md"]') 
two_pt_pass = driver.find_elements_by_xpath('//td[@data-stat="two_pt_pass"]') 
fantasy_points = driver.find_elements_by_xpath('//td[@data-stat="fantasy_points"]') 
fantasy_points_ppr = driver.find_elements_by_xpath('//td[@data-stat="fantasy_points_ppr"]') 
draftkings_points = driver.find_elements_by_xpath('//td[@data-stat="draftkings_points"]') 
fanduel_points = driver.find_elements_by_xpath('//td[@data-stat="fanduel_points"]') 
vbd = driver.find_elements_by_xpath('//td[@data-stat="vbd"]') 
fantasy_rank_pos = driver.find_elements_by_xpath('//td[@data-stat="fantasy_rank_pos"]') 
fantasy_rank_overall = driver.find_elements_by_xpath('//td[@data-stat="fantasy_rank_overall"]') '''
#print(player)
players = []
teams = []
# Print out all players and teams on current page
num_players = len(player)
for i in range(num_players):
    teams.append(team[i].text)
    players.append(player[i].text)
#print(teams)

df = pd.DataFrame({"Player":players, "Team":teams})
print(df.head())





driver.close()