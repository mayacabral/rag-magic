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

from flask import Blueprint, jsonify
from dotenv import load_dotenv
import gzip, json
import requests


load_dotenv()

URL = 'https://api.scryfall.com'

HEADERS = {
    'User-Agent': 'agenteIa',
    'Accept': 'application/json;q=0.9,*/*;q=0.8'
}
