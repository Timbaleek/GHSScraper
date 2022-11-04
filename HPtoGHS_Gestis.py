import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

session = HTMLSession()

wikiLink = input("Sigma-Aldrich Link: ")
r = session.get(wikiLink)
r.html.render(sleep=1)
soup = BeautifulSoup(r.html.raw_html, "html.parser")

'''from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(
    "/usr/lib/chromium-browser/chromedriver", chrome_options=options)
driver.get(input("Google Suche: "))
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
assert "No results found." not in driver.page_source
driver.close()'''

# Made by Timbaleek

'''wikiLink = input("Google Suche: ")

# Get the HTML from the URL
response = requests.get(
    url=wikiLink, headers={'User-Agent': 'Chrome'}
)'''

# title
#title = soup.find("span", {"class": "mw-page-title-main"}).text

#H and P
#fatherH = soup.find(text="H: ").parent
#hps = list(fatherH.descendants)

# GHS
#print("\\HPStatements{" + title + "}{\\ghspic{exclam}\\\\\\\\}")
print("{\\begin{itemize}")

# print(soup.prettify())

# H
hs = soup.select(".app-article-view > div:nth-child(2) > div:nth-child(9) > div:nth-child(4) > div:nth-child(1) > table:nth-child(9) > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(1)")
# print(hs)

hList = list(hs[0].stripped_strings)
#hsString = hs.get_text(separator='\n', strip=True)
for h in hList:
    if (hSeparated[0] == 'H'):
        hSeparated = h.split(": ")

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
