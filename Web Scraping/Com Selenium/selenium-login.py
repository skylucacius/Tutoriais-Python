from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException  
import os.path

# configurações de web Scraping
options = Options()
options.headless = True #deixarei como False para podermos visualizar o processo
options.add_argument("--window-size=400,400") # setar para a resolução da tela. Por ex. 1920 x 1200
ESTE_DIRETORIO = os.path.dirname(__file__).replace('\\','/') # em sistema linux, este último método deverá ser omitido, pois utiliza-se barra invertida como separador de pastas
PRINTSCR = ESTE_DIRETORIO + '/screenshot.png' # idem para este ...
DRIVER_PATH = ESTE_DIRETORIO + '/chromedriver.exe' # ... e este. Em Linux, substituir "/" por "\". Aqui, deve-se incluir o nome do diretório onde está o chromedriver.exe, juntamente com o nome do arquivo.

# configurações do site
SITE = "https://news.ycombinator.com/login" # site que vamos realizar o web scraping
USERNAME = '<nome de usuário no site>' # usuário que acessará o site
PASSWORD = '<senha no site>' # senha que acessará o site


driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get(SITE)
login = driver.find_element_by_xpath("//input").send_keys(USERNAME)
password = driver.find_element_by_xpath("//input[@type='password']").send_keys(PASSWORD)
submit = driver.find_element_by_xpath("//input[@value='login']").click()
try:
    logout_button = driver.find_element_by_id("logout")
    print('Successfully logged in')
    driver.execute_script('window.scrollBy(0,1000)') # rola a barra para baixo
    driver.save_screenshot(PRINTSCR) # tira um screenshot de uma tela 400 x 400
    
except NoSuchElementException:
    print('login/password incorreto(s)')