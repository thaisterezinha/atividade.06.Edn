import requests

# URL da API
url = "https://randomuser.me/api/"

# Faz a requisição GET
resposta = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if resposta.status_code == 200:
    dados = resposta.json()
    usuario = dados['results'][0]

    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario['email']
    pais = usuario['location']['country']

    print("=== Perfil de Usuário Aleatório ===")
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"País: {pais}")
else:
    print("Erro ao acessar a API. Código:", resposta.status_code)
