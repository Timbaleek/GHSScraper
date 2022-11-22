import requests
from bs4 import BeautifulSoup
from googlesearch import search


# Made by Timbaleek

googleSearch = input("Google Suche: ")
wikiLink = next(search(googleSearch))  # Automatic Google Search URL

# Get the HTML from the URL
response = requests.get(
    url=str(wikiLink),
)
soup = BeautifulSoup(response.content, 'html.parser')

# title
#soup.find("span", {"class": "mw-page-title-main"}).get_text()
title = soup.find("span", {"class": "mw-page-title-main"}).text

#H and P
#fatherH = soup.find(text="H: ").parent
#hps = list(fatherH.descendants)

# GHS
print("\\HPStatements{" + title + "}{\\ghspic{exclam}\\\\\\\\}")
print("{\\begin{itemize}")

# H
hs = soup.select("#Vorlage_Infobox_Chemikalie > tbody:nth-child(1) > tr:nth-child(n) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > a:nth-child(n) > span:nth-child(1) > span:nth-child(1)")

for h in hs:
    print("\\item \\ghs{h}{" + h.text + "}")

print("\\end{itemize}}")

# P

print("{\\begin{itemize}")

ps = soup.select("#Vorlage_Infobox_Chemikalie > tbody:nth-child(1) > tr:nth-child(n) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-last-child(1) > td:nth-child(1) > a:nth-child(n) > span:nth-child(1) > span:nth-child(1)")

for p in ps:
    print("\\item \\ghs{p}{" + p.text + "}")

print("\\end{itemize}}")
print("{}")


# check if hp only contains numbers
# print(type(hp))
# if hp.string != None:
#    if hp.string.isnumeric():
#        print(hp.string)

#    print(" sdasdasd")

# GHS
# for hp in hps:
#    if (hp.get_text() == 'H'):
#        hp.getChildren().get_text()

#hazards = []
#precautions = []

#hazards = hazardString.split("-")
#precautions = precautionString.split("-")

# for hazard in hazards:
#    print(hazard)
