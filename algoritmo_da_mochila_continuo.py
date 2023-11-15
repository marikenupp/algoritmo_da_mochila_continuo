import pandas as pd

itens = {
    'Tipo_Item': ['A', 'B', 'C', 'D'],
    'Quantidade_Item': [2, 3, 1, 4],
    'Valor_Item': [60, 30, 20, 20],
    'Peso_Item': [8, 4, 3, 2]
}

df_itens = pd.DataFrame(itens)
df_itens['Densidade_Valor_Item'] = df_itens['Valor_Item'] / df_itens['Peso_Item']
df_itens.sort_values(by='Densidade_Valor_Item', ascending=False, inplace=True)

capacidade_mochila = 30
carga_atual = 0
Valor_Item_total = 0
Quantidade_Item_itens = []

for _, item in df_itens.iterrows():
    if carga_atual < capacidade_mochila:
        if carga_atual + item['Peso_Item'] * item['Quantidade_Item'] <= capacidade_mochila:
            carga_atual += item['Peso_Item'] * item['Quantidade_Item']
            Valor_Item_total += item['Valor_Item'] * item['Quantidade_Item']
            Quantidade_Item_itens.append(item['Quantidade_Item'])
        else:
            espaco_restante = capacidade_mochila - carga_atual
            fraccao = espaco_restante / item['Peso_Item']
            carga_atual += fraccao * item['Peso_Item']
            Valor_Item_total += fraccao * item['Valor_Item']
            Quantidade_Item_itens.append(fraccao)
            break  
    else:
        Quantidade_Item_itens.append(0)


while len(Quantidade_Item_itens) < len(df_itens):
    Quantidade_Item_itens.append(0)

df_itens['Quantidade_Item na Mochila'] = Quantidade_Item_itens
df_itens['Fração na Mochila'] = df_itens['Quantidade_Item na Mochila'] / df_itens['Quantidade_Item']
df_itens.sort_values(by='Tipo_Item', inplace=True)

tabela_saida = df_itens[['Tipo_Item', 'Fração na Mochila']].reset_index(drop=True)
print(tabela_saida)