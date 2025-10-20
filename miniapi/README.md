# Mini API em Flask

## 🚀 Como executar
```bash
# Crie o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
python src/app.py

#Post com novos usuários através do comando: curl -X POST http://127.0.0.1:5000/users -H "Content-Type: application/json" -d "{\"name\":\"julinhocarrara\", \"email\":\"JulinhoCarrara@example.com\"}" | python -m json.tool