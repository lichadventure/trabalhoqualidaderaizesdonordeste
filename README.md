# Trabalho qualidade rede Raizes do Nordeste
Sobre o projeto

Este projeto foi feito para a disciplina chamada Projeto: Engenharia de Software, com foco em Qualidade de Software (QA) do Centro Universitário Internacional Uninter.
A ideia é simular um sistema de uma rede de restaurantes chamada Raízes do Nordeste, onde dá para fazer pedidos, ver o cardápio, simular pagamentos, acompanhar o status dos pedidos, fazer relatorios de estoque e funcionarios.
O objetivo principal é testar se o sistema funciona bem, se está rápido, seguro e se aguenta muitos usuários ao mesmo tempo.

O que este projeto faz:
Simula pedidos em um restaurante;
Mostra cardápio;
Permite cancelar pedidos;
Simula pagamento;
Controle simples de estoque;
Login de cliente e administrador;
Gera relatórios simples.

Ferramentas usadas:
Python: linguagem principal do sistema
Flask: para criar o sistema
Locust: para testar de carga simula muitos usuários ao mesmo tempo
OWASP ZAP: para teste segurança de dados
GitHub: para armazenar o código fonte

Arquivos do projeto:
main.py - arquivo principal para rodar o sistema
app_flask.py - parte do sistema que cria e funciona como APIs
telas.py - organização de telas e menus
dados_sistema.py - guarda os dados do sistema
locustfile.py - testes de carga e estresse

Testes feitos:
Teste de login (certo e errado)
Teste de pedidos com estoque e sem estoque
Teste de relatorios
Teste do sistema completo de pedidos
Simulação de até 500 pessoas usando o sistema ao mesmo tempo
Testes de segurança
Testes de desempenho e carga (velocidade do sistema)

O que foi analisado:
O sistema deve responder rápido (1 a 2 segundos)
Deve funcionar quase sempre (99,5% do tempo)
Não pode falhar muito (menos de 2%)
Deve aguentar muitas pessoas usando ao mesmo tempo
Deve ser seguro com os dados dos usuários conforme a Lei Geral de Proteção de Dados (LGPD)

Quesito Segurança:
O sistema devara seguir boas práticas conforme a lei (LGPD)
Proteção de dados dos usuários
Cuidados com informações pessoais e frageis
Simulação de segurança com ferramentas de teste
impedir o vazamento de informações e dados

Como rodar o projeto:
Instale o Python no computador
Instale as bibliotecas necessárias (Flask e Locust)
Abra o terminal na pasta do projeto
Rode o sistema com: python main.py
