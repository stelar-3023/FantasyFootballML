from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://www.pro-football-reference.com"
year = 2020
max_players = 300

# grab the first table
r = requests.get(url + "/years/" + str(year) + "/fantasy.htm")
soup = BeautifulSoup(r.content, "html.parser")
parsed_table = soup.find_all("table")[0]
#print(parsed_table)

df = []

# first 2 rows are col headers so skip them with [2:]
for i, row in enumerate(parsed_table.find_all("tr")[2:]):
    if i % 10 == 0: print(i, end=" ")
    if i >= max_players:
        print("\nComplete")
        break
    try:        
        data = row.find("td", attrs={"data-stat": "player"})
        name = data.a.get_text()
        stub = data.a.get("href")
        stub = stub[:-4] + "/fantasy/" + str(year)
        pos = row.find("td", attrs={"data-stat": "fantasy_pos"}).get_text()
        
        # grab this players stats
        statsdf = pd.read_html(url + stub)[0]
        
        # get rid of MultiIndex, just keep last row
        statsdf.columns = statsdf.columns.get_level_values(-1)
        
        # fix the away/home column
        statsdf = statsdf.rename(columns={"Unnamed: 4_level_2": "Away"})
        statsdf["Away"] = [1 if r=="0" else 0 for r in statsdf["Away"]]
        
        
        # drop "Total" row
        statsdf = statsdf.query('Date != "Total"')
        
        # add other info
        statsdf["Name"] = name
        statsdf["Position"] = pos
        statsdf["Season"] = year
        
        df.append(statsdf)
    except:
        pass
df = pd.DataFrame(statsdf)
#print(df.head())
print(df)

#df.to_csv(r"E:\\FantasyFootballML\\fantasy2020.csv")
    