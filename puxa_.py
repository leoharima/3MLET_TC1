import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06"

pagina = requests.get(url)

soup = BeautifulSoup(pagina, "html_parser")

tabela = soup.find("table", class_="tb_base tb_dados")

tabela_header = [header.text.strip() for header in tabela.find_all("th")]

linhas = tabela.find_all("tr")[1:]

for linha in linhas:
    td = linha.find_all("td")

all_data = []

for linha in linhas[:-1]:
    colunas = linha.find_all("td")
    dados_linha = {
        tabela_header[0]: colunas[0].text.strip,
        tabela_header[1]: colunas[1].text.strip.replace("-", "0"),
        tabela_header[2]: colunas[2].text.strip.replace("-", "0"),
    }
    all_data.append(dados_linha)

print(jsonify(all_data))
