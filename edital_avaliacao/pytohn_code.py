import pandas as pd
order = "https://raw.githubusercontent.com/Data-Science-Research/edital_avaliacao/main/order.csv"
country = "https://raw.githubusercontent.com/Data-Science-Research/edital_avaliacao/main/country.csv"
mainCategory = "https://raw.githubusercontent.com/Data-Science-Research/edital_avaliacao/main/mainCategory.csv"
order = pd.read_csv(order, sep=";", header=0)
country = pd.read_csv(country, sep=";", header=0)
mainCategory = pd.read_csv(mainCategory, sep=";", header=0)


mapeamento_roupas = mainCategory.set_index('id')['mainCategory'].to_dict()
order['page 1 (main category)'] = order['page 1 (main category)'].map(mapeamento_roupas)

quantModelosPorTipoRoupa = order.groupby('page 1 (main category)')['page 2 (clothing model)'].nunique()

df_quantModelosPorTipoRoupa = quantModelosPorTipoRoupa.reset_index()

# Definir os nomes das colunas do DataFrame
df_quantModelosPorTipoRoupa.columns = ['Tipo de Roupa', 'Quantidade de Modelos']

# Escrever o DataFrame em um arquivo JSON
print(df_quantModelosPorTipoRoupa)

caminho_arquivo_json = 'dados_questao_6.json'
df_quantModelosPorTipoRoupa.to_json(caminho_arquivo_json, orient='records')