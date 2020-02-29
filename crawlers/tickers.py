import requests
from bs4 import BeautifulSoup

def getTickers():
    '''
    Essa função obtém os tickers listados no site fundamentus.com.br, seja um setor
    específico, uma lista de setores ou todos os tickers de todos os setores.
    '''
    
    setores = {"Agropecuária": "42", "Água e Saneamento": "33", "Alimentos": "15",
               "Bebidas": "16", "Comércio": "27", "Comércio2": "12",
               "Comércio e Distribuição": "20", "Computadores e Equipamentos": "28",
               "Construção e Engenharia": "13", "Diversos": "26",
               "Embalagens": "6", "Energia Elétrica": "32",
               "Equipamentos Elétricos": "9", "Exploração de Imóveis": "39",
               "Financeiros": "35", "Fumo": "17", "Gás": "34", 
               "Holdings Diversificadas": "40", "Hoteis e Restaurantes": "24",
               "Madeira e Papel": "5", "Máquinas e Equipamentos": "10", 
               "Materiais Diversos": "7", "Material de Transporte": "8",
               "Mídia": "23", "Mineração": "2", "Outros": "41",
               "Petróleo, Gás e Biocombustíveis": "1", "Previdência e Seguros": "38",
               "Prods. de Uso Pessoal e de Limpeza": "18", "Programas e Serviços": "29",
               "Químicos": "4", "Saúde": "19", "Securitizadoras de Recebíveis": "36",
               "Serviços": "11", "Serviços Financeiros Diversos": "37",
               "Siderurgia e Metalurgia": "3", "Tecidos, Vestuário e Calçados": "21",
               "Telefonia Fixa": "30", "Telefonia Móvel": "31", "Transporte": "14",
               "Utilidades Domésticas": "22", "Viagens e Lazer": "25"}

    lista_setores = list(setores.keys())
    
    tickers = []

    for item in lista_setores:
        try:
            url = "https://www.fundamentus.com.br/resultado.php?setor=" + setores[item]
            response = requests.get(url)
        except:
            print("Não foi possível coletar informações do setor: " + item)
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        tickers_bruto = soup.find('tbody').find_all("a")
        for ticker in tickers_bruto:
            tickers.append(ticker.string)
        
    tickers.sort()
    return tickers
