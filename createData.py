from crawlers.fundamentus import Fundamentus
import pandas as pd

def getFundamentus(data='balanco'):
    f = Fundamentus()
    info = getInfo()
    f.get(table=data)

    data = f.data

def getInfo():
    pass
