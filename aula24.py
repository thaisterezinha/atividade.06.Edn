import requests

# Solicita o código da moeda (ex: USD, EUR, GBP)
moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()

# Monta a URL da API
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

# Faz a requisição
resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()

    # A chave do dicionário é algo como "USDBRL", "EURBRL" etc.
    chave = moeda + "BRL"
    if chave in dados:
        info = dados[chave]
        print("\n=== Cotação Atual ===")
        print(f"Moeda: {info['name']}")
        print(f"Valor Atual: R$ {float(info['bid']):.2f}")
        print(f"Valor Máximo: R$ {float(info['high']):.2f}")
        print(f"Valor Mínimo: R$ {float(info['low']):.2f}")
        print(f"Data e Hora da Atualização: {info['create_date']}")
    else:
        print("Moeda não encontrada na API.")
else:
    print("Erro ao acessar a API. Código:", resposta.status_code)
