import requests
from bs4 import BeautifulSoup


def get_exportacao(ano, tipo):
    mapa = {"vinhos": 1, "espumantes": 2, "uvas": 3, "suco": 4}
    if tipo in mapa:
        tipo = mapa[tipo]

    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_06&subopcao=subopt_0{tipo}"

    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
    else:
        return f"Erro ao acessar a página: {response.status_code}"

    soup = BeautifulSoup(html_content, "html.parser")

    tabela = soup.find("table", class_="tb_base tb_dados")

    tabela_header = [header.text.strip() for header in tabela.find_all("th")]

    linhas = tabela.find_all("tr")[1:]

    all_data = []

    for linha in linhas[:-1]:
        colunas = linha.find_all("td")
        dados_linha = {
            tabela_header[0]: colunas[0].text.strip(),
            tabela_header[1]: colunas[1]
            .text.strip()
            .replace(".", "")
            .replace("-", "0"),
            tabela_header[2]: colunas[2]
            .text.strip()
            .replace(".", "")
            .replace("-", "0"),
        }
        all_data.append(dados_linha)

    return all_data


def get_importacao(ano, tipo):
    mapa = {"vinhos": 1, "espumantes": 2, "frescas": 3, "passas": 4, "suco": 5}
    if tipo in mapa:
        tipo = mapa[tipo]

    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_05&subopcao=subopt_0{tipo}"

    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
    else:
        return f"Erro ao acessar a página: {response.status_code}"

    soup = BeautifulSoup(html_content, "html.parser")

    tabela = soup.find("table", class_="tb_base tb_dados")

    tabela_header = [header.text.strip() for header in tabela.find_all("th")]

    linhas = tabela.find_all("tr")[1:]

    all_data = []

    for linha in linhas[:-1]:
        colunas = linha.find_all("td")
        dados_linha = {
            tabela_header[0]: colunas[0].text.strip(),
            tabela_header[1]: colunas[1]
            .text.strip()
            .replace(".", "")
            .replace("-", "0"),
            tabela_header[2]: colunas[2]
            .text.strip()
            .replace(".", "")
            .replace("-", "0"),
        }
        all_data.append(dados_linha)

    return all_data


def get_comercializacao(ano):
    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_04"

    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
    else:
        return f"Erro ao acessar a página: {response.status_code}"

    soup = BeautifulSoup(response.text, "html.parser")

    tabela = soup.find("table", class_="tb_base tb_dados")

    tabela_header = [header.text.strip() for header in tabela.find_all("th")]

    linhas = tabela.find_all("tr")[1:]

    all_data = []
    item_atual = None

    for linha in linhas[:-1]:
        td = linha.find("td")
        if td is not None:
            if td.has_attr("class"):
                if "tb_item" in td["class"]:
                    item_atual = {
                        tabela_header[0]: td.text.strip(),
                        tabela_header[1]: linha.find_all("td")[1]
                        .text.strip()
                        .replace(".", "")
                        .replace("-", "0"),
                        "subitens": [],
                    }
                    all_data.append(item_atual)
                elif "tb_subitem" in td["class"]:
                    subitem = {
                        tabela_header[0]: td.text.strip(),
                        tabela_header[1]: linha.find_all("td")[1]
                        .text.strip()
                        .replace(".", "")
                        .replace("-", "0"),
                    }
                    if item_atual:
                        item_atual["subitens"].append(subitem)

    return all_data


def get_processamento(ano, tipo):
    mapa = {"viniferas": 1, "americanas": 2, "uvas": 3, "sem_class": 4}
    if tipo in mapa:
        tipo = mapa[tipo]

    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_03&subopcao=subopt_0{tipo}"

    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
    else:
        return f"Erro ao acessar a página: {response.status_code}"

    soup = BeautifulSoup(response.text, "html.parser")

    tabela = soup.find("table", class_="tb_base tb_dados")

    tabela_header = [header.text.strip() for header in tabela.find_all("th")]

    linhas = tabela.find_all("tr")[1:]

    all_data = []
    item_atual = None

    for linha in linhas[:-1]:
        td = linha.find("td")
        if td is not None:
            if td.has_attr("class"):
                if "tb_item" in td["class"]:
                    item_atual = {
                        tabela_header[0]: td.text.strip(),
                        tabela_header[1]: linha.find_all("td")[1]
                        .text.strip()
                        .replace(".", "")
                        .replace("-", "0"),
                        "subitens": [],
                    }
                    all_data.append(item_atual)
                elif "tb_subitem" in td["class"]:
                    subitem = {
                        tabela_header[0]: td.text.strip(),
                        tabela_header[1]: linha.find_all("td")[1]
                        .text.strip()
                        .replace(".", "")
                        .replace("-", "0"),
                    }
                    if item_atual:
                        item_atual["subitens"].append(subitem)

    return all_data


def get_producao(ano):
    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_02"

    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
    else:
        return f"Erro ao acessar a página: {response.status_code}"

    soup = BeautifulSoup(response.text, "html.parser")

    tabela = soup.find("table", class_="tb_base tb_dados")

    tabela_header = [header.text.strip() for header in tabela.find_all("th")]

    linhas = tabela.find_all("tr")[1:]

    all_data = []
    item_atual = None

    for linha in linhas[:-1]:
        td = linha.find("td")
        if td is not None:
            if td.has_attr("class"):
                if "tb_item" in td["class"]:
                    item_atual = {
                        tabela_header[0]: td.text.strip(),
                        tabela_header[1]: linha.find_all("td")[1]
                        .text.strip()
                        .replace(".", "")
                        .replace("-", "0"),
                        "subitens": [],
                    }
                    all_data.append(item_atual)
                elif "tb_subitem" in td["class"]:
                    subitem = {
                        tabela_header[0]: td.text.strip(),
                        tabela_header[1]: linha.find_all("td")[1]
                        .text.strip()
                        .replace(".", "")
                        .replace("-", "0"),
                    }
                    if item_atual:
                        item_atual["subitens"].append(subitem)

    return all_data
