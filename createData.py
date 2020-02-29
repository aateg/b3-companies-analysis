from crawlers.fundamentus import getFundamentus
from crawlers.info import getSetor
import pandas as pd

def createData():
    f = getFundamentus('balanco')

    s = getSetor()
