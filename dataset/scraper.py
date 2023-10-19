# This script finds liquipedia links in players.txt, traverses them to find team history, and stores it in a CSV file.
import requests
from bs4 import BeautifulSoup

URL = "https://liquipedia.net/counterstrike/MalbsMd"
r = requests.get(URL)

soup = BeautifulSoup(r.content, "html.parser")

teams = soup.find_all("div", attrs={"style": "font-size:100%; line-height:-10px;"})

ALLOWEDCHARS = [" ", "-", "?"]

for team in teams:
    date = team.findChildren("i")
    name = team.findChildren("a")
    if (
        len(date) > 1
    ):  # This indicates a player was inactive/benched on that team at the time
        continue
    date = "".join([c for c in date[0].text if c.isalnum() or c in ALLOWEDCHARS])
    name = "".join([c for c in name[0].text if c.isalnum() or c in ALLOWEDCHARS])

    print(name, date)
