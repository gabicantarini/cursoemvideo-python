import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC9a17185193f153d266f4d251b13d55aa"
# Your Auth Token from twilio.com/console
auth_token  = "29ae88af5a893988a1f16e55f4d3c02c"
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em Excel para busca d info.
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']


for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+351969179784",
            from_="+18124146504",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)




# Lógica - Para cada arquivo:
# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000 - OK
# Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor - OK
# Caso não seja maior do que 55.000 não quero fazer nada - OK

# Notes
# Instalar no terminal
# pip install pandas
# pip install openpyxl
# pip install twilio
# pd é abreviação de pandas
# .loc localiza a linha e a coluna dentro do excel (tabela)
# usar .loc com .values para indicar somente o valor



