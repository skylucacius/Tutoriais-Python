from bs4 import BeautifulSoup
import requests
html = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp").content
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())
try:
    temperatura_minima = soup.find("span", id="min-temp-1").string
    temperatura_maxima = soup.find("span", id="max-temp-1").string
    print("a temperatura máxima é: " + temperatura_maxima + "C")
    print("a temperatura mínima é: " + temperatura_minima + "C")
except Exception as e:
    print(e)
    