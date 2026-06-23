from flask import Flask, jsonify, request
import random
# Importando variáveis do banco de dados
from dados_sistema import cardapio, estoque, dados_matriz, dados_todas_lojas

app = Flask(__name__)

@app.route("/simular_compra", methods=["POST"])
def simular_compra():
    # Simula o cliente escolhendo a forma de compra App, Totem, etc
    opcao_meio = random.choice([1, 2, 3, 4])
    
    # Escolhe um produto aleatório do cardápio
    produto_id = random.choice(list(cardapio.keys()))
    item = cardapio[produto_id]["item"]
    preco = cardapio[produto_id]["preco"]

    # Verifica se tem estoque
    if estoque[item] > 0:
        # Desconto de 10% se for pelo App
        if opcao_meio == 1:
            preco *= 0.90
        
        # estoque e atualiza
        estoque[item] -= 1
        dados_matriz["vendas_totais_reais"] += preco
        dados_todas_lojas["Unidade Centro Matriz (Loja 01)"]["venda_atual"] += preco
        dados_matriz["produtos_vendidos"][item] = dados_matriz["produtos_vendidos"].get(item, 0) + 1

        return jsonify({
            "status": "sucesso",
            "mensagem": f"Comprou {item} por R${preco:.2f} via meio [{opcao_meio}]",
            "estoque_restante": estoque[item]
        }), 200
    else:
        return jsonify({
            "status": "erro",
            "mensagem": f"Item {item} esgotado no estoque!"
        }), 400

if __name__ == "__main__":
    # Roda o servidor flask na porta 5000
    app.run(debug=True, port=5000)