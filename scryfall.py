""" 
IDEIA DO PROJETO: CONSUMIR A API OFICIAL DO MAGIC, SUBIR EM ALGUM BANCO LOCAL (PROVAVELMENTE MONGO) 
FAZER RAG
DEVOLVER COM ALGUM MODELO DE IA
EXPOSTO NO STRIMILITE

ESTRUTURA: LÓGICA EM MÓDULOS COMUNS, FLASK COMO CAMADA FINA

agenteIA/
├── scryfall.py   # baixar_cartas, eh_carta_valida, normalizar   (sem Flask, sem Mongo)
├── banco.py      # conexão Mongo + importar_cartas
├── rag.py        # busca + chamada ao modelo de IA
├── api.py        # Flask: rotas que só chamam as funções acima
└── main.py       # Streamlit: importa e chama as funções direto
"""

from flask import Blueprint, Flask, jsonify
import gzip, json
import requests


app = Flask(__name__)

URL = 'https://api.scryfall.com'

HEADERS = {
    'User-Agent': 'agenteIa',
    'Accept': 'application/json;q=0.9,*/*;q=0.8'
}

scryfall_bp = Blueprint("scryfall", __name__)

@scryfall_bp.route("/catalogo/card-names", methods=["GET"])
def listar_nomes_cartas():
    endpoint = f"{URL}/catalog/card-names"

    try:
        response = requests.get(
            endpoint,
            headers=HEADERS,
            timeout=30
        )
        response.raise_for_status()

        dados = response.json()

        return jsonify(dados), 200

    except requests.exceptions.RequestException as erro:
        return jsonify({
            "erro": "Não foi possível consultar a Scryfall API.",
            "detalhes": str(erro)
        }), 502




app.register_blueprint(scryfall_bp)

if __name__ == "__main__":
    print("Rotas registradas:")
    print(app.url_map)

    app.run(debug=True)

