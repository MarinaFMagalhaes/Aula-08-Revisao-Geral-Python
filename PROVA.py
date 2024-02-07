def adicionar_produto(lista_produtos):
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    valor_unitario = float(input("Digite o valor unitário do produto: "))

    total_produto = quantidade * valor_unitario
    produto = {"nome": nome, "quantidade": quantidade, "valor": valor_unitario, "total": total_produto}
    lista_produtos.append(produto)

    atualizar_valor_total(lista_produtos)
    print("Produto adicionado com sucesso!\n")


def ver_lista_produtos(lista_produtos):
    print("\nLista de Produtos:")
    for produto in lista_produtos:
        print(f"Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Valor Unitário: {produto['valor']}, Total: {produto['total']}")

    print(f"\nValor total de todos os produtos: {total_produtos}\n")


def atualizar_produto(lista_produtos):
    nome_produto = input("Digite o nome do produto que deseja atualizar: ")
    
    for produto in lista_produtos:
        if produto['nome'] == nome_produto:
            produto['nome'] = input("Digite o novo nome do produto: ")
            produto['quantidade'] = int(input("Digite a nova quantidade do produto: "))
            produto['valor'] = float(input("Digite o novo valor unitário do produto: "))
            
            produto['total'] = produto['quantidade'] * produto['valor']
            atualizar_valor_total(lista_produtos)
            
            print("Produto atualizado com sucesso!\n")
            return
    
    print("Produto não encontrado.\n")


def remover_produto(lista_produtos):
    nome_produto = input("Digite o nome do produto que deseja remover: ")
    
    for produto in lista_produtos:
        if produto['nome'] == nome_produto:
            lista_produtos.remove(produto)
            atualizar_valor_total(lista_produtos)
            print("Produto removido com sucesso!\n")
            return
    
    print("Produto não encontrado.\n")


def atualizar_valor_total(lista_produtos):
    global total_produtos
    total_produtos = sum(produto['total'] for produto in lista_produtos)


def menu():
    lista_produtos = []
    global total_produtos
    total_produtos = 0

    while True:
        print("Opções:")
        print("1. Adicionar produto")
        print("2. Ver lista de produtos")
        print("3. Atualizar produto")
        print("4. Remover produto")
        print("5. Encerrar programa")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            adicionar_produto(lista_produtos)
        elif opcao == '2':
            ver_lista_produtos(lista_produtos)
        elif opcao == '3':
            atualizar_produto(lista_produtos)
        elif opcao == '4':
            remover_produto(lista_produtos)
        elif opcao == '5':
            print("Programa encerrado.")
            return
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu()