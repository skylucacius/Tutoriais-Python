# -*- encoding: utf-8 -*-
import requests
import pandas as pd
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import json
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

# Grab content from URL (Pegar conteúdo HTML a partir da URL)
url = "https://www.nba.com/stats/players/traditional/?sort=W&dir=-1"
top10ranking = {}

# rankings = {
#     '3points': {'field': 'FG3M', 'label': '3PM'},
#     'points': {'field': 'PTS', 'label': 'PTS'},
#     'assistants': {'field': 'AST', 'label': 'AST'},
#     'rebounds': {'field': 'REB', 'label': 'REB'},
#     'steals': {'field': 'STL', 'label': 'STL'},
#     'blocks': {'field': 'BLK', 'label': 'BLK'},
# }


# def buildrank(type):

#     field = rankings[type]['field']
#     label = rankings[type]['label']

#     driver.find_element_by_xpath(
#         f"//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='{field}']").click()

#     element = driver.find_element_by_xpath(
#         "//div[@class='nba-stat-table']//table")
#     html_content = element.get_attribute('outerHTML')

#     # Parse HTML (Parsear o conteúdo HTML) - BeaultifulSoup
#     soup = BeautifulSoup(html_content, 'html.parser')
#     table = soup.find(name='table')

#     # Data Structure Conversion (Estruturar conteúdo em um Data Frame) - Pandas
#     df_full = pd.read_html(str(table))[0].head(10)
#     df = df_full[['Unnamed: 0', 'PLAYER', 'TEAM', label]]
#     df.columns = ['pos', 'player', 'team', 'total']

#     # Convert to Dict (Transformar os Dados em um Dicionário de dados próprio)
#     return df.to_dict('records')

options = webdriver.ChromeOptions()
options.headless = False
driver = webdriver.Chrome(ChromeDriverManager().install() , options=options)
from time import sleep
driver.get(url)

driver.implicitly_wait(15)  # in seconds
# sleep(60)

seletor_xpath = lambda campo : f"//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='{campo}']"
pagina_html = "//div[@class='nba-stat-table']//table"

try:
    # driver.find_element_by_xpath(seletor_xpath("PTS")).click()
    elemento = driver.find_element_by_xpath("//div[@class='nba-stat-table']//table")
    tabela = elemento.get_attribute("outerHTML")
except NoSuchElementException as erro:
    print("elemento não encontrado: " + erro.msg)
except ElementClickInterceptedException as erro:
    print("Elemento foi interceptado por outro elemento: \n\n" + erro.msg)

driver.implicitly_wait(15)  # in seconds
# sleep(60)



# for k in rankings:
#     top10ranking[k] = buildrank(k)

driver.quit()

# # Dump and Save to JSON file (Converter e salvar em um arquivo JSON)
# with open('ranking.json', 'w', encoding='utf-8') as jp:
#     js = json.dumps(top10ranking, indent=4)
#     jp.write(js)











# Para esperar até que uma condição seja satisfeita dado um limite de tempo
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException

# delay = 3 # seconds
# try:
#     myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
#     print "Page is ready!"
# except TimeoutException:
#     print "Loading took too much time!"
