import time
# Importa do arquivo banco de dados
from dados_sistema import (
    cardapio, estoque, dados_todas_lojas, 
    formas_pagamento, dados_matriz, materiais_sistema
)

def tela_cliente():
    """Área do Cliente"""
    print("\n [ÁREA DO CLIENTE]")
    print("Como deseja comprar?\n[1] App\n[2] Totem\n[3] Balcão\n[4] Pick-up\n[0] Voltar para Tela de Login")
    try:
        opcao_meio = int(input("Opção: "))
    except ValueError:
        print(" Digite um número válido.")
        return

    if opcao_meio == 0:
        print("Voltando...")
        return

    carrinho = []
    total_pedido = 0.0

    while True:
        print("\nCARDÁPIO UNIDADE")
        for codigo, info in cardapio.items():
            print(f"[{codigo}] {info['item']} - R$ {info['preco']:.2f} (Disponível: {estoque[info['item']]})")
        print("[0] Cancelar Compra e Sair do Menu")

        try:
            opcao_produto = int(input("\nDigite o número do item ou 0 para cancelar e voltar: "))
        except ValueError:
            print(" Opção inválida.")
            continue

        if opcao_produto == 0:
            for produto in carrinho:
                estoque[produto['item']] += 1
            print("Compra cancelada pelo cliente.")
            return

        if opcao_produto in cardapio:
            item = cardapio[opcao_produto]["item"]
            preco = cardapio[opcao_produto]["preco"]

            if estoque[item] > 0:
                if opcao_meio == 1:
                    preco *= 0.90

                carrinho.append({"item": item, "preco": preco})
                estoque[item] -= 1
                total_pedido += preco
                print(f" {item} adicionado ao carrinho!")
            else:
                print(f" Desculpe, o item '{item}' está esgotado!")
        else:
            print(" Opção de produto inválida.")

        print("\n" + "-" * 30)
        proximo_passo = input("Deseja [A] adicionar mais um produto ou [F] finalizar e pagar? (A/F): ").upper()
        if proximo_passo == "F":
            break

    if len(carrinho) > 0:
        print("\n" + "=" * 45)
        print("           CARRINHO         ")
        print("=" * 45)
        for produto in carrinho:
            print(f"• {produto['item']}: R$ {produto['preco']:.2f}")
        print("-" * 45)
        print(f"TOTAL DO PEDIDO: R$ {total_pedido:.2f}")
        print("=" * 45)

        confirmar = input("\nConfirmar e ir para o pagamento? (S/N): ").upper()

        if confirmar == "S":
            print("\n--- OPÇÕES DE PAGAMENTO ---")
            for cod_pag, nome_pag in formas_pagamento.items():
                print(f"[{cod_pag}] - {nome_pag}")

            try:
                opcao_pag = int(input("Escolha a forma de pagamento: "))
                print("\n[Dados protegido conforme Lei Geral da Proteção de Dados (LGPD)]")
            except ValueError:
                opcao_pag = 0
                
            pag_escolhido = formas_pagamento.get(opcao_pag, "Não informado")

            print(f"\nProcessando pagamento via {pag_escolhido}...")
            time.sleep(1)
            print(" Pagamento aprovado com sucesso!")

            dados_matriz["vendas_totais_reais"] += total_pedido
            dados_todas_lojas["Unidade Centro Matriz (Loja 01)"]["venda_atual"] += total_pedido

            for produto in carrinho:
                nome_item = produto['item']
                dados_matriz["produtos_vendidos"][nome_item] = dados_matriz["produtos_vendidos"].get(nome_item, 0) + 1

            tipo_envio = "Retirada"
            if opcao_meio == 1:
                print("\n COMO DESEJA RECEBER SEU PEDIDO?")
                print("[1] Retirada na Loja")
                print("[2] Entrega Delivery")
                try:
                    opcao_envio = int(input("Escolha uma opção: "))
                except ValueError:
                    opcao_envio = 1

                if opcao_envio == 2:
                    tipo_envio = "Entrega"
                    endereco = input("Digite seu endereço completo para entrega: ")
                    print("\n[Dados protegido conforme Lei Geral da Proteção de Dados (LGPD)]")
                    print(f" Endereço registrado: {endereco}")
                else:
                    tipo_envio = "Retirada"

            print("\n[STATUS]:  Pedido enviado para a Cozinha...")
            time.sleep(1)
            print("[STATUS]:  Refeição pronta!")

            if tipo_envio == "Entrega":
                print("\n [STATUS DO PEDIDO]: Seu pedido chegou por Delivery!")
            else:
                print("\n [STATUS DO PEDIDO]: Seu pedido está pronto no balcão!")
        else:
            for produto in carrinho:
                estoque[produto['item']] += 1
            print("\nPedido cancelado.")

def tela_funcionario(nome_usuario, loja_vinculada):
    """Área do Funcionário"""
    while True:
        print(f"\n [PAINEL DO FUNCIONÁRIO - OPERAÇÃO LOCAL]")
        print(f"Funcionário: {nome_usuario} |  Loja: {loja_vinculada}")
        print("1. Ver Estoque desta Unidade")
        print("2. Ver Metas e Indicadores desta Unidade")
        print("3. Registrar Cancelamento ou Ajuste")
        print("0. Desconectar e Voltar para Tela de Login")
        opcao = input("Escolha uma opção: ")

        dados_loja_atual = dados_todas_lojas[loja_vinculada]

        if opcao == "0":
            print(f"Saindo do painel da {loja_vinculada}...")
            break
        elif opcao == "1":
            print(f"\n ESTOQUE ATUAL  {loja_vinculada.upper()} ")
            for produto, qtd in dados_loja_atual["estoque"].items():
                print(f"• {produto}: {qtd} unidades restantes")
        elif opcao == "2":
            print(f"\n DESEMPENHO DA LOJA  {loja_vinculada.upper()} ")
            print(f"Meta Diária da Unidade: R$ {dados_loja_atual['meta_diaria']:.2f}")
            print(f"Vendas Hoje nesta Unidade: R$ {dados_loja_atual['venda_atual']:.2f}")
            progresso = (dados_loja_atual['venda_atual'] / dados_loja_atual['meta_diaria']) * 100
            print(f"Progresso da Meta Local: {progresso:.1f}%")
        elif opcao == "3":
            item_cancelar = input("Digite o nome do produto para cancelar: ")
            justificativa = input("Motivo do cancelamento: ")
            log = f"ALERTA AUDITORIA: Ajuste de '{item_cancelar}' na {loja_vinculada} feito por {nome_usuario}. Motivo: {justificativa}"
            dados_matriz["auditoria_alertas"].append(log)
            print("Operação de ajuste registrada na matriz.")

def tela_chefe():
    """Área do Chefe"""
    while True:
        print("\n [PAINEL DA MATRIZ - LOGIN ADMINISTRADOR]")
        print("1. Relatório Financeiro de Vendas")
        print("2. Produtos Mais Consumidos (Ranking)")
        print("3. Auditoria de Operações")
        print("4. Acessar Materiais da Matriz e das Franquias")
        print("5. Ver Estoques de Todas as Lojas")
        print("6. Ver Funcionários de Todas as Lojas")
        print("0. Desconectar e Voltar para Tela de Login")
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Saindo do painel da matriz...")
            break
        elif opcao == "1":
            print(f"\nFaturamento Total da Rede: R$ {dados_matriz['vendas_totais_reais']:.2f}")
        elif opcao == "2":
            print("\n PRODUTOS MAIS CONSUMIDOS")
            for prod, qtd in dados_matriz["produtos_vendidos"].items():
                print(f"• {prod}: {qtd} saídas")
        elif opcao == "3":
            print("\n AUDITORIA E RASTREABILIDADE")
            for alerta in dados_matriz["auditoria_alertas"]:
                print(alerta)
        elif opcao == "4":
            print("\n REPOSITÓRIO CENTRAL DE MATERIAIS")
            print("\n[MATERIAIS DA MATRIZ]")
            for doc in materiais_sistema["Matriz"]: print(f"  {doc}")
            print("\n[MATERIAIS DAS FRANQUIAS / OPERAÇÃO]")
            for doc in materiais_sistema["Franquias (Operação Local)"]: print(f"  {doc}")
        elif opcao == "5":
            print("\n RELATÓRIO DE ESTOQUES DA REDE")
            for nome_loja, dados in dados_todas_lojas.items():
                print(f"\n {nome_loja}:")
                for prod, qtd in dados["estoque"].items(): print(f"  • {prod}: {qtd} unidades")
        elif opcao == "6":
            print("\nQUADRO DE FUNCIONÁRIOS")
            for nome_loja, dados in dados_todas_lojas.items():
                print(f"\n Equipe própria da {nome_loja}:")
                for func in dados["funcionarios"]: print(f"   {func}")