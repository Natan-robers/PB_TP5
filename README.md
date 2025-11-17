# Mercado TP4 - Estrutura Organizada

Estrutura modularizada em camadas (data, services, views, utils) pronta para rodar.
Para executar:
1. Criar e ativar um venv
2. `pip install -r requirements.txt`
3. `python app.py`

O app irá:
- Inicializar o banco SQLite (mercado.db)
- Garantir clientes iniciais (clientes.json)
- Fazer scraping robusto da página de produtos e gerar produtos.csv
- Importar produtos para o banco
- Abrir menu do caixa e permitir atendimento com agrupamento de itens e baixa de estoque ao finalizar.
