import params as params
import req as req
import requests as requests
from bs4 import BeautifulSoup

payload = {
    "type": "ps",
    "ps_profession": "34",
    "ps_profession_label": "Médecin généraliste",
    "ps_localisation": "HERAULT (34)",
    "localisation_category": "departements",
}

#url = "http://annuairesante.ameli.fr/"
url = "http://annuairesante.ameli.fr/recherche.html"
header = {
    "User-Agent": "Mobzilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

req = requests.Session()

# page = req.get(url)

page = req.post(url, params=payload, headers=header)

if page.status_code == 200:
    lienrecherche = page.url

soup = BeautifulSoup(page.text, 'html.parser')

print(soup)

