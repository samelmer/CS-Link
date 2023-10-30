# This script finds liquipedia links in players.txt, traverses them to find team history, and stores it in a CSV file.
import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://liquipedia.net/counterstrike/MalbsMd"
r = requests.get(URL)

soup = BeautifulSoup(r.content, "html.parser")

teams = soup.find_all("div", attrs={"style": "font-size:100%; line-height:-10px;"})

ALLOWEDCHARS = ["?"]

for team in teams:
    date = team.findChildren("i")
    name = team.findChildren("a")
    if (
        len(date) > 1
    ):  # This indicates a player was inactive/benched on that team at the time
        continue
    parsedDate = "".join([c for c in date[0].text if c.isalnum() or c in ALLOWEDCHARS])
    parsedName = "".join(
        [c for c in name[0].text if c.isalnum() or c in ALLOWEDCHARS or c == " "]
    )

    try:
        joinDate = datetime.strptime(parsedDate[0:7], "%Y%m%d")
        leaveDate = datetime.strptime(parsedDate[-8:], "%Y%m%d")
        print(parsedName, joinDate, leaveDate)
    except Exception as e:
        print(e)

    print()
