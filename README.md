# Dash Entrevista — Análise Olist Brazilian E-commerce

Projeto de análise exploratória e tratamento do dataset [Olist Brazilian E-commerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) (Kaggle), com saída para um dashboard em Power BI (`dash.pbix`).

## Estrutura

- `import_data.py` — baixa o dataset via `kagglehub` e salva os CSVs brutos em `dados/`.
- `analises.ipynb` — carrega os CSVs de `dados/`, faz a análise exploratória e o tratamento, e exporta os dados tratados para `dados_tratados/`.
- `dados/` — CSVs originais (9 tabelas: clientes, geolocalização, pedidos, itens de pedido, pagamentos, avaliações, produtos, vendedores, tradução de categorias).
- `dados_tratados/` — CSVs tratados, prontos para consumo no Power BI.
- `dash.pbix` — dashboard construído em cima dos dados tratados.

## Resumo da análise (`analises.ipynb`)

**Carregamento:** os 9 CSVs de `dados/` são lidos e organizados num dicionário `dfs`, mapeando nomes amigáveis (`dados_clientes`, `dados_pedidos`, etc.) aos respectivos DataFrames.

**Exploração inicial:**
- Verificação de volume: de ~3 mil linhas (`dados_vendedores`) a ~1 milhão de linhas (`dados_geograficos`).
- Verificação de valores nulos em todas as tabelas.

**Principais achados e tratamentos:**
- `dados_produtos`: 610 produtos sem `product_category_name`. Os nulos foram preenchidos com `"Sem Informação"`.
- `dados_pedidos`: 160 pedidos sem `order_approved_at` (~0,2% do total) — datas de aprovação de pagamento ausentes, mapeadas mas não preenchidas.
- `dados_pedidos`: também há nulos em `order_delivered_carrier_date` (1.783) e `order_delivered_customer_date` (2.965), referentes a pedidos ainda não entregues/despachados.
- `dados_avaliacoes`: grande parte das avaliações não tem título (87.656 nulos) nem comentário (58.247 nulos) — comportamento esperado, já que esses campos são opcionais para o cliente.

**Saída:** os DataFrames tratados (dicionário `dfs`) são exportados para `dados_tratados/`, um CSV por tabela, servindo de fonte para o dashboard Power BI.

## Como rodar

### 1. Criar e ativar o ambiente virtual

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Se o PowerShell bloquear a ativação com o erro *"a execução de scripts foi desabilitada neste sistema"*, libere scripts locais para o seu usuário (uma vez só) e tente ativar de novo:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Com o venv ativo, o prompt passa a mostrar `(.venv)` no início da linha.

### 2. Instalar as dependências

```powershell
pip install -r requirements.txt
```

### 3. Rodar o projeto

```powershell
python import_data.py             # baixa os dados brutos para dados/
jupyter notebook analises.ipynb   # roda a análise e gera dados_tratados/
```

Para desativar o ambiente virtual quando terminar:

```powershell
deactivate
```
