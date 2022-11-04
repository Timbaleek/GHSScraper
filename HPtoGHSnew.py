import requests
from bs4 import BeautifulSoup
#from googlesearch import search
import json

# Made by Timbaleek

#googleSearch = input("Google Suche: ") + " Sigma-Aldrich"
# wikiLink = next(search(googleSearch))  # Automatic Google Search URL

wikilink = input("Sigma-Aldrich Link: ")

response = requests.get(
    url=wikilink, headers={'User-Agent': 'Chrome'}
)

print(response.url)
soup = BeautifulSoup(response.content, 'html.parser')

# print(soup.prettify())

data = soup.find('script', type='application/json').text
data = json.loads(data)

print(data)

print(data["props"]["pageProps"]["data"]["getProductDetail"]["name"])

print(data["props"]["pageProps"]["data"]
      ["getProductDetail"]["compliance"][2]["value"])

# title
#soup.find("span", {"class": "mw-page-title-main"}).get_text()
title = data["props"]["pageProps"]["data"]["getProductDetail"]["name"]


#H and P
#fatherH = soup.find(text="H: ").parent
#hps = list(fatherH.descendants)

# GHS
print("\\HPStatements{" + title + "}", end="")

# Images #TODO: correct JSON path
'''ghsImagesJson = data["props"]["pageProps"]["data"]["getProductDetail"]["compliance"][0]["value"]
imageString = ""
ghsImages = ghsImagesJson.split(",")
for image in ghsImages:
    imageString += "\\ghspic{" + image + "}"'''

print("{\\ghspic{exclam}\\\\\\\\}")

print("{\\begin{itemize}")

# H
hsString = data["props"]["pageProps"]["data"]["getProductDetail"]["compliance"][2]["value"]

hs = hsString.split(" - ")
for h in hs:

    print("\\item \\ghs{h}{" + h + "}")

print("\\end{itemize}}")

# P

print("{\\begin{itemize}")

psString = data["props"]["pageProps"]["data"]["getProductDetail"]["compliance"][3]["value"]

ps = psString.split(" - ")
for p in ps:
    print("\\item \\ghs{p}{" + p.replace(" ", "") + "}")

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
