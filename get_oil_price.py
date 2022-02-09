from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://www.boilerjuice.com/heating-oil-prices-scotland/'

options = webdriver.FirefoxOptions()
options.headless = True
# sudo apt install firefox-geckodriver
driver = webdriver.Firefox(options=options)
# Wait for graph to load
driver.implicitly_wait(4)
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
try:
    td_price = soup.find(id='chart_div').find_all('tr')[-1].find('td')
except (IndexError, AttributeError):
    print('nothing found, problem with page?')
else:
    print(td_price.text)
