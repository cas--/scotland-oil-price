#!/usr/bin/env python

def get_price_from_json():
    import requests

    resp = requests.get("https://www.boilerjuice.com/includes/priceChart.inc.php?a=4&ot=1&d=180&c=0&va=1&ex=1")
    try:
        data = resp.json()
    except Exception:
        return 'no price, problem with site?'
    return str(data['rows'][-1]['c'][-1]['v']) + 'p'


def get_price_from_soup():
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
        return 'nothing found, problem with page?'
    else:
        return td_price.text


def main():
    print(get_price_from_json())

if __name__ == '__main__':
    main()
