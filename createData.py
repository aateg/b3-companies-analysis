from crawlers.fundamentus import getFundamentus
from crawlers.info import getSetor
import pandas as pd

def createData():
    """
    Essa função cria os dados a partir dos crawlers
    """
    
    #f = getFundamentus('balanco')
    #s = getSetor()
    
    #balance_data = pd.DataFrame(f)
    #sector_data = pd.DataFrame(s)
    
    #balance_data.to_csv('./data/balanco.csv', index = False)
    #sector_data.to_csv('./data/setor.csv', index = False)
    
    balance_data = pd.read_csv('./data/balanco.csv')
    sector_data = pd.read_csv('./data/setor.csv')
    
    balance_setor = pd.merge(balance_data, sector_data, on='ticker')
    
    return balance_setor
    