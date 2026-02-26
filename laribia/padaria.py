Nome_do_cliente=str(input("Digite seu nome completo:"))
Nome_do_produto=str(input("Digite o nome do produto que deseja comprar:"))
Quantidade=int(input("Digite a quantidade que deseja:"))
Preço_unitário=float(input("Digite o preço único do produto:"))
Valor_total=Quantidade*Preço_unitário

print("Seu nome é:",Nome_do_cliente)
print("O produto que você está comprando é:",Nome_do_produto)
print("O valor total foi de:",Valor_total)