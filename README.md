
##  Dados de Teste

### Clientes de Teste


| ID | Nome | Descrição |
|----|------|-----------|
| Varia | `cliente_teste1` | Cliente que mais compra e mais gasta (3 compras) |
| Varia | `cliente_teste2` | Cliente que gastou menos (1 compra pequena) |
| Varia | `cliente_teste3` | Cliente com 1 compra |
| Varia | `cliente_teste4` | Cliente sem compras |
| Varia | `cliente_teste5` | Cliente sem compras |

Nota: Os IDs são gerados automaticamente. Use o SIG para consultar os IDs reais.

### Produtos


| ID | Nome | Quantidade | Preço |
|----|------|------------|-------|
| 1 | (Varia conforme scraping) | (Varia) | (Varia) |
| 2 | (Varia conforme scraping) | (Varia) | (Varia) |
| 3 | (Varia conforme scraping) | (Varia) | (Varia) |
| ... | ... | ... | ... |
| 10 | (Varia conforme scraping) | (Varia) | (Varia) |

Para ver os produtos disponíveis:
- No SIG: Menu "Produtos" → "Consultar produtos"
- No App: Durante o atendimento, digite o ID do produto

### Fornecedores de Teste

| ID | Nome | Produtos Associados |
|----|------|---------------------|
| Varia | `fornecedor_teste1` | Produtos ID: 1, 2, 3 |
| Varia | `fornecedor_teste2` | Produtos ID: 4, 5 |
| Varia | `fornecedor_teste3` | Produtos ID: 6, 7, 1 (produto 1 compartilhado) |
| Varia | `fornecedor_teste4` | SEM PRODUTOS |

### Compras de Teste

**Cliente `cliente_teste1` (3 compras):**
- **Compra 1:** 3 itens (Produtos 1, 2, 3)
- **Compra 2:** 2 itens (Produtos 4, 5)
- **Compra 3:** 3 itens (Produtos 6, 7, 1)

**Cliente `cliente_teste2` (1 compra):**
- **Compra 4:** 1 item (Produto 1) - **GASTOU MENOS**

**Cliente `cliente_teste3` (1 compra):**
- **Compra 5:** 1 item (Produto 2)

---

## 🎯 Demonstração do SIG

### Menu Principal

```
1. Clientes
2. Produtos
0. Sair
```

### 1. Menu Clientes

#### 1.1. Clientes com Compras

**Opção 1: Consultar compras de um cliente**
1. Escolha "Clientes" → "Clientes com compras" → "Consultar compras de um cliente"
2. Digite o ID do cliente (ex: ID de `cliente_teste1`)
3. Veja a lista de compras ordenadas por data/hora (mais recente primeiro)
4. Digite o ID de uma compra para ver a nota fiscal completa

**Opção 2: Clientes que mais compram**
1. Escolha "Clientes" → "Clientes com compras" → "Clientes que mais compram"
2. Veja o ranking de clientes por número de compras
3. **Resultado esperado:** `cliente_teste1` em primeiro lugar (3 compras)

**Opção 3: Clientes que mais gastam**
1. Escolha "Clientes" → "Clientes com compras" → "Clientes que mais gastam"
2. Veja o ranking de clientes por valor total gasto
3. **Resultado esperado:** `cliente_teste1` em primeiro lugar (maior valor)

#### 1.2. Clientes sem Compras

1. Escolha "Clientes" → "Clientes sem compras"
2. Veja a lista de clientes que nunca fizeram compras
3. **Resultado esperado:** `cliente_teste4` e `cliente_teste5`

### 2. Menu Produtos

#### 2.1. CRUD de Produtos

**Consultar produtos:**
- Veja todos os produtos cadastrados com ID, nome, quantidade e preço

**Cadastrar produto:**
- Crie um novo produto
- Associe fornecedores durante o cadastro

**Alterar produto:**
- Altere nome, quantidade ou preço
- Gerencie fornecedores (adicionar/remover)

**Excluir produto:**
- Remova um produto do sistema

#### 2.2. Consultas Especiais

**Opção 1: Produtos mais vendidos**
- Veja o Top 10 produtos por quantidade vendida
- **Resultado esperado:** Produtos mais comprados aparecem primeiro

**Opção 2: Produtos menos vendidos**
- Veja o Top 10 produtos menos vendidos
- Produtos nunca vendidos também são listados

**Opção 3: Produtos com estoque baixo**
- Digite um limite de estoque (ex: 10)
- Veja produtos com quantidade <= ao limite

**Opção 4: Fornecedores de um produto**
- Digite o ID de um produto (ex: 1)
- Veja todos os fornecedores associados
- **Resultado esperado:** Produto 1 tem 2 fornecedores (`fornecedor_teste1` e `fornecedor_teste3`)

---

## 🛒 Demonstração do App (Caixa)

### Fluxo de Atendimento

1. **Abrir Caixa:**
   ```
   Deseja abrir o caixa? [s/n]: s
   ```

2. **Iniciar Atendimento:**
   ```
   Deseja iniciar um atendimento? [s/n]: s
   ```

3. **Solicitar ID do Cliente:**
   ```
   Entre com o ID do cliente: [ID]
   ```
   - Se o cliente não existir, será cadastrado automaticamente como "Cliente {ID}"

4. **Adicionar Produtos:**
   ```
   Digite id do produto (ou 'fim' para encerrar): [ID]
   Quantidade para [Nome do Produto] (disponível [Qtd]): [Qtd]
   ```
   - Repita para adicionar mais produtos
   - Digite `fim` para finalizar

5. **Nota Fiscal:**
   - A nota fiscal é exibida automaticamente
   - Produtos iguais são agrupados
   - Mostra quantidade total e valor total por item
   - Mostra o total geral

6. **Finalizar:**
   - A compra é registrada no banco
   - O estoque é atualizado
   - Você pode iniciar outro atendimento ou encerrar

### Exemplo de Uso

```
Deseja abrir o caixa? [s/n]: s
Deseja iniciar um atendimento? [s/n]: s
Entre com o ID do cliente: 40
Compra 11 iniciada.
Digite id do produto (ou 'fim' para encerrar): 1
Quantidade para [Produto] (disponível 100): 5
Digite id do produto (ou 'fim' para encerrar): 1
Quantidade para [Produto] (disponível 95): 3
Digite id do produto (ou 'fim' para encerrar): 2
Quantidade para [Produto] (disponível 50): 2
Digite id do produto (ou 'fim' para encerrar): fim

--- NOTA FISCAL ---
Cliente: cliente_teste1 (ID: 40)

nome          quantidade  preco  total
[Produto 1]   8           10.00   80.00
[Produto 2]   2           15.00   30.00

Total: R$ 110.00

Compra 11 registrada. Estoque atualizado e atendimento finalizado.
```

**Observação:** Produtos iguais são agrupados automaticamente (ex: 2x Produto 1 = 8 unidades no total).

---

## 📁 Estrutura do Projeto

```
mercado_tp4/
├── app.py                          # Aplicação do Caixa
├── sig.py                          # Aplicação SIG
├── popular_banco_teste.py          # Script para popular dados de teste
├── criar_fornecedores_excel.py    # Script para criar fornecedores.xlsx
├── data/
│   ├── conexao.py                 # Gerenciamento de sessão única
│   ├── modelos.py                 # Modelos SQLAlchemy
│   └── repositorio_*.py           # Repositórios de dados
├── services/
│   ├── servico_cliente.py         # Serviços de cliente
│   ├── servico_produto.py         # Serviços de produto
│   ├── servico_scraping.py         # Web scraping
│   ├── servico_atendimento.py      # Lógica de atendimento
│   └── sig/
│       └── servico_excel.py        # Carregamento de Excel
├── views/
│   ├── menu_caixa.py               # Menu do caixa
│   ├── interface_console.py        # Interface console
│   └── sig/
│       ├── menu_principal.py       # Menu principal SIG
│       ├── menu_clientes.py        # Menu de clientes
│       └── menu_produtos.py         # Menu de produtos
├── utils/
│   └── arquivos.py                 # Utilitários de arquivos
├── clientes.json                   # Arquivo JSON com clientes iniciais
├── produtos.csv                    # Arquivo CSV gerado pelo scraping
├── fornecedores.xlsx               # Arquivo Excel com fornecedores
└── mercado.db                      # Banco de dados SQLite
```

---

## 🔍 Dicas para Demonstração

### Para Demonstrar o SIG:

1. **Clientes que mais compram:**
   - Use `cliente_teste1` (deve aparecer em primeiro)

2. **Clientes que mais gastam:**
   - Use `cliente_teste1` (deve ter o maior valor)

3. **Clientes sem compras:**
   - Mostre `cliente_teste4` e `cliente_teste5`

4. **Fornecedores de um produto:**
   - Use o Produto ID 1 (deve ter 2 fornecedores: `fornecedor_teste1` e `fornecedor_teste3`)

5. **Produtos mais vendidos:**
   - Mostre o ranking completo

### Para Demonstrar o App:

1. **Agrupamento de produtos:**
   - Adicione o mesmo produto várias vezes
   - Mostre que na nota fiscal aparece agrupado

2. **Cadastro automático de cliente:**
   - Use um ID que não existe
   - Mostre que o cliente é cadastrado automaticamente

3. **Atualização de estoque:**
   - Verifique o estoque antes e depois da compra

---

## ⚠️ Observações Importantes

1. **Ordem de Execução:**
   - Primeiro execute `app.py` para carregar produtos
   - Depois execute `popular_banco_teste.py` para criar dados de teste
   - Por fim, execute `sig.py` ou `app.py` conforme necessário

2. **IDs Dinâmicos:**
   - Os IDs de clientes e fornecedores são gerados automaticamente
   - Use o SIG para consultar os IDs reais antes de demonstrar

3. **Produtos:**
   - Os produtos são carregados via web scraping
   - Os nomes e preços variam conforme a página web
   - Use o SIG para ver os produtos disponíveis

4. **Fornecedores:**
   - O arquivo `fornecedores.xlsx` é carregado automaticamente pelo SIG
   - Se não existir, o sistema avisará mas continuará funcionando

---

## 📝 Notas Finais

- O sistema utiliza uma **sessão única** de banco de dados (conforme Rubric 0 do TP4)
- Todos os dados são persistidos no arquivo `mercado.db`
- O sistema suporta tratamento de erros e interrupções (Ctrl+C)
- Os nomes das funções estão em português (pt-BR)

---

**Desenvolvido para TP5 - Projeto de Bloco**
