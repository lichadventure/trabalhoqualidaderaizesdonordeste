# BANCO DE DADOS
usuarios = {
    "cliente": {"senha": "123", "perfil": "CLIENTE", "loja": None},
    "funcionario1": {"senha": "AAA", "perfil": "FUNCIONARIO", "loja": "Unidade Centro Matriz (Loja 01)"},
    "funcionario2": {"senha": "BBB", "perfil": "FUNCIONARIO", "loja": "Unidade Shopping (Loja 02)"},
    "funcionario3": {"senha": "CCC", "perfil": "FUNCIONARIO", "loja": "Unidade Sul (Loja 03)"},
    "chefe": {"senha": "ADMIN", "perfil": "ADM", "loja": None}
}

cardapio = {
    1: {"item": "Tapioca Recheada", "preco": 8.00},
    2: {"item": "Cuscuz Recheado", "preco": 10.00},
    3: {"item": "Bolo de Macaxeira", "preco": 5.00},
    4: {"item": "Suco Regional", "preco": 6.00},
    5: {"item": "Café da Manhã Completo", "preco": 22.00}
}

estoque = {
    "Tapioca Recheada": 150,
    "Cuscuz Recheado": 102,
    "Bolo de Macaxeira": 81,
    "Suco Regional": 201,
    "Café da Manhã Completo": 51
}

dados_todas_lojas = {
    "Unidade Centro Matriz (Loja 01)": {
        "funcionarios": ["Carlos (Gerente)", "Ana (Atendente)", "Seu Jose (Cozinheiro)"],
        "estoque": {"Tapioca Recheada": 50, "Cuscuz Recheado": 34, "Bolo de Macaxeira": 27, "Suco Regional": 67, "Café da Manhã Completo": 17},
        "meta_diaria": 1000.00,
        "venda_atual": 350.00
    },
    "Unidade Shopping (Loja 02)": {
        "funcionarios": ["Mariana (Gerente)", "Bruno (Atendente)", "Dona Maria (Cozinheira)"],
        "estoque": {"Tapioca Recheada": 50, "Cuscuz Recheado": 34, "Bolo de Macaxeira": 27, "Suco Regional": 67, "Café da Manhã Completo": 17},
        "meta_diaria": 2000.00,
        "venda_atual": 850.00
    },
    "Unidade Norte (Loja 03)": {
        "funcionarios": ["Renato (Gerente)", "Bruna (Atendente)", "Dona Marta (Cozinheiro)"],
        "estoque": {"Tapioca Recheada": 50, "Cuscuz Recheado": 34, "Bolo de Macaxeira": 27, "Suco Regional": 67, "Café da Manhã Completo": 17},
        "meta_diaria": 1500.00,
        "venda_atual": 400.00
    }
}

formas_pagamento = {
    1: "Pix",
    2: "Cartão de Débito",
    3: "Cartão de Crédito"
}

dados_matriz = {
    "vendas_totais_reais": 1600.00, 
    "produtos_vendidos": {"Tapioca Recheada": 20, "Cuscuz Recheado": 15, "Bolo de Macaxeira": 10},
    "auditoria_alertas": [
        "ALERTA AUDITORIA: Desconto de 10% aplicado via App no pedido #102",
        "ALERTA AUDITORIA: Cancelamento de 1x Cuscuz feito pelo Funcionario1 às 08h32"
    ]
}

materiais_sistema = {
    "Matriz": [
        "Manual do Funcionario",
        "Contrato Padrão da Franquia (Jurídico)",
    ],
    "Franquias (Operação Local)": [
        "Ficha Técnica: Tapiocas e Cuscuz",
        "Manual de Atendimento Humano e Boas Vindas",
        "Guia de Higiene e Controle de Estoque Local"
    ]
}