from flask import jsonify
from app import app, auth
from app.services.scraping_service import (
    get_exportacao,
    get_importacao,
    get_comercializacao,
    get_processamento,
    get_producao,
)


@app.route("/exportacao/<int:ano>/<tipo>", methods=["GET"])
@auth.login_required
def scrape_exportacao(ano, tipo):
    """
    Endpoint para obter dados de exportação
    ---
    parameters:
      - name: ano
        in: path
        type: integer
        required: true
        description: O ano para o qual obter os dados de exportação
      - name: tipo
        in: path
        type: string
        required: true
        description: O tipo de produto (vinhos, espumantes, uvas, suco)
    responses:
      200:
        description: Dados de exportação
        schema:
          type: object
          properties:
            data:
              type: array
              items:
                type: string
      400:
        description: Erro de validação
        schema:
          type: object
          properties:
            error:
              type: string
    """
    if not (1973 <= ano <= 2023):
        return jsonify({"error": "Ano deve estar entre 1973 e 2023"}), 400
    if tipo not in ["vinhos", "espumantes", "uvas", "suco"]:
        return (
            jsonify(
                {
                    "error": "Tipo deve ser um dos seguintes: vinhos, espumantes, uvas, suco"
                }
            ),
            400,
        )
    return jsonify(get_exportacao(ano, tipo))


@app.route("/importacao/<int:ano>/<tipo>", methods=["GET"])
@auth.login_required
def scrape_importacao(ano, tipo):
    """
    Endpoint para obter dados de importação
    ---
    parameters:
      - name: ano
        in: path
        type: integer
        required: true
        description: O ano para o qual obter os dados de importação
      - name: tipo
        in: path
        type: string
        required: true
        description: O tipo de produto (vinhos, espumantes, frescas, passas, suco)
    responses:
      200:
        description: Dados de importação
        schema:
          type: object
          properties:
            data:
              type: array
              items:
                type: string
      400:
        description: Erro de validação
        schema:
          type: object
          properties:
            error:
              type: string
    """
    if not (1973 <= ano <= 2023):
        return jsonify({"error": "Ano deve estar entre 1973 e 2023"}), 400
    if tipo not in ["vinhos", "espumantes", "frescas", "passas", "suco"]:
        return (
            jsonify(
                {
                    "error": "Tipo deve ser um dos seguintes: vinhos, espumantes, uvas frescas, uvas passas ou suco"
                }
            ),
            400,
        )
    return jsonify(get_importacao(ano, tipo))


@app.route("/comercializacao/<int:ano>", methods=["GET"])
@auth.login_required
def scrape_comercializacao(ano):
    """
    Endpoint para obter dados de comercialização
    ---
    parameters:
      - name: ano
        in: path
        type: integer
        required: true
        description: O ano para o qual obter os dados de comercialização
    responses:
      200:
        description: Dados de comercialização
        schema:
          type: object
          properties:
            data:
              type: array
              items:
                type: string
      400:
        description: Erro de validação
        schema:
          type: object
          properties:
            error:
              type: string
    """
    if not (1973 <= ano <= 2023):
        return jsonify({"error": "Ano deve estar entre 1973 e 2023"}), 400
    return jsonify(get_comercializacao(ano))


@app.route("/processamento/<int:ano>/<tipo>", methods=["GET"])
@auth.login_required
def scrape_processamento(ano, tipo):
    """
    Endpoint para obter dados de processamento
    ---
    parameters:
      - name: ano
        in: path
        type: integer
        required: true
        description: O ano para o qual obter os dados de processamento
      - name: tipo
        in: path
        type: string
        required: true
        description: O tipo de produto (viniferas, americanas, uvas, sem_class)
    responses:
      200:
        description: Dados de processamento
        schema:
          type: object
          properties:
            data:
              type: array
              items:
                type: string
      400:
        description: Erro de validação
        schema:
          type: object
          properties:
            error:
              type: string
    """
    if not (1973 <= ano <= 2023):
        return jsonify({"error": "Ano deve estar entre 1973 e 2023"}), 400
    if tipo not in ["viniferas", "americanas", "uvas", "sem_class"]:
        return (
            jsonify(
                {
                    "error": "Tipo deve ser um dos seguintes: viníferas, americanas, uvas, sem classificação"
                }
            ),
            400,
        )
    return jsonify(get_processamento(ano, tipo))


@app.route("/producao/<int:ano>", methods=["GET"])
@auth.login_required
def scrape_producao(ano):
    """
    Endpoint para obter dados de produção
    ---
    parameters:
      - name: ano
        in: path
        type: integer
        required: true
        description: O ano para o qual obter os dados de produção
    responses:
      200:
        description: Dados de produção
        schema:
          type: object
          properties:
            data:
              type: array
              items:
                type: string
      400:
        description: Erro de validação
        schema:
          type: object
          properties:
            error:
              type: string
    """
    if not (1973 <= ano <= 2023):
        return jsonify({"error": "Ano deve estar entre 1973 e 2023"}), 400
    return jsonify(get_producao(ano))
