import json

# Definindo a classe Corretor


class Corretor:
    def __init__(self, nome, susep, apolices, contato):
        self.nome = nome
        self.susep = susep
        self.apolices = apolices
        self.contato = contato


# Lendo o arquivo JSON
with open('arquivo.json', 'r') as conteudo:
    dados_corretor = json.load(conteudo)

# Criando um objeto Corretor a partir dos dados do arquivo JSON
corretor = Corretor(
    nome=dados_corretor['nome'],
    susep=dados_corretor['susep'],
    apolices=dados_corretor['apolices'],
    contato=dados_corretor['contato']
)

# Exibindo as informações do objeto Corretor
print(f"Nome: {corretor.nome}")
print(f"SUSEP: {corretor.susep}")
print(f"Apolices: {corretor.apolices}")
print(f"Contato: {corretor.contato}")
