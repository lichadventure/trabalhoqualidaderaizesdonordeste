# Importa login e as telas
from dados_sistema import usuarios
from telas import tela_cliente, tela_funcionario, tela_chefe

# SISTEMA PRINCIPAL COM RETORNO

while True:
    
    print("SISTEMA RAIZES DO NORDESTE")
    print("\n[Dados protegido conforme Lei Geral da Proteção de Dados (LGPD)]")
   

    usuario_digitado = input("Digite seu Usuário ou 'sair' para fechar): ").lower()

    if usuario_digitado == "sair":
        print("\nEncerrando o sistema da franquia . Até logo!")
        break

    senha_digitada = input("Digite sua Senha: ")

    if usuario_digitado in usuarios and usuarios[usuario_digitado]["senha"] == senha_digitada:
        perfil = usuarios[usuario_digitado]["perfil"]
        loja_do_usuario = usuarios[usuario_digitado]["loja"]
        print(f"\nLogin realizado com sucesso! Perfil: {perfil}")

        # Redirecionamento do login
        if perfil == "CLIENTE":
            tela_cliente()
        elif perfil == "FUNCIONARIO":
            tela_funcionario(usuario_digitado, loja_do_usuario)
        elif perfil == "ADM":
            tela_chefe()

        print("\n" + "-" * 45)
        escolha_pos_pedido = input("Deseja fazer um novo login no menu? (S/N): ").upper()

        if escolha_pos_pedido != "S":
            print("\nObrigado por utilizar nosso sistema. Encerrando programa!")
            break
    else:
        print("\n Usuário ou senha incorretos! Tente novamente.")
        print("-" * 45)