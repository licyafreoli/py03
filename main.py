produtos = {}

def obter_preco():
    while True:
        try:
            preco = input("Digite o preço do produto (ex: 10.50 ou 10,50): ")
            preco = preco.replace(',', '.')
            preco_float = float(preco)
            return preco_float
        except ValueError:
            print("Valor inválido! Por favor, insira um preço válido.")

for i in range(5):
    nome_produto = input(f"Digite o nome do produto {i+1}: ")
    preco_produto = obter_preco()
    
    produtos[nome_produto] = preco_produto

valor_total = sum(produtos.values())

print(f"\nValor total da compra: R${valor_total:.2f}")
