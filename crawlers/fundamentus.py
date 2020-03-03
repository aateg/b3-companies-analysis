import requests
from bs4 import BeautifulSoup
from crawlers.tickers import getTickers
from crawlers.info import getInfo

def getFundamentus(table='fundamentalista'):
    base_url = 'https://www.fundamentus.com.br/detalhes.php?papel='

    table_index = {
        'fundamentalista': 2,
        'balanco': 3,
        'demonstrativo': 4
    }
    tickers = list(getTickers())

    data = []
    
    for ticker in tickers:
        
        print(f'Requisitando dados {ticker} ...')

        try:
            url = base_url + ticker
            response = requests.get(url)

            soup = BeautifulSoup(response.content, 'html.parser')

            alltables = soup.find_all('table', 'w728')
            t = alltables[table_index[table]]

            label = t.find_all('td', {'class': 'label'})
            content = t.find_all('td', {'class': 'data'})
        except:
            continue

        ticker_data = {}
        for l, c in zip(label, content):
            data_label = l.find('span', {'class': 'txt'}).getText()
            data_content = c.getText()
            if fix_string(data_label):
                ticker_data[data_label] = string_to_float(data_content)
        ticker_data['ticker'] = ticker

        data.append(ticker_data)

    return data

def string_to_float(string):
    is_percentage = True if '%' in string else False
    replaced_string = string.replace('\n', '') \
        .replace('%', '').replace(' ', '').replace('.', '').replace(',', '.')
    if replaced_string == '-':
        return 0.0
    if is_percentage:
        return float(replaced_string) / 100
    return float(replaced_string)

def fix_string(string):
    return string.replace(' ', '').replace('\n', '')