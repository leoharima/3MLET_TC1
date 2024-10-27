from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route("/consulta", methods=["GET"])
def consulta():
    """
    Consulta informações sobre variedades de uva no site da Embrapa.

    Parâmetros:
        - nome (str): O nome da variedade de uva a ser pesquisada.

    Resposta:
        - Retorna um JSON com os detalhes da variedade de uva se encontrada,
          ou uma mensagem de erro se não encontrada.
    """
    nome = request.args.get("nome")
    if not nome:
        return jsonify({"error": "Parâmetro 'nome' é obrigatório"}), 400

    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01"

    try:
        # Simula o envio de uma requisição POST com o nome da variedade
        response = requests.post(url, data={"variedade": nome})
        response.raise_for_status()

        # Processa a resposta usando BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Extrai as informações relevantes
        resultados = []
        for item in soup.select(".result-item"):
            info = {
                "nome": item.select_one(".nome-variedade").get_text(strip=True),
                "detalhes": item.select_one(".detalhes").get_text(strip=True),
            }
            resultados.append(info)

        if not resultados:
            return jsonify({"message": "Variedade não encontrada"}), 404

        return jsonify(resultados), 200

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


# if __name__ == "__main__":
#     app.run(debug=True)
