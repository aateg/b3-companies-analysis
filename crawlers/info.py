import requests, zipfile, io, xlrd
from bs4 import BeautifulSoup
from tickers import getTickers

def getInfo(ticker = None):
    """
    Retorna setor, subsetor, segmento e nome referente aos tickers indicados, 
    ou à todos os tickers se não houver parâmetro indicado
    Parâmetros
    ----------
    ticker: str, list ou None
        nome do ticker da empresa
    Saidas
    ------
    list ou dict
        lista com info das empresas parametrizadas,
        ou dict com todas as infos caso ticker=None
    Exemplos de uso:
    >>> get_info('WEGE3')
    ['Bens Industriais', 'Máquinas e Equipamentos', 'Motores, Compressores e Outros', 'WEG         ']
    >>> get_info(['WEGE3', 'ITSA4'])
    [['Bens Industriais', 'Máquinas e Equipamentos', 'Motores, Compressores e Outros', 'WEG         '],
    ['Financeiro', 'Intermediários Financeiros', 'Bancos', 'ITAUSA      ']]
    >>> get_info()
    retorna dict com info de todas as empresas listadas
    """
    
    url = "http://www.b3.com.br/lumis/portal/file/fileDownload.jsp?fileId=8AA8D0975A2D7918015A3C81693D4CA4"

    try:
        responseZip = requests.get(url)
    except:
        return None
        
    z = zipfile.ZipFile(io.BytesIO(responseZip.content))
    fileName = z.namelist()[0]
     
    file = z.read(fileName)
    workbook = xlrd.open_workbook(file_contents=file)
    worksheet = workbook.sheet_by_index(0)
    
    nlin = worksheet.nrows
    
    info = {}
    lin = 0
    while lin < nlin:
        currentRow = worksheet.row_values(lin)
        #nextRow = worksheet.row_values(lin + 1)
        if currentRow == ['SETOR ECONÔMICO', 'SUBSETOR', 'SEGMENTO', 'LISTAGEM', '']:
            #and nextRow == ['', '', '', 'CÓDIGO', 'SEGMENTO']): 
            setorEcon, subSetor, segmento, _, _ = worksheet.row_values(lin + 2)
            currentRow = worksheet.row_values(lin + 3)
            lin += 3
            while currentRow != ['', '', '', '', '']:
                if currentRow[3] == '':
                    if currentRow[1] != '':
                        subSetor = currentRow[1]
                        segmento = currentRow[2]
                    else:
                        segmento = currentRow[2]
                else:
                    nome = currentRow[2]
                    info[currentRow[3]] = [setorEcon, subSetor, segmento, nome]
                lin += 1
                currentRow = worksheet.row_values(lin)
        lin += 1
    if ticker:
        if isinstance(ticker, str):
            return info[ticker[:4]]
        if isinstance(ticker, list):
            return [info[t[:4]] for t in ticker]
    return info

def getSetor():
    tickers = list(getTickers())

    info = getInfo()
    aux_list = []
    for ticker in tickers:
        try:
            info_ticker = info[ticker[:4]]
        except:
            info_ticker = ['', '', '']
        aux_dict = {}
        aux_dict['ticker'] = ticker
        aux_dict['setor'] = info_ticker[0]
        aux_dict['subsetor'] = info_ticker[1]
        aux_dict['segmento'] = info_ticker[2]
        aux_list.append(aux_dict)

    return aux_list
