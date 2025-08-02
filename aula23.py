import requests

# Solicita o CEP ao usuário
cep = input("Digite o CEP (somente números): ")

# Remove espaços e confere se o CEP tem 8 dígitos
cep = cep.strip()
if len(cep) != 8 or not cep.isdigit():
    print("CEP inválido! Digite exatamente 8 números.")
else:
    # URL da API ViaCEP
    url = f"https://viacep.com.br/ws/{cep}/json/"

    # Requisição à API
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()

        # Verifica se o CEP foi encontrado
        if "erro" in dados:
            print("CEP não encontrado.")
        else:
            print("\n=== Endereço encontrado ===")
            print(f"Logradouro: {dados['logradouro']}")
            print(f"Bairro: {dados['bairro']}")
            print(f"Cidade: {dados['localidade']}")
            print(f"Estado: {dados['uf']}")
    else:
        print("Erro ao acessar a API. Código:", resposta.status_code)
