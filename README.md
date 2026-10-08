# RAG Magic

Assistente de IA para **Magic: The Gathering** que responde perguntas usando RAG (*Retrieval-Augmented Generation*) sobre dados da API oficial do Magic, com interface em Streamlit.

> 🚧 Projeto em desenvolvimento.

## Ideia do projeto

1. **Coletar** os dados das cartas pela API oficial do Magic
2. **Armazenar** os dados em um banco local (provavelmente MongoDB)
3. **Buscar** as informações relevantes para cada pergunta (RAG)
4. **Responder** com um modelo de IA usando o contexto encontrado
5. **Exibir** tudo em uma interface web com Streamlit

## Estrutura

```
agenteIA/
├── main.py       # Interface Streamlit (por enquanto, uma demo)
├── rag.py        # Lógica de RAG (em construção)
├── .env          # Chave de API (não vai para o GitHub)
└── .gitignore
```

## Como rodar

### 1. Clonar o repositório

```bash
git clone https://github.com/mayacabral/rag-magic.git
cd rag-magic
```

### 2. Criar e ativar o ambiente virtual

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

No Linux/macOS, use `source venv/bin/activate`.

### 3. Instalar as dependências

```bash
pip install streamlit pandas numpy python-dotenv
```

### 4. Configurar a chave de API

Crie um arquivo `.env` na raiz do projeto:

```
CHAVE_API=sua_chave_aqui
```

O `.env` está no `.gitignore` e **nunca** deve ser enviado para o GitHub.

### 5. Iniciar a aplicação

```bash
streamlit run main.py
```

O navegador abre em `http://localhost:8501`.

## Próximos passos

- [ ] Consumir a API oficial do Magic
- [ ] Salvar os dados no MongoDB
- [ ] Implementar a busca (RAG)
- [ ] Integrar um modelo de IA para gerar as respostas
- [ ] Montar a interface de perguntas no Streamlit
